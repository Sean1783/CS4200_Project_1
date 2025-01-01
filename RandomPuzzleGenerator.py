import random

class RandomPuzzleGenerator:

    def generate_random_puzzle_string(self):
        puzzle_string = ""
        i = 0
        while i < 9:
            random_num = random.randint(0, 8)
            valid_num = self.is_valid_num(puzzle_string, random_num)
            if valid_num:
                puzzle_string += str(random_num) + " "
                i += 1
        return puzzle_string

    def is_valid_num(self, puzzle_string, num):
        return self.is_num_in_range(num) and not self.is_num_in_string(puzzle_string, num)

    def is_num_in_string(self, puzzle_string, num):
        return str(num) in puzzle_string

    def is_num_in_range(self, num):
        return 0 <= num <= 8

    def generate_state_config_from_string(self, puzzle_string):
        x = puzzle_string.split()
        state_config = list()
        row_one = [int(num) for num in x[:3]]
        row_two = [int(num) for num in x[3:6:]]
        row_three = [int(num) for num in x[6:9:]]
        state_config.append(row_one)
        state_config.append(row_two)
        state_config.append(row_three)
        return state_config

    def generate_random_state_config(self, target_state):
        state_config_string = self.generate_random_puzzle_string()
        target_state_string = target_state.get_key_string()
        while not self.is_target_reachable(target_state_string, state_config_string):
            state_config_string = self.generate_random_puzzle_string()
        return self.generate_state_config_from_string(state_config_string)

    def is_target_reachable(self, target_state, initial_state):
        target_total_inversions = self.compute_inversions(target_state)
        initial_total_misplaced = self.compute_inversions(initial_state)
        target_orientations = target_total_inversions % 2
        initial_orientations = initial_total_misplaced % 2
        return target_orientations == initial_orientations

    def compute_inversions(self, some_state_string):
        state_string = some_state_string[:].replace("0", "")
        total_inversions = 0
        for i in range(len(state_string)-1):
            for j in range(i, len(state_string)-1):
                if state_string[j] > state_string[j+1]:
                    total_inversions += 1
        return total_inversions


