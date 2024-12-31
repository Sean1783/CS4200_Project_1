class Dialogue:

    def puzzle_selection_prompt(self):
        prompt = ("Select:\n"
        + "[1] Single Test Puzzle\n"
       + "[2] Multi-Test Puzzle\n"
       + "[3] Exit")
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

