class Dialogue:

    def select_or_exit_prompt(self):
        prompt = ("Select:\n"
        + "[Enter] Begin the testing sequence.\n"
        + "[:q]    Exit the current sequence at any point.")
        print(prompt)

    def input_selection_prompt(self):
        prompt = ("Select initial puzzle state generation method:\n"
        + "[1] Create a random initial puzzle configuration.\n"
        + "[2] Extract puzzle configurations from a file.\n")
        print(prompt)

    def depth_prompt(self):
        prompt = "Enter Solution Depth (2-20):"
        print(prompt)

    def select_h_function_prompt(self):
        prompt = ("Select H function:\n"
        + "[1] H1\n"
        + "[2] H2")
        print(prompt)

    def solution_not_found(self, depth):
        print("Solution not found at depth " + str(depth))

    def execution_time(self, execution_time_value):
        print(f'Execution time: {execution_time_value:.6f} seconds')

    def search_cost(self, search_cost):
        print("Search cost: " + str(search_cost))

    def search_deptht(self, search_depth):
        print("Max search depth: " + str(search_depth))

    def search_complete(self, execution_time, search_cost, depth):
        self.execution_time(execution_time)
        self.search_cost(search_cost)
        self.search_deptht(depth)
        print("")

    def file_name_prompt(self):
        prompt = "Enter File Name:"
        print(prompt)

