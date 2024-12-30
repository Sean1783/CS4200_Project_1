from puzzleState import *
from puzzleStateComparator import *


class PuzzleNode:
    def __init__(self, state: PuzzleState):
        self.state = state
        self.key = self.make_key_string()
        self.parent = None
        self.children = list()
        self.h1_cost = 0
        self.h2_cost = 0


    def calculate_h_costs(self, target_puzzle_state: PuzzleState):
        state_comparator = PuzzleStateComparator()
        self.h1_cost = state_comparator.num_misplaced(target_puzzle_state, self.state)
        self.h2_cost = state_comparator.total_difference(target_puzzle_state, self.state)


    def get_parent_h_costs(self) -> (int, int):
        if self.parent:
            parent_costs = self.parent.get_parent_h_costs()
            return parent_costs[0], parent_costs[1]
        else:
            return 0, 0


    def create_total_costs(self, target_puzzle_state: PuzzleState) -> None:
        self.calculate_h_costs(target_puzzle_state)
        parent_h_costs = self.get_parent_h_costs()
        self.h1_cost += parent_h_costs[0]
        self.h2_cost += parent_h_costs[1]


    def enumerate_child_nodes(self) -> None:
        alternate_states = self.state.generate_alternate_states()
        for state in alternate_states:
            puzzle_node = PuzzleNode(state)
            puzzle_node.set_parent(self)
            self.children.append(puzzle_node)


    def get_state(self) -> PuzzleState:
        return self.state


    def get_costs(self) -> (int, int):
        return self.h1_cost, self.h2_cost


    def get_parent(self):
        return self.parent


    def get_configuration(self) -> list[list[int]]:
        return self.state.get_configuration()


    def get_children(self):
        return self.children


    def set_parent(self, parent) -> None:
        self.parent = parent


    def make_key_string(self) -> str:
        state_config = self.get_configuration()
        key_string = ""
        for row in state_config:
            for value in row:
                key_string += str(value) + " "
        return key_string

    def to_string(self) -> str:
        state_config_string = self.state.to_string()
        return (("{\n" +
                repr(self) + "\n" +
                "\tkey:" + self.key + ",\n" +
                state_config_string + ",\n" +
                "\th1_cost:" + str(self.h1_cost) + ",\n" +
                "\th2_cost:" + str(self.h2_cost)) + "\n" +
                "\tparent:" + repr(self.parent) + "\n" +
                "}")

    def get_key(self) -> str:
        return copy.copy(self.key)

    def print_parent(self)  -> None:
        print(self.key)
        if self.parent is not None:
            self.parent.print_parent()