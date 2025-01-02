# 8-Puzzle Solver

This program solves instances of the [8 puzzle game](https://en.wikipedia.org/wiki/15_puzzle) via the A* algorithm. 


## Installation

To run this program, you'll need Python 3.9 or newer installed (due to type hinting usage). 

1. Clone the repository:
   ```bash
   git clone https://github.com/Sean1783/CS4200_Project_1
   cd project-name
   ```

2. Install Python (if you don’t already have it):
   - Download Python from [https://www.python.org/downloads/](https://www.python.org/downloads/).

3. Run the program:
   ```bash
   python main.py
   ```

No additional dependencies are required as the program uses Python's standard libraries.


## Usage

Run the program with:
```bash
python main.py
```

The user can quit the current sequence at any input prompt by entering the below:
```
:q
```

An integer argument can be provided that sets the maximum depth that the program will search. If no argument is provided, the default search depth is 25. The search will terminate if no solution is found at this depth.
```bash
python main.py 12
```

The user will be prompted to select the method of generating the initial puzzle state.
```
Select initial puzzle state generation method:
[1] Create a random initial puzzle configuration.
[2] Extract puzzle configurations from a file.
```
Option 1 will create a randomly generated initial state from which the target state is _theoretically_ reachable although the search depth might exceed user's given depth value.

Option 2 allows the user to provide their own initial states to use. 
```
Enter file name:
<source file name here>
```
Please ensure your configurations have the following format:
```
/
1 2 5
3 4 8
6 7 0
/
1 2 5
3 0 4
6 7 8
```

The user will be prompted to choose a which heuristic the A* search algorithm should use.
```
Select H function:
[1] H1
[2] H2
```
The program will output search results:
```
***Solution found***
Execution time: 0.081573 seconds
Search cost: 462
Max search depth: 20
```

Below is the default target state for the search. This configuration can be changed via the target_state_config in main.py.
```
0 1 2
3 4 5
6 7 8
```