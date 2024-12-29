from puzzleState import *


class PuzzleNode:
    def __init__(self, state: PuzzleState):
        self.state = state
        self.key = self.make_key_string()
        self.parent = None
        self.children = list()

    def enumerate_child_nodes(self) -> None:
        alternate_states = self.state.generate_alternate_states()
        for state in alternate_states:
            puzzle_node = PuzzleNode(state)
            puzzle_node.set_parent(self)
            self.children.append(puzzle_node)

    def get_parent(self) -> PuzzleState:
        return self.parent

    def get_configuration(self) -> list[list[int]]:
        return self.state.get_configuration()

    def set_parent(self, parent) -> None:
        self.parent = parent

    def make_key_string(self) -> str:
        state_config = self.get_configuration()
        key_string = ""
        for row in state_config:
            for value in row:
                key_string += str(value) + " "
        return key_string

    def print_parent(self)  -> None:
        print(self.key)
        if self.parent is not None:
            self.parent.print_parent()