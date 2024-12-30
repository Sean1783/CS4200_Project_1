import sys
from PuzzleNode import *
from PuzzleState import *
from PuzzleStateComparator import *
from PuzzleSearch import *
from Frontier import *
from InputHandler import *


def main():
    print('Hello there', sys.argv[1])


def puzzle_state_test():
    state = PuzzleState([[1, 2, 3], [0, 4, 5], [6, 7, 8]])
    child_states = state.generate_alternate_states()
    for child_state in child_states:
        print("{\n", child_state.to_string(), "\n}\n", sep="")


def puzzle_node_test():
    state = PuzzleState([
        [1, 2, 3],
        [0, 4, 5],
        [6, 7, 8]
    ])
    target_state = PuzzleState([
        [1, 2, 3],
        [4, 6, 5],
        [0, 8, 7]
    ])
    n1 = PuzzleNode(state, 0)
    n1.calculate_h_costs(target_state)
    # print(n1.to_string())
    # print(n1.key)
    n1.enumerate_child_nodes()
    for child_node in n1.children:
        child_node.calculate_h_costs(target_state)
        print(child_node.to_string())


def frontier_test():
    state = PuzzleState([
        [4, 2, 3],
        [1, 8, 6],
        [7, 5, 0]
    ])

    target_state = PuzzleState([
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ])

    nodes_created = 0

    root_node = PuzzleNode(state, 0, 2)
    root_node.compute_f_cost(target_state)
    root_node.enumerate_child_nodes()

    frontier = Frontier()
    frontier.push(root_node)
    closed_list = dict()
    closed_list[root_node.get_key()] = root_node

    psc = PuzzleStateComparator()

    while frontier:
        current_node = frontier.pop()[2]
        current_state = current_node.get_state()
        is_match = psc.matches_target_state(target_state, current_state)
        if is_match:
            # current_node.print_parents()
            current_node.show_root_to_leaf_path()
            break
        child_nodes = current_node.get_child_nodes()
        nodes_created += len(child_nodes)
        for node in child_nodes:
            if node.get_key() not in closed_list:
                node.compute_f_cost(target_state)
                node.enumerate_child_nodes()
                frontier.push(node)

    print("Search cost:", nodes_created)

    # for element in frontier.p_queue:
    #     print(element[2].to_string())

    # frontier.append({n1.make_key_string(): n1})
    # for node in n1.children:
    #     node.create_total_costs(target_state)
    #     node.enumerate_child_nodes()
    #     if node.get_key() not in frontier:
    #         frontier.append({node.key: node})
    #     for child in node.children:
    #         child.create_total_costs(target_state)
    #         if child.get_key() not in frontier:
    #             frontier.append({child.key: child})

    # frontier.append({n1.get_key() : n1, "cost" : n1.get_costs()[0]})
    # for i in range(4):
    #     # for key, puzzle_node in frontier[i].items():
    #     for key in frontier[i].keys():
    #         node = frontier[i][key]
    #         node.create_total_costs(target_state)
    #         node.enumerate_child_nodes()
    #         # puzzle_node.create_total_costs(target_state)
    #         # puzzle_node.enumerate_child_nodes()
    #         # for child_node in puzzle_node.get_children():
    #         #     if child_node.get_key() not in frontier:
    #         #         frontier.append({child_node.get_key() : child_node})
    #
    #
    # psc = PuzzleStateComparator()
    # for element in frontier:
    #     for key, puzzle_node in element.items():
    #         current_node_state = puzzle_node.get_state()
    #         matches_target = psc.matches_target_state(target_state, current_node_state)
    #         print(matches_target)


def puzzle_state_comparator_test():
    psc = PuzzleStateComparator()
    state = PuzzleState([[1, 2, 3], [0, 4, 5], [6, 7, 8]])
    target_state = PuzzleState([[1, 2, 3], [4, 6, 5], [0, 8, 7]])
    location_map = psc.create_value_location_map(state)
    target_location_map = psc.create_value_location_map(target_state)
    print(location_map)
    print(target_location_map)
    print(psc.total_difference(target_state, state))
    print(psc.num_misplaced(target_state, state))

def puzzle_search_test():
    state = PuzzleState([
        [0, 1, 4],
        [8, 7, 6],
        [3, 5, 2]
    ])

    target_state = PuzzleState([
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ])

    puzzle_search = PuzzleSearch(target_state, state, 1)
    puzzle_search.search(16)

def main_interaction_sequence():
    puzzle_selection = ("Select:\n"
                + "[1] Single Test Puzzle\n"
                + "[2] Multi-Test Puzzle\n"
                + "[3] Exit\n")
    print(puzzle_selection)
    input_handler = InputHandler()
    puzzle_option_selection = input_handler.validate_puzzle_selection()

    input_selection = ("Select Input Method:\n"
        + "[1] Random\n"
        + "[2] File\n")

    print(input_selection)
    input_selection = input_handler.validate_input_selection()

    solution_depth = "Enter Solution Depth (2-20):\n"
    print(solution_depth)
    input_handler.validate_solution_depth()


if __name__ == '__main__':
    # main()
    # frontier_test()
    # puzzle_node_test()
    # puzzle_state_test()
    # puzzle_state_comparator_test()
    # puzzle_search_test()
    main_interaction_sequence()

