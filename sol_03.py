# Advent of Code 2023: Day 3


lower_offset = 96 # ascii a = 97
upper_offset = 38 # ascii A = 65

filename = './input/input_03.txt'
with open(filename) as file:
    lines = [line.rstrip() for line in file]

priority = 0
badge_priority = 0
line_count = 0
group = []
for line in lines:
    divide = int(len(line)/2)
    a, b = set(line[:divide]), set(line[divide:])
    intersection = ord([el_a for el_a in a for el_b in b if el_a == el_b][0]) # by inspection, single element intersection
    priority += intersection - lower_offset if intersection >= lower_offset else intersection - upper_offset
    
    line_count += 1
    group.append(line)
    if line_count % 3 == 0:
        group_intersection = ord([el_a for el_a in group[0] for el_b in group[1] for el_c in group[2] if el_a == el_b == el_c][0])
        badge_priority += group_intersection - lower_offset if group_intersection >= lower_offset else group_intersection - upper_offset
        group = []

print(f'priority, badge_priority: {priority}, {badge_priority}')

