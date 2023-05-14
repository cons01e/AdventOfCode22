# Advent of Code: day 1

import lib


lines = lib.read_input("input/input_01.txt") 

snacks = []             # list of snack tuples defined as (list of individual snacks, total calories)
current_snack = []      # list of snack items in the current iteration
current_calories = 0    # total calories in the current snack iteration
for line in lines:
    if line != '':
        current_snack.append(int(line))
        current_calories += int(line)
    else:
        snacks.append( (current_snack, current_calories) )
        current_snack = []
        current_calories = 0

# sort the list of snacks from highest to lowest based on total calories
snacks = sorted(snacks, key=lambda snack: snack[1], reverse=True)

print('top three snacks:')
for i in range(3):
    print(f'snack {i + 1}: {snacks[i][1]} calories, snacks = {snacks[i][0]}')
print(f'total calories in top 3: {snacks[0][1] + snacks[1][1] + snacks[2][1]}')
