import heapq
from PuzzleNode import *

class Frontier:
    def __init__(self):
        self.p_queue = []

    def push(self, puzzle_node : PuzzleNode):
        f_cost = puzzle_node.get_f_cost()
        heapq.heappush(self.p_queue, (f_cost, id(puzzle_node), puzzle_node))

    def pop(self):
        return heapq.heappop(self.p_queue)

    def peek(self):
        return self.p_queue[0] if self.p_queue else None

    def is_empty(self):
        return len(self.p_queue) == 0


