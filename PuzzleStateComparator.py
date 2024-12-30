from PuzzleState import *

class PuzzleStateComparator:

    def create_value_location_map(self, puzzle_state: PuzzleState) -> {int : (int, int)}:
        value_location_map = dict()
        config = puzzle_state.get_configuration()
        for row_idx in range(len(config)):
            for value in config[row_idx]:
                col_idx = config[row_idx].index(value)
                coordinates = (col_idx, row_idx)
                value_location_map[value] = coordinates
        return value_location_map


    def total_difference(self, target_state : PuzzleState, current_state : PuzzleState) -> int:
        aggregate_difference = 0
        target_value_location_map = self.create_value_location_map(target_state)
        current_value_location_map = self.create_value_location_map(current_state)
        for key, value in target_value_location_map.items():
            target_coordinates = target_value_location_map[key]
            current_coordinates = current_value_location_map[key]
            x_difference = abs(target_coordinates[0] - current_coordinates[0])
            y_difference = abs(target_coordinates[1] - current_coordinates[1])
            aggregate_difference += (x_difference + y_difference)
        return aggregate_difference


    def num_misplaced(self, target_state : PuzzleState, current_state : PuzzleState) -> int:
        total_misplaced = 0
        target_value_location_map = self.create_value_location_map(target_state)
        current_value_location_map = self.create_value_location_map(current_state)
        for key, value in target_value_location_map.items():
            target_coordinates = target_value_location_map[key]
            current_coordinates = current_value_location_map[key]
            if target_coordinates[0] != current_coordinates[0] or target_coordinates[1] != current_coordinates[1]:
                total_misplaced += 1
        return total_misplaced


    def matches_target_state(self, target_state : PuzzleState, current_state : PuzzleState) -> bool:
        target_value_location_map = self.create_value_location_map(target_state)
        current_value_location_map = self.create_value_location_map(current_state)
        for key in target_value_location_map.keys():
            if current_value_location_map[key] != target_value_location_map[key]:
                return False
        return True

