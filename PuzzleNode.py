from PuzzleState import *
from PuzzleStateComparator import *


class PuzzleNode:
    def __init__(self, state: PuzzleState, g_cost: int, h_function: int):
        self.state = state
        self.key = self.make_key_string()
        self.parent = None
        self.children = list()
        self.h_function = h_function
        self.h_cost = 0
        self.f_cost = 0
        self.g_cost = g_cost

    def calculate_h1_cost(self, target_puzzle_state: PuzzleState) -> int:
        state_comparator = PuzzleStateComparator()
        h_cost = state_comparator.num_misplaced(target_puzzle_state, self.state)
        return h_cost

    def calculate_h2_cost(self, target_puzzle_state: PuzzleState) -> int:
        state_comparator = PuzzleStateComparator()
        h_cost = state_comparator.total_difference(target_puzzle_state, self.state)
        return h_cost

    def compute_f_cost(self, target_puzzle_state: PuzzleState) -> None:
        h_cost = 0
        if self.h_function == 1:
            h_cost = self.calculate_h1_cost(target_puzzle_state)
        elif self.h_function == 2:
            h_cost = self.calculate_h2_cost(target_puzzle_state)
        self.f_cost = self.g_cost + h_cost

    def enumerate_child_nodes(self) -> None:
        alternate_states = self.state.generate_alternate_states()
        for state in alternate_states:
            puzzle_node = PuzzleNode(state, self.g_cost + 1, self.h_function)
            puzzle_node.set_parent(self)
            self.children.append(puzzle_node)

    def get_state(self) -> PuzzleState:
        return self.state

    def get_h_costs(self) -> (int, int):
        # return self.h1_cost, self.h2_cost
        return self.h_cost

    def get_f_cost(self) -> int:
        return self.f_cost

    def get_g_cost(self) -> int:
        return self.g_cost

    def get_parent(self):
        return self.parent

    def get_puzzle_state_configuration(self) -> list[list[int]]:
        return self.state.get_configuration()

    def get_child_nodes(self):
        return self.children

    def get_key(self) -> str:
        return copy.copy(self.key)

    def set_parent(self, parent_node) -> None:
        self.parent = parent_node

    def make_key_string(self) -> str:
        state_config = self.get_puzzle_state_configuration()
        key_string = ""
        for row in state_config:
            for value in row:
                key_string += str(value) + " "
        return key_string

    def show_root_to_leaf_path(self):
        node_stack = list()
        current_node = self
        node_stack.append(current_node)
        current_node = self.parent
        while current_node is not None:
            node_stack.append(current_node)
            current_node = current_node.get_parent()
        while node_stack:
            node = node_stack.pop()
            print("Step : ", node.g_cost)
            node.get_state().print_configuration()

    def print_parents(self) -> None:
        print("Step : ", self.g_cost)
        self.get_state().print_configuration()
        if self.parent is not None:
            self.parent.print_parents()

    def to_string(self) -> str:
        state_config_string = self.state.to_string()
        return ("{\n" +
                 repr(self) + "\n" +
                 "\tkey:" + self.key + ",\n" +
                 state_config_string + ",\n" +
                 "\tg_cost:" + str(self.g_cost) + ",\n" +
                 "\tf_cost:" + str(self.f_cost) + ",\n" +
                 "\th_cost:" + str(self.h_cost) + ",\n" +
                "\tparent:" + repr(self.parent) + "\n" +
                "}")
