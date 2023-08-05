# Advent of Code 2022
# Day 10


import lib
from numpy import full


def draw_pixel(crt, cycle, x):
    row = cycle // 40
    col = cycle % 40
    sprite = range(x - 1, x + 2)
    crt_char = '#' if col in sprite else '.'
    print(cycle_count, x, sprite, crt_char, row, col)
    crt[row, col] = crt_char


sid = lib.read_input("input/sample/sample_10.txt")
fid = lib.read_input("input/full/input_10.txt")

cycle_count = 0
x = 1
check_cycles = [20, 60, 100, 140, 180, 220]
check_signals = []
crt = full((6,40), '0')
print(crt)

for ins in fid:
    draw_pixel(crt, cycle_count, x)
    cycle_count += 1

    if ins == "noop":
        continue

    draw_pixel(crt, cycle_count, x)
    x += int(ins.split(" ")[1])
    cycle_count += 1

   # if ins == "noop":
   #     ins_type = ins
   #     cycles = 1
   # else:
   #     ins_type, x_inc = ins.split(" ")
   #     cycles = 2

   # for cycle in range(1, cycles + 1):
   #     # part 2
   #     sprite_range = range(x - 1, x + 1)
   #     crt_row = cycle_count // 40
   #     crt_row_pos = cycle_count % 40
   #     crt_char = '#' if cycle_count in sprite_range else '.'
   #     print(cycle_count, crt_row, crt_row_pos)
   #     crt[crt_row, crt_row_pos] = crt_char

   #     cycle_count += 1
   #     if ins_type == "addx" and cycle == cycles:
   #         x += int(x_inc)
   #     if cycle_count in check_cycles:
   #         check_signals.append(cycle_count * x)

print(sum(check_signals))
print(crt)

for row in range(6):
    for col in range(40):
        print(crt[row, col], end='')
    print()

