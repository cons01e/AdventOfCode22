# This file serves as a small library of commonly used utils


# Get a puzzles input in the form of an array of input strings
def read_input(input_file_path):
    with open(input_file_path) as input_file:
        lines = [line.rstrip() for line in input_file]
    return lines

