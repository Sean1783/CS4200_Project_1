from PuzzleState import *
from Frontier import *

class PuzzleSearch:
    def __init__(self, target_state : PuzzleState, initial_state : PuzzleState, h_function : int):
        self.initial_state = initial_state
        self.target_state = target_state
        self.h_function = h_function
        # self.search_cost = 0


    def search(self, depth : int) -> (bool, int):
        search_cost = 0
        root_node = PuzzleNode(self.initial_state, 0, self.h_function)
        root_node.compute_f_cost(self.target_state)
        root_node.enumerate_child_nodes()

        frontier = Frontier()
        frontier.push(root_node)
        explored_list = dict()

        psc = PuzzleStateComparator()
        is_goal_reached = False

        while not frontier.is_empty():
            _, _, current_node = frontier.pop()
            current_depth = current_node.get_g_cost()
            if current_depth > depth:
                # break
                continue
            explored_list[current_node.get_key()] = current_node
            current_state = current_node.get_state()
            is_goal_reached = psc.matches_target_state(self.target_state, current_state)
            if is_goal_reached:
                current_node.show_root_to_leaf_path()
                break
            child_nodes = current_node.get_child_nodes()
            for node in child_nodes:
                node_key = node.get_key()
                node_cost = node.get_g_cost()
                twin_node = explored_list.get(node_key)
                twin_node_cost = twin_node.get_g_cost() if twin_node is not None else node_cost + 1
                if node_key not in explored_list or node_cost < twin_node_cost:
                    search_cost += 1
                    node.compute_f_cost(self.target_state)
                    node.enumerate_child_nodes()
                    frontier.push(node)
                    explored_list[node_key] = node
                # else:
                #     twin_node = explored_list[node.get_key()]
                #     if twin_node.get_g_cost() > node.get_g_cost():
                #         search_cost += 1
                #         node.compute_f_cost(self.target_state)
                #         node.enumerate_child_nodes()
                #         frontier.push(node)
                #         explored_list[node.get_key()] = node

        return is_goal_reached, search_cost


