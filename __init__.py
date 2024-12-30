import sys
from puzzleNode import *
from puzzleState import *
from puzzleStateComparator import *


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
    n1 = PuzzleNode(state)
    n1.calculate_h_costs(target_state)
    # print(n1.to_string())
    # print(n1.key)
    n1.enumerate_child_nodes()
    for child_node in n1.children:
        child_node.calculate_h_costs(target_state)
        print(child_node.to_string())


def frontier_test():
    state = PuzzleState([
        [1, 2, 3],
        [0, 4, 5],
        [6, 7, 8]
    ])

    target_state = PuzzleState([
        [1, 2, 3],
        [4, 5, 0],
        [6, 7, 8]
    ])

    n1 = PuzzleNode(state)
    # n1.create_total_costs(target_state)
    # n1.enumerate_child_nodes()
    frontier = list()
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

    frontier.append({n1.get_key() : n1})
    for i in range(4):
        for key, puzzle_node in frontier[i].items():
            puzzle_node.create_total_costs(target_state)
            puzzle_node.enumerate_child_nodes()
            for child_node in puzzle_node.get_children():
                frontier.append({child_node.get_key() : child_node})

    psc = PuzzleStateComparator()
    for element in frontier:
        for key, puzzle_node in element.items():
            current_node_state = puzzle_node.get_state()
            matches_target = psc.matches_target_state(target_state, current_node_state)
            print(matches_target)


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


if __name__ == '__main__':
    # main()
    frontier_test()
    # puzzle_node_test()
    # puzzle_state_test()
    # puzzle_state_comparator_test()