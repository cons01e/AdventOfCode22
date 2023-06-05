# Advent of Code 2022
# Day 6


import lib


# data = "bvwbjplbgvbhsrlpgdmjqwftvncz"
full_data_path = "input/full/input_06.txt"
lines = lib.read_input(full_data_path)

data = lines[0]
marker_pos = 3 # minimum eligible starting position
while marker_pos < len(data):
    marker = data[marker_pos - 4:marker_pos]
    if len(set(marker)) == 4:
        break
    marker_pos += 1

print(marker_pos)

