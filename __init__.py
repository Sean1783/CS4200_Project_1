import sys
from puzzleNode import *
from puzzleState import *


def main():
  print ('Hello there', sys.argv[1])


def puzzle_state_test():
  state = PuzzleState([[1, 2, 3], [0, 4, 5], [6, 7, 8]])
  child_states = state.generate_alternate_states()
  for child_state in child_states:
    child_state.print_configuration()
    print("\n")


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
  frontier = dict()
  frontier[n1.key] = n1
  for node in n1.children:
    frontier[node.key] = node

  for item in frontier:
    print(frontier[item].key)


if __name__ == '__main__':
  # main()
  frontier_test()
  # puzzle_node_test()
  # puzzle_state_test()