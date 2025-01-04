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
[3] Enter configuration manually.
```
**Option 1** will create a randomly generated initial state from which the target state is _theoretically_ reachable although the required search depth might exceed user's given or default max depth.

**Option 2** allows the user to provide their own initial states to use via a separate file. 
```
Enter file name:
<source file name here>
```
Please ensure your configurations have the following format in your source file:
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
**Option 3** allows the user to manually input a string representing the initial state.
```
1 0 2 3 4 5 6 7 8
```
*There is no validation checking done for this input method. If the string is not valid - contains too many / not enough values / incorrect values / etc. - or the target state is not reachable, the program may crash.* 

The user will be prompted to choose which heuristic the A* search algorithm will use.
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

Below is the default target state for the search. This configuration can be changed via the target_state_config variable in main.py.
```
0 1 2
3 4 5
6 7 8
```