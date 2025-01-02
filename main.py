import sys

from application_sequence import *

def main():
    target_state_config = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8]
    ]
    max_solution_depth = int(sys.argv[1]) if len(sys.argv) > 1 else 25
    main_sequence(target_state_config, max_solution_depth)

if __name__ == '__main__':
    main()





