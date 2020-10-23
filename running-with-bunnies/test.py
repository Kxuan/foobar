import sys
import os
from pprint import pprint

sys.path.append(os.getcwd())

import solution

pprint(solution.solution(
    [[0, 0, 0, 0, 0, 0],
 [1, 1, 1, 1, 1, 0],
 [0, 0, 0, 0, 0, 0],
 [0, 1, 1, 1, 1, 1],
 [0, 1, 1, 1, 1, 1],
 [0, 0, 0, 0, 0, 0]], 0))

pprint(solution.solution(
    [[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, -4, 0, 1], [1, 1, 1, 1, 0]], 3))

pprint(solution.solution(
    [[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 3))

pprint(solution.solution(
    [[0, 2, 2, 2, -1],
     [9, 0, 2, 2, -1],
     [9, 3, 0, 2, -1],
     [9, 3, 2, 0, -1],
     [9, 3, 2, 2, 0]], 1))

pprint(solution.solution(
    [[0, 0, 0, 0, 1],
     [0, 0, 0, 0, 1],
     [0, 0, 0, 0, 1],
     [0, 0, 0, 0, 1],
     [0, 0, 0, 0, 0]], 0))
