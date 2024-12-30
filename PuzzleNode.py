from PuzzleState import *
from PuzzleStateComparator import *


class PuzzleNode:
    def __init__(self, state: PuzzleState, g_cost : int):
        self.state = state
        self.key = self.make_key_string()
        self.parent = None
        self.children = list()
        self.g_cost = g_cost
        self.h1_cost = 0
        self.h2_cost = 0
        self.f_cost = 0


    def calculate_h_costs(self, target_puzzle_state: PuzzleState):
        state_comparator = PuzzleStateComparator()
        self.h1_cost = state_comparator.num_misplaced(target_puzzle_state, self.state)
        self.h2_cost = state_comparator.total_difference(target_puzzle_state, self.state)


    # def get_parent_h_costs(self) -> (int, int):
    #     if self.parent:
    #         parent_costs = self.parent.get_parent_h_costs()
    #         return parent_costs[0], parent_costs[1]
    #     else:
    #         return 0, 0


    # Use this to determine which heuristic to use for f_cost.
    def create_total_costs(self, target_puzzle_state: PuzzleState) -> None:
        self.calculate_h_costs(target_puzzle_state)
        # self.f_cost = self.h1_cost + self.g_cost
        self.f_cost = self.h2_cost + self.g_cost
        # parent_h_costs = self.get_parent_h_costs()
        # self.h1_cost += parent_h_costs[0]
        # self.h2_cost += parent_h_costs[1]


    def enumerate_child_nodes(self) -> None:
        alternate_states = self.state.generate_alternate_states()
        for state in alternate_states:
            puzzle_node = PuzzleNode(state, self.g_cost + 1)
            puzzle_node.set_parent(self)
            self.children.append(puzzle_node)


    def get_state(self) -> PuzzleState:
        return self.state


    def get_h_costs(self) -> (int, int):
        return self.h1_cost, self.h2_cost


    def get_total_cost(self) -> int:
        return self.f_cost


    def get_parent(self):
        return self.parent


    def get_puzzle_state_configuration(self) -> list[list[int]]:
        return self.state.get_configuration()


    def get_children(self):
        return self.children


    def get_key(self) -> str:
        return copy.copy(self.key)


    def set_parent(self, parent) -> None:
        self.parent = parent


    def make_key_string(self) -> str:
        state_config = self.get_puzzle_state_configuration()
        key_string = ""
        for row in state_config:
            for value in row:
                key_string += str(value) + " "
        return key_string


    def print_parents(self)  -> None:
        print(self.to_string(), ",", sep="")
        if self.parent is not None:
            self.parent.print_parents()


    def to_string(self) -> str:
        state_config_string = self.state.to_string()
        return (("{\n" +
                repr(self) + "\n" +
                "\tkey:" + self.key + ",\n" +
                state_config_string + ",\n" +
                "\tg_cost:" + str(self.g_cost) + ",\n" +
                "\tf_cost:" + str(self.f_cost) + ",\n" +
                "\th1_cost:" + str(self.h1_cost) + ",\n" +
                "\th2_cost:" + str(self.h2_cost)) + "\n" +
                "\tparent:" + repr(self.parent) + "\n" +
                "}")


