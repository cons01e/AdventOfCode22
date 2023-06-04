# Advent of Code 2023
# Day 5


import sys
import lib

# read problem input
part = int(sys.argv[1])
sample_input = "input/sample/sample_05.txt"
full_input = "input/full/input_05.txt"
input_lines = lib.read_input(full_input)

# initialize variables
moves = list()
stacks = list()

# parse input
for line_num, line in enumerate(input_lines):
    # empty line indicates separation between stacks and moves
    if line == "":
        # extract the raw line data
        char_lines = input_lines[:line_num-1]
        num_stacks = int(input_lines[line_num-1].rstrip()[-1])
        moves = input_lines[line_num+1:]

        # create the character matrix
        # matrix must be square to allow for transposition
        # size determined by num_stacks (num_stacks > char_lines)
        # this leads to an additional row of 0s to be cleaned later
        char_matrix = [[0] * num_stacks for _ in range(num_stacks)]
        for i, char_line in enumerate(char_lines):
            # start from first stack char and iterate over remaining
            for j, char_index in enumerate(range(1, len(char_line), 4)):
                if char_line[char_index] != " ":
                    char_matrix[i][j] = char_line[char_index]


        # create the list of stacks by tranposing the character matrix
        stacks = [[0] * num_stacks for _ in range(num_stacks)]
        for row in range(len(char_matrix)):
            for col in range(len(char_matrix)):
                stacks[row][col] = char_matrix[col][row]

        # reverse the stacks and remove the leading and trailing 0s
        for row in stacks:
            row.reverse()
            row.pop(0)
            while row[-1] == 0:
                row.pop()

        # parsing of the input is complete
        break

# perform the stack operations
for move in moves:
    # sample move "move 1 from 2 to 1"
    move_words = move.split(" ")
    n = int(move_words[1])
    src = int(move_words[3]) - 1 # decrement for 0 indexed stack list
    dst = int(move_words[5]) - 1

    match part:
        case 1:
        # part 1: for each move n, pop from src stack onto dst stack
            while n > 0:
                stacks[dst].append(stacks[src].pop())
                n -= 1
        case 2:
        # part 2: append last n elements of src stack onto dst stack then
        # remove those elements from src stack
            stacks[dst] = stacks[dst] + stacks[src][-n:]
            del stacks[src][-n:]
        case _:
            print("unexpected part number")
            quit()

# read the top of each stack
stack_tops = "".join([stack[-1] for stack in stacks])
print("top create of each stack:", stack_tops)

