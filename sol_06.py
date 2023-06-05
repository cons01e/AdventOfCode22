# Advent of Code 2022
# Day 6
# todo: optimize


import sys
import lib


part = int(sys.argv[1])
# data = "bvwbjplbgvbhsrlpgdmjqwftvncz"
full_data_path = "input/full/input_06.txt"
lines = lib.read_input(full_data_path)

data = lines[0]
marker_len = 4 if part == 1 else 14
marker_pos = marker_len - 1 # minimum eligible starting position
while marker_pos < len(data):
    marker = data[marker_pos - marker_len:marker_pos]
    if len(set(marker)) == marker_len:
        break
    marker_pos += 1

print(marker_pos)

