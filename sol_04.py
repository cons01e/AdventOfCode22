# Advent of Code 2023: Day 4


with open('./input/input_04.txt') as file:
    lines = [line.rstrip() for line in file]

contained_pairs = 0
overlapping_pairs = 0
for line in lines:
    # line format: a-b,c-d
    A,B = [range(int(e[0]), int(e[1]) + 1) for e in [e.split('-') for e in line.split(',')]]
    
    # part 1
    if A.start <= B.start and A.stop >= B.stop or B.start <= A.start and B.stop >= A.stop:
        contained_pairs += 1
   
    # part 2
    if A.start in B or A.stop - 1 in B or B.start in A or B.stop - 1 in A:
        overlapping_pairs += 1

print("contained pairs", contained_pairs, "\noverlapping pairs", overlapping_pairs)

