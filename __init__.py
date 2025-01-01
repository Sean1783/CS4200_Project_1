import sys
import time

from PuzzleSearch import *
from InputHandler import *
from RandomPuzzleGenerator import *
from Dialogue import *
from PuzzleExtractor import *


def user_puzzle_validation(target_config, initial_state_list):
    rpg = RandomPuzzleGenerator()
    are_puzzles_reachable = rpg.validate_user_puzzles(target_config, initial_state_list)
    if not are_puzzles_reachable:
        handler = InputHandler()
        handler.user_puzzle_handling()


def test_sequence(initial_state_config, target_config, max_solution_depth):

    solution_depth = max_solution_depth
    dialogue = Dialogue()

    initial_state = PuzzleState(initial_state_config)
    dialogue.select_h_function_prompt()

    input_handler = InputHandler()
    selected_h_function = input_handler.validate_h_function()
    if selected_h_function == ":q":
        return ":q"

    target_state = PuzzleState(target_config)
    puzzle_search = PuzzleSearch(target_state, initial_state, selected_h_function)
    start_time = time.time()
    found, search_cost, depth = puzzle_search.search(solution_depth)
    end_time = time.time()
    execution_time = end_time - start_time
    if not found:
        dialogue.solution_not_found(solution_depth)
        depth -= 1
    dialogue.search_complete(execution_time, search_cost, depth)


def main_sequence(target_config, max_depth):

    puzzle_option_selection = 1
    while puzzle_option_selection != 2:

        dialogue = Dialogue()
        dialogue.select_or_exit_prompt()
        input_handler = InputHandler()
        puzzle_option_selection = input_handler.validate_puzzle_selection()

        if puzzle_option_selection != ":q":
            dialogue.input_selection_prompt()
            input_method = input_handler.validate_input_selection()
            if input_method == 1:
                rpg = RandomPuzzleGenerator()
                target_state = PuzzleState(target_config)
                initial_state_config = rpg.generate_random_state_config(target_state)
                print("Initial puzzle state: ")
                for row in initial_state_config:
                    for element in row:
                        print(element, end=" ")
                    print()
                user_response = test_sequence(initial_state_config, target_config, max_depth)
                if user_response == ":q":
                    break
            elif input_method == 2:
                dialogue.file_name_prompt()
                file_name = input_handler.validate_file_exists()
                if file_name == ":q":
                    break
                extractor = PuzzleExtractor()
                initial_state_list = extractor.extract_puzzles_from_file(file_name)

                user_puzzle_validation(target_config, initial_state_list)

                for initial_state_config in initial_state_list:
                    user_response = test_sequence(initial_state_config, target_config, max_depth)
                    if user_response == ":q":
                        break
            elif input_method == ":q":
                    break
        else:
            print("Goodbye")
            break

def main():
    target_state_config = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]]
    max_solution_depth = int(sys.argv[1]) if len(sys.argv) > 1 else 25
    # max_solution_depth = 25
    main_sequence(target_state_config, max_solution_depth)

if __name__ == '__main__':
    main()





