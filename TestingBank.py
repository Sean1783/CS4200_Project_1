import sys
import time

from PuzzleSearch import *
from Frontier import *
from InputHandler import *
from RandomPuzzleGenerator import *
from Dialogue import *
from PuzzleExtractor import *


def main():
    print('Hello there', sys.argv[1])


def puzzle_state_test():
    state = PuzzleState([[1, 2, 3], [0, 4, 5], [6, 7, 8]])
    child_states = state.generate_alternate_states()
    for child_state in child_states:
        print("{\n", child_state.to_string(), "\n}\n", sep="")


def puzzle_node_test():
    state = PuzzleState([
        [1, 2, 3],
        [0, 4, 5],
        [6, 7, 8]
    ])
    target_state = PuzzleState([
        [1, 2, 3],
        [4, 6, 5],
        [0, 8, 7]
    ])
    n1 = PuzzleNode(state, 0)
    n1.calculate_h_costs(target_state)
    # print(n1.to_string())
    # print(n1.key)
    n1.enumerate_child_nodes()
    for child_node in n1.children:
        child_node.calculate_h_costs(target_state)
        print(child_node.to_string())


def frontier_test():
    state = PuzzleState([
        [4, 2, 3],
        [1, 8, 6],
        [7, 5, 0]
    ])

    target_state = PuzzleState([
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ])

    nodes_created = 0

    root_node = PuzzleNode(state, 0, 2)
    root_node.compute_f_cost(target_state)
    root_node.enumerate_child_nodes()

    frontier = Frontier()
    frontier.push(root_node)
    closed_list = dict()
    closed_list[root_node.get_key()] = root_node

    psc = PuzzleStateComparator()

    while frontier:
        current_node = frontier.pop()[2]
        current_state = current_node.get_state()
        is_match = psc.matches_target_state(target_state, current_state)
        if is_match:
            # current_node.print_parents()
            current_node.show_root_to_leaf_path()
            break
        child_nodes = current_node.get_child_nodes()
        nodes_created += len(child_nodes)
        for node in child_nodes:
            if node.get_key() not in closed_list:
                node.compute_f_cost(target_state)
                node.enumerate_child_nodes()
                frontier.push(node)

    print("Search cost:", nodes_created)

def puzzle_state_comparator_test():
    psc = PuzzleStateComparator()
    state = PuzzleState([[1, 2, 3], [0, 4, 5], [6, 7, 8]])
    target_state = PuzzleState([[1, 2, 3], [4, 6, 5], [0, 8, 7]])
    location_map = psc.create_value_location_map(state)
    target_location_map = psc.create_value_location_map(target_state)
    print(location_map)
    print(target_location_map)
    print(psc.total_difference(target_state, state))
    print(psc.num_misplaced(target_state, state))


def puzzle_search_test():
    state = PuzzleState([
        [0, 1, 4],
        [8, 7, 6],
        [3, 5, 2]
    ])

    target_state = PuzzleState([
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ])

    puzzle_search = PuzzleSearch(target_state, state, 1)
    puzzle_search.search(20)


def random_puzzle_generator_test():
    rpg = RandomPuzzleGenerator()
    random_puzzle = rpg.generate_random_puzzle_string()
    print(random_puzzle)
    state_config = rpg.generate_state_config_from_string(random_puzzle)
    print(state_config)


def puzzle_extractor_test():
    extractor = PuzzleExtractor()
    matrices = extractor.extract_puzzles_from_file("project1/Length4.txt")
    for m in matrices:
        print(m)
