from pathlib import Path


class InputHandler:

    def validate_puzzle_selection(self):
        user_input = input()
        while user_input != "":
            if self.quit_program(user_input):
                return user_input
            print("Invalid input.")
            user_input = input()

    def validate_input_selection(self):
        user_input = input()
        while user_input != "1" and user_input != "2" and user_input != "3":
            if self.quit_program(user_input):
                return user_input
            print("Invalid input.")
            user_input = input()
        return int(user_input)

    def validate_solution_depth(self):
        valid_input = False
        while not valid_input:
            try:
                user_input = int(input())
                if self.quit_program(user_input):
                    return user_input
                if not 0 < user_input <= 25:
                    valid_input = False
                    print("Invalid input. Please enter a positive integer.")
                    continue
                valid_input = True
                return int(user_input)
            except ValueError:
                print("Invalid input. Please enter a positive integer.")

    def validate_h_function(self):
        user_input = input()
        while user_input != "1" and user_input != "2":
            if self.quit_program(user_input):
                return user_input
            print("Invalid input.")
            user_input = input()
        return int(user_input)

    def validate_file_exists(self):
        file_name = input()
        my_file = Path(file_name)
        while not my_file.is_file():
            if self.quit_program(file_name):
                return file_name
            print("File not found.")
            print("Enter a valid file path.")
            file_name = input()
            my_file = Path(file_name)
        return file_name

    def user_puzzle_handling(self):
        print("The target puzzle is not reachable by one or more user input puzzles.")
        user_input = input("Press enter to continue.")
        while user_input != "":
            user_input = input("Press enter to continue.")

    def quit_program(self, user_input):
        if ":q" in user_input:
            return True

    def manual_configuration_handler(self) -> str:
        validated_config_string = ""
        validation_complete = False
        while not validation_complete:
            validation_complete = True
            print("Enter a valid configuration string.\n")
            manually_entered_configuration = input().split()
            for value in manually_entered_configuration:
                if self.quit_program(value):
                    return value
                if not value.isdigit():
                    print("Invalid input.")
                    validation_complete = False
                    validated_config_string = ""
                    break
                else:
                    validated_config_string += value + " "
            if validated_config_string == "":
                print("Invalid input.")
                validation_complete = False

        return validated_config_string


