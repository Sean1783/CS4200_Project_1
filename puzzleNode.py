from puzzleState import *


class PuzzleNode:
    def __init__(self, state : PuzzleState):
        self.state = state
        self.key = self.state.get_key_string()
        self.parent = None
        self.children = list()
        # self.enumerate_child_nodes()


    def enumerate_child_nodes(self):
        alternate_states = self.state.generate_alternate_states()
        for state in alternate_states:
            puzzle_node = PuzzleNode(state)
            puzzle_node.parent = self
            self.children.append(puzzle_node)


    def print_parent(self):
        print(self.key)
        if self.parent is not None:
            self.parent.print_parent()

