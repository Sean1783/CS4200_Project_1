import copy


class PuzzleState:
    def __init__(self, configuration):
        self.configuration = configuration
        self.x, self.y = self.find_coordinates(0)

    def set_configuration(self, configuration):
        self.configuration = configuration
        self.x, self.y = self.find_coordinates(0)

    def find_coordinates(self, value):
        for row_index, row in enumerate(self.configuration):
            if value in row:
                column_index = row.index(value)
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
        if self.x - 1 >= 0:
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

    def get_configuration(self) -> list[list[int]]:
        config = list()
        for row in self.configuration:
            row_copy = copy.deepcopy(row)
            config.append(row_copy)
        return config

    def get_key_string(self):
        key_string = ""
        for row in self.configuration:
            for value in row:
                key_string += str(value) + " "
        return key_string

    def to_string(self) -> str:
        config_string = ""
        for row in self.configuration:
            config_string += "\t\t\t"
            for value in row:
                config_string += str(value) + " "
            config_string += "\n"
        config_string = config_string[:-1]
        return "\tconfiguration:\n" + config_string
                # ",\n\tblank coordinate:" +
                # str(self.x) + " " + str(self.y))

    def print_configuration(self):
        for row in self.configuration:
            row_string = ""
            for value in row:
                row_string += str(value) + " "
            print(row_string)