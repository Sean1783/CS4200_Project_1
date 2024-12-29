import copy

class PuzzleState:
    def __init__(self, configuration):
        self.configuration = configuration
        self.x, self.y = self.find_coordinates()


    def set_configuration(self, configuration):
        self.configuration = configuration
        self.x, self.y = self.find_coordinates()


    def find_coordinates(self):
        for row_index, row in enumerate(self.configuration):
            if 0 in row:
                column_index = row.index(0)
                return row_index, column_index
        return None


    def generate_alternate_states(self):
        state_array = list()
        if self.x + 1 <= 2:
            val_1 = self.configuration[self.x + 1][self.y]
            alt_config_1 = copy.deepcopy(self.configuration)
            alt_config_1[self.x + 1][self.y] = 0
            alt_config_1[self.x][self.y] = val_1
            state_array.append(PuzzleState(alt_config_1))
        if self.x -1 >= 0:
            val_2 = self.configuration[self.x - 1][self.y]
            alt_config_2 = copy.deepcopy(self.configuration)
            alt_config_2[self.x - 1][self.y] = 0
            alt_config_2[self.x][self.y] = val_2
            state_array.append(PuzzleState(alt_config_2))
        if self.y + 1 <= 2:
            val_3 = self.configuration[self.x][self.y + 1]
            alt_config_3 = copy.deepcopy(self.configuration)
            alt_config_3[self.x][self.y + 1] = 0
            alt_config_3[self.x][self.y] = val_3
            state_array.append(PuzzleState(alt_config_3))
        if self.y - 1 >= 0:
            val_4 = self.configuration[self.x][self.y - 1]
            alt_config_4 = copy.deepcopy(self.configuration)
            alt_config_4[self.x][self.y - 1] = 0
            alt_config_4[self.x][self.y] = val_4
            state_array.append(PuzzleState(alt_config_4))
        return state_array


    def print_configuration(self):
        for row in self.configuration:
            print(row)


    def get_key_string(self):
        key_string = ""
        for row in self.configuration:
            for value in row:
                key_string += str(value) + " "
        return key_string