

import lib

# read problem input
sample_input = "input/sample/sample_05.txt"
full_input = "input/input/input_05.txt"
input_lines = lib.read_input(sample_input)

# initialize variables
num_stacks = 0 
moves = list()
stacks = list()

# parse input
for line_num, line in enumerate(input_lines):
    if line == "":
        # extract the raw line data
        raw_stacks = input_lines[:line_num-1]
        num_stacks = int(input_lines[line_num-1].rstrip()[-1])
        moves = input_lines[line_num+1:]
        
        # create the list of stacks
        for _ in range(num_stacks):
            stacks.append([0] * num_stacks)

        # populate stacks
        for i, raw_stack in enumerate(raw_stacks):
            # start from first stack char and iterate over remaining
            for char_num, char_index in enumerate(range(1, len(raw_stack), 4)):
                char = raw_stack[char_index]
                stacks[i][char_num] = ("0" if char == " " else char)

        break

