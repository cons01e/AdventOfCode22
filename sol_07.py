# Advent of Code: Day 7

import re
import lib


class Node:
    def __init__(self, parent, name):
        self.parent = parent
        self.dirs = []
        self.files = []
        self.name = name 
        self.size = 0

    def compute_size(self):
        for file in self.files:
            filesize, filename = file
            self.size += filesize
        for dir in self.dirs:
            self.size += dir.compute_size()
        return self.size


def find_valid_dirs(node, valid_nodes, filesize):
    if node is None:
        return
    if node.size <= filesize:
        valid_nodes.append(node)
    for dir in node.dirs:
        find_valid_dirs(dir, valid_nodes, filesize)


sample_data_file = "input/sample/sample_07.txt"
full_data_file = "input/full/input_07.txt"
lines = lib.read_input(full_data_file)

node_ptr = root = None
for line in lines:
    # handle commands
    if line[0] == "$":
        line_elements = line.split(" ")
        # handle cd command 
        if len(line_elements) > 2:
            cd_arg = line_elements[-1]
            if cd_arg == "..":
                node_ptr = node_ptr.parent
            elif cd_arg == "/":
                node_ptr = root = Node(None, cd_arg)
            else:
                for node in node_ptr.dirs:
                    if node.name == cd_arg:
                        node_ptr = node
                        break
        # else ls command, no need to handle
    # handle ls output
    # either "dir <dir_name>" or "<file_size> <file_name>"
    else:
        line_elements = line.split(" ")
        if line_elements[0] == "dir":
            node_ptr.dirs.append(Node(node_ptr, line_elements[1]))
        else:
            node_ptr.files.append(tuple((int(line_elements[0]), line_elements[1])))

# compute dir sizes
root.compute_size()

# find dirs with size under 100000
valid_dirs = []
filesize = 100000
find_valid_dirs(root, valid_dirs, filesize)

# compute the total size of valid dirs
total_size = 0
for dir in valid_dirs:
    total_size += dir.size

print(f"Total size: {total_size}")

