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
    state = PuzzleState([[1, 2, 3], [0, 4, 5], [6, 7, 8]])
    n1 = PuzzleNode(state)
    print(n1.key)
    n1.enumerate_child_nodes()
    for child_node in n1.children:
        print(child_node.key)


def frontier_test():
    state = PuzzleState([[1, 2, 3], [0, 4, 5], [6, 7, 8]])
    n1 = PuzzleNode(state)
    n1.enumerate_child_nodes()
    frontier = list()
    frontier.append({n1.make_key_string(): n1})
    for node in n1.children:
        frontier.append({node.key: node})
        # node.enumerate_child_nodes()

    for element in frontier:
        for key, puzzle_node in element.items():
            print(key, puzzle_node.get_configuration())

def puzzle_state_comparator_test():
    psc = PuzzleStateComparator()
    state = PuzzleState([[1, 2, 3], [0, 4, 5], [6, 7, 8]])
    target_state = PuzzleState([[1, 2, 3], [4, 6, 5], [0, 8, 7]])
    location_map = psc.create_value_location_map(state)
    target_location_map = psc.create_value_location_map(target_state)
    print(location_map)
    print(target_location_map)
    print(psc.calculate_difference(target_state, state))
    print(psc.number_of_misplaced_tiles(target_state, state))


if __name__ == '__main__':
    # main()
    # frontier_test()
    # puzzle_node_test()
    # puzzle_state_test()
    puzzle_state_comparator_test()