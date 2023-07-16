# Advent of Code 2022
# Day 9


import lib


class KnotNode:
    def __init__(self, prv, nxt, pos):
        self.prv = prv
        self.nxt = nxt
        self.pos = pos


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

def move_tail(head, tail, visited_spaces, tailknot):
    dx, dy = distance(head, tail)
    if abs(dx) + abs(dy) > 2:   # diagonal move
        print("diagonal")
        tail[0] += 1 * sign(dx)
        tail[1] += 1 * sign(dy)
    elif abs(dx) > 1:   # horizonal move
        print("horizontal")
        tail[0] += 1 * sign(dx)
    elif abs(dy) > 1:   # vertial move
        print("vertial")
        tail[1] += 1 * sign(dy)
    if tailknot:
        visited_spaces.add(tuple(tail))

def move_knots(prev, curr, visited_spaces):
    dx, dy = distance(prev.pos, curr.pos)
    if abs(dx) + abs(dy) > 2:   # diagonal move
        print("diagonal")
        curr.pos[0] += 1 * sign(dx)
        curr.pos[1] += 1 * sign(dy)
    elif abs(dx) > 1:   # horizonal move
        print("horizontal")
        curr.pos[0] += 1 * sign(dx)
    elif abs(dy) > 1:   # vertial move
        print("vertial")
        curr.pos[1] += 1 * sign(dy)
    if curr.nxt is None:
        print(f"adding {(curr.pos)} to set")
        visited_spaces.add(tuple(curr.pos))

sample_data = lib.read_input("input/sample/sample_09.txt")
sample_data_extra = lib.read_input("input/sample/sample_09_extra.txt")
full_data = lib.read_input("input/full/input_09.txt")

#head = [0,0]
#tail = [0,0]
#visited_spaces = set()
#for line in full_data:
#    direction, moves = line.split(" ")
#    moves = int(moves)
#
#    while moves:
#        move_head(head, direction)
#        move_tail(head, tail, visited_spaces, True)
#        moves -= 1
#
#print(len(visited_spaces))

rope = KnotNode(None, None, [0,0])
knot = rope
for _ in range(9):
    new_knot = KnotNode(knot, None, [0,0])
    knot = new_knot
    new_knot.prv.nxt = new_knot

rope_visited_spaces = set()
for line in full_data:
    direction, moves = line.split(" ")
    moves = int(moves)

    print("\n\n*** NEW MOVE ***\n\n")


    while moves:
        move_head(rope.pos, direction)
        knot = rope.nxt
        while knot is not None:
            move_knots(knot.prv, knot, rope_visited_spaces)
            knot = knot.nxt
        moves -= 1

print(len(rope_visited_spaces))
