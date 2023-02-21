# Advent of Code: Day 3
# 
# algo
#   1. split line in half
#   2. find duplicates
#   3. set priority

lower_offset = 96 # ascii a = 97
upper_offset = 38 # ascii A = 65

filename = './input/input_03.txt'
with open(filename) as file:
    lines = [line.rstrip() for line in file]

priority = 0
for line in lines:
    divide = int(len(line)/2)
    a, b = set(line[:divide]), set(line[divide:])
    intersection = ord([el_a for el_a in a for el_b in b if el_a == el_b][0]) # by inspection, single element intersection
    priority += intersection - lower_offset if intersection >= lower_offset else intersection - upper_offset
print(priority)

