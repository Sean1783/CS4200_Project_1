

class InputHandler():
    def __init__(self):
        pass

    def validate_puzzle_selection(self):
        user_input = input()
        while user_input != "1" and user_input != "2" and user_input != "3":
            print("Invalid input.")
            user_input = input()
        return user_input

    def validate_input_selection(self):
        user_input = input()
        while user_input != "1" and user_input != "2":
            print("Invalid input.")
            user_input = input()
        return user_input

    def validate_solution_depth(self):
        valid_input = False
        while not valid_input:
            try:
                user_input = int(input())
                if user_input < 1:
                    valid_input = False
                    print("Invalid input. Please enter a positive integer.")
                    continue
                valid_input = True
                return user_input
            except ValueError:
                print("Invalid input. Please enter a positive integer.")

