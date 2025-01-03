import random
from puzzle_state import *


class RandomPuzzleGenerator:

    def generate_random_puzzle_string(self) -> str:
        puzzle_string = ""
        i = 0
        while i < 9:
            random_num = random.randint(0, 8)
            valid_num = self.is_valid_num(puzzle_string, random_num)
            if valid_num:
                puzzle_string += str(random_num) + " "
                i += 1
        return puzzle_string

    def is_valid_num(self, puzzle_string : str, num : int) -> bool:
        return self.is_num_in_range(num) and not self.is_num_in_string(puzzle_string, num)

    def is_num_in_string(self, puzzle_string : str, num : int) -> bool:
        return str(num) in puzzle_string

    def is_num_in_range(self, num : int) -> bool:
        return 0 <= num <= 8

    def generate_state_config_from_string(self, puzzle_string : str) -> list[list[int]]:
        x = puzzle_string.split()
        state_config = list()
        row_one = [int(num) for num in x[:3]]
        row_two = [int(num) for num in x[3:6:]]
        row_three = [int(num) for num in x[6:9:]]
        state_config.append(row_one)
        state_config.append(row_two)
        state_config.append(row_three)
        return state_config

    def generate_random_state_config(self, target_state : PuzzleState) -> list[list[int]]:
        state_config_string = self.generate_random_puzzle_string()
        target_state_string = target_state.get_key_string()
        while not self.is_target_reachable(target_state_string, state_config_string):
            state_config_string = self.generate_random_puzzle_string()
        return self.generate_state_config_from_string(state_config_string)

    def is_target_reachable(self, target_state_string : str, initial_state_string : str) -> bool:
        target_total_inversions = self.compute_inversions(target_state_string)
        initial_state_total_inversions = self.compute_inversions(initial_state_string)
        target_orientation = target_total_inversions % 2
        initial_orientation = initial_state_total_inversions % 2
        return target_orientation == initial_orientation

    def compute_inversions(self, some_state_string : str) -> int:
        state_string = [int(i) for i in some_state_string.split() if i != "0"]
        total_inversions = 0
        for i in range(len(state_string)):
            for j in range(i + 1, len(state_string)):
                if state_string[i] > state_string[j]:
                    total_inversions += 1
        return total_inversions

    def validate_user_puzzles(self, target_config : list[list[int]], user_puzzles : list[list[list[int]]]) -> bool:
        target_state = PuzzleState(target_config)
        for puzzle in user_puzzles:
            state = PuzzleState(puzzle)
            target_is_reachable = self.is_target_reachable(target_state.get_key_string(), state.get_key_string())
            if not target_is_reachable:
                return False
        return True
