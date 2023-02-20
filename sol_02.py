# A -> rock, B -> paper, C -> scissors
# Part 1: X -> rock, Y -> paper, Z -> scissors
# Part 2: X -> loss, Y -> draw, Z -> win


outcomes = [
    [0, 0, 0, 0],
    [0, 1, 0, 2],
    [0, 2, 1, 0],
    [0, 0, 2, 1]
]
fixed_outcomes = [
    [0, 0, 0, 0],
    [0, 3, 1, 2],
    [0, 1, 2, 3],
    [0, 2, 3, 1]
]
map_a = {'A': 1, 'B': 2, 'C': 3}
map_b = {'X': 1, 'Y': 2, 'Z': 3}

input_file = "./input/input_02.txt"
with open(input_file) as file:
    lines = [line.rstrip() for line in file]

scores = [0, 0]
for line in lines:
    a, b = line.split()
    scores[0] += map_b[b] + 3 * outcomes[map_b[b]][map_a[a]]
    scores[1] += fixed_outcomes[map_a[a]][map_b[b]] + 3 * outcomes[fixed_outcomes[map_a[a]][map_b[b]]][map_a[a]]

print(f'scores: {scores}')

