# Advent of Code 2023
# Day 8

import numpy
from math import prod
import lib


def visibility_score(cell_val, subranges):
    for sr in subranges:
        if len(sr) == 0 or cell_val > max(sr):
            return 1
    return 0

def directional_score(cell_val, subrange):
    if len(subrange) == 0:
        return 0
    for i, el in enumerate(subrange, 1):
        if cell_val <= el:
            break
    return i


# PARSE INPUT
sample_data_file = "input/sample/sample_08.txt"
full_data_file = "input/full/input_08.txt"
lines = lib.read_input(full_data_file)
M = numpy.array([list(map(int, line)) for line in lines])

visible_trees = 0
max_score = 0
for i, row in enumerate(M):
    for j, cell_val in enumerate(row):
        col = M[:, j]
        subranges = [
            row[j+1:],                  # right
            list(reversed(row[:j])),    # left
            col[i+1:],                  # down
            list(reversed(col[:i]))     # up
        ]
        
        # PART 1
        visible_trees += visibility_score(cell_val, subranges)

        # PART 2
        score = prod([directional_score(cell_val, sr) for sr in subranges])
        if score > max_score:
            max_score = score

print(visible_trees, max_score)

