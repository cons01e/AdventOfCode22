# Advent of Code 2022
# Day 10


import lib


sid = lib.read_input("input/sample/sample_10.txt")
fid = lib.read_input("input/full/input_10.txt")

cycle_count = 1
x = 1
check_cycles = [20, 60, 100, 140, 180, 220]
check_signals = []

for ins in fid:
    if ins == "noop":
        ins_type = ins
        cycles = 1
    else:
        ins_type, x_inc = ins.split(" ")
        cycles = 2

    for cycle in range(1, cycles + 1):
        cycle_count += 1
        if ins_type == "addx" and cycle == cycles:
            x += int(x_inc)
        if cycle_count in check_cycles:
            check_signals.append(cycle_count * x)

print(sum(check_signals))
