class Dialogue:

    def select_or_exit_prompt(self) -> None:
        prompt = (
            "\n" +
            "[Enter] Begin the testing sequence.\n" +
            "[:q]    Exit the current sequence at any point.")
        print(prompt)

    def input_selection_prompt(self) -> None:
        prompt = (
            "Select initial puzzle state generation method:\n" +
            "[1] Create a random initial puzzle configuration.\n" +
            "[2] Extract puzzle configurations from a file.\n" +
            "[3] Enter configuration manually.\n")
        print(prompt)

    def depth_prompt(self) -> None:
        prompt = "Enter Solution Depth (2-20):"
        print(prompt)

    def select_h_function_prompt(self) -> None:
        prompt = (
            "Select H function:\n" +
            "[1] H1\n" +
            "[2] H2")
        print(prompt)

    def solution_not_found(self, depth) -> None:
        print("Solution not found at depth " + str(depth))

    def execution_time(self, execution_time_value : float) -> None:
        print(f'Execution time: {execution_time_value:.6f} seconds')

    def search_cost(self, search_cost : int) -> None:
        print("Search cost: " + str(search_cost))

    def search_deptht(self, search_depth : int) -> None:
        print("Max search depth: " + str(search_depth))

    def solution_found(self):
        print("***Solution found***")

    def search_complete(self, execution_time : float, search_cost : int, depth : int) -> None:
        self.execution_time(execution_time)
        self.search_cost(search_cost)
        self.search_deptht(depth)
        print("")

    def file_name_prompt(self) -> None:
        prompt = "Enter file name:"
        print(prompt)

    def manual_input_prompt(self) -> None:
        prompt = (
            "Enter values in the order they appear from left to right\n" +
            "and top to bottom in your puzzle. Separate the values with a space.\n" +
            "Use a '0' to represent the blank cell in your puzzle.\n\n"
            "1 2 3\n" +
            "4 0 5\t--->\t1 2 3 4 0 5 6 7 8\n" +
            "6 7 8\n"
        )
        print(prompt)