class Dialogue:

    def select_or_exit_prompt(self) -> None:
        prompt = (
            "Select:\n"
            + "[Enter] Begin the testing sequence.\n"
            + "[:q]    Exit the current sequence at any point.")
        print(prompt)

    def input_selection_prompt(self) -> None:
        prompt = (
            "Select initial puzzle state generation method:\n" +
            "[1] Create a random initial puzzle configuration.\n" +
            "[2] Extract puzzle configurations from a file.\n")
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
