
class Snack:
    def __init__(self, snacks, calories):
        self.snacks = snacks
        self.calories = calories

input_file = "./input/input_01.txt"
snacks = []

with open(input_file) as file:
    lines = [line.rstrip() for line in file]

current_snack = []
current_calories = 0
for line in lines:
    if line != '':
        current_snack.append(int(line))
        current_calories += int(line)
    else:
        snacks.append(Snack(current_snack, current_calories)) 
        current_snack = []
        current_calories = 0

snacks = sorted(snacks, key=lambda snack: snack.calories, reverse=True)

print('top three snacks:')
for i in range(3):
    print(f'snack {i + 1}: {snacks[i].calories} calories, snacks = {snacks[i].snacks}')
print(f'total calories in top 3: {snacks[0].calories + snacks[1].calories + snacks[2].calories}')
