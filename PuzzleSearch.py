from PuzzleState import *
from Frontier import *

class PuzzleSearch:
    def __init__(self, target_state : PuzzleState, initial_state : PuzzleState, h_function : int):
        self.initial_state = initial_state
        self.target_state = target_state
        self.h_function = h_function
        self.search_cost = 0


    def search(self, depth : int) -> None:

        root_node = PuzzleNode(self.initial_state, 0, self.h_function)
        root_node.compute_f_cost(self.target_state)
        root_node.enumerate_child_nodes()

        frontier = Frontier()
        frontier.push(root_node)
        explored_list = dict()
        root_node_key = root_node.get_key()
        explored_list[root_node_key] = root_node

        psc = PuzzleStateComparator()
        is_match = False
        while frontier:
            current_node = frontier.pop()[2]
            current_depth = current_node.get_g_cost()
            if current_depth > depth:
                break
            current_state = current_node.get_state()
            is_match = psc.matches_target_state(self.target_state, current_state)
            if is_match:
                current_node.show_root_to_leaf_path()
                break
            child_nodes = current_node.get_child_nodes()
            for node in child_nodes:
                if node.get_key() not in explored_list:
                    self.search_cost += 1
                    node.compute_f_cost(self.target_state)
                    node.enumerate_child_nodes()
                    frontier.push(node)

        if not is_match:
            print("No solution found at depth ", depth)
        print("Search cost:", self.search_cost)

