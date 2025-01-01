class Dialogue:

    def select_or_exit_prompt(self):
       #  prompt = ("Select:\n"
       #  + "[1] Single Test Puzzle\n"
       # + "[2] Multi-Test Puzzle\n"
       # + "[3] Exit")

        prompt = ("Select:\n"
                  + "[1] Test Puzzle\n"
                  + "[2] Exit")
        print(prompt)

    def input_selection_prompt(self):
        prompt = ("Select Input Method:\n"
          + "[1] Random\n"
          + "[2] File")
        print(prompt)

    def depth_prompt(self):
        prompt = "Enter Solution Depth (2-20):"
        print(prompt)

    def select_h_function_prompt(self):
        prompt = ("Select H Function:\n"
        + "[1] H1\n"
         + "[2] H2")
        print(prompt)

    def solution_not_found(self, depth):
        print("Solution not found at depth " + str(depth))

    def execution_time(self, execution_time_value):
        print(f'Execution time: {execution_time_value:.6f} seconds')

    def search_cost(self, search_cost):
        print("Search Cost:" + str(search_cost))

    def search_complete(self, execution_time, search_cost):
        self.execution_time(execution_time)
        self.search_cost(search_cost)
        print("")
