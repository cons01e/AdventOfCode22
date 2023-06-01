

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
    # an empty line indicates the separation between the stack representations
    # and the list of moves
    if line == "":
        # extract the raw line data
        char_lines = input_lines[:line_num-1]
        num_stacks = int(input_lines[line_num-1].rstrip()[-1])
        moves = input_lines[line_num+1:]
        
        # create the character matrix
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

        # reverse the stacks and remove the trailing 0s
        for row in stacks:
            row.reverse()
            while row[-1] == 0:
                row.pop()

        # parsing of the input is complete
        break

# perform the stack operations
for move in moves:
    print(move)

