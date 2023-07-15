# Advent of Code 2022
# Day 9


import lib


def sign(x):
    return 1 if x > 0 else -1

def distance(head, tail):
    dx = head[0] - tail[0]
    dy = head[1] - tail[1]
    return (dx, dy)

def move_head(head, direction):
    match direction:
        case "R":
            head[0] += 1
        case "L":
            head[0] -= 1
        case "D":
            head[1] += 1
        case "U":
            head[1] -= 1

def move_tail(head, tail, visited_spaces):
    dx, dy = distance(head, tail)
    if abs(dx) + abs(dy) > 2:   # diagonal move
        tail[0] += 1 * sign(dx)
        tail[1] += 1 * sign(dy)
    elif abs(dx) > 1:   # horizonal move
        tail[0] += 1 * sign(dx)
    elif abs(dy) > 1:   # vertial move
        tail[1] += 1 * sign(dy)
    visited_spaces.add(tuple(tail))

sample_data = lib.read_input("input/sample/sample_09.txt")
full_data = lib.read_input("input/full/input_09.txt")

head = [0,0]
tail = [0,0]
visited_spaces = set()
for line in full_data:
    direction, moves = line.split(" ")
    moves = int(moves)

    while moves:
        move_head(head, direction)
        move_tail(head, tail, visited_spaces)
        moves -= 1

print(len(visited_spaces))
