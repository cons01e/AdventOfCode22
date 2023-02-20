# part 1
# A -> rock, B -> paper, C -> scissors
# X -> rock, Y -> paper, Z -> scissors
#
# part 1 score: ally_move + 3C[ally_move][enemy_move]
# part 2 score: F(enemy_move, outcome) + 3C[F(enemy_move, outcome)][enemy_move]

outcomes = [
    [0, 0, 0, 0],
    [0, 1, 0, 2],
    [0, 2, 1, 0],
    [0, 0, 2, 1]
]
fixed_outcomes = {
    'AX': 3, 'AY': 1, 'AZ': 2,
    'BX': 1, 'BY': 2, 'BZ': 3,
    'CX': 2, 'CY': 3, 'CZ': 1
}
enemy_moves = {'A': 1, 'B': 2, 'C': 3}
ally_moves = {'X': 1, 'Y': 2, 'Z': 3}

input_file = "./input/input_02.txt"
with open(input_file) as file:
    lines = [line.rstrip() for line in file]

score_a = 0
score_b = 0
for line in lines:
    enemy_move, ally_move = line.split()
    score_a += ally_moves[ally_move] + 3 * outcomes[ally_moves[ally_move]][enemy_moves[enemy_move]]
    score_b += fixed_outcomes[enemy_move + ally_move] + 3 * outcomes[fixed_outcomes[enemy_move + ally_move]][enemy_moves[enemy_move]]

print(f'part 1 score: {score_a}\npart 2 score: {score_b}')
