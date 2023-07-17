# Advent of Code 2022
# Day 9


import lib


class KnotNode:
    def __init__(self, prv, nxt, pos):
        self.prv = prv
        self.nxt = nxt
        self.pos = pos

class Rope:
    def __init__(self, size):
        self.head = self.construct_rope(size)
        self.tail_locations = set()

    def construct_rope(self, size):
        knot = rope = KnotNode(None, None, [0,0])
        for _ in range(size - 1):
            knot.nxt = KnotNode(knot, None, [0,0])
            knot = knot.nxt
        return rope

def sign(x):
    return 1 if x > 0 else -1

def distance(head, tail):
    dx = head[0] - tail[0]
    dy = head[1] - tail[1]
    return (dx, dy)

def move_head(head_pos, direction):
    match direction:
        case "R":
            head_pos[0] += 1
        case "L":
            head_pos[0] -= 1
        case "D":
            head_pos[1] += 1
        case "U":
            head_pos[1] -= 1

def move_knot(prev_pos, curr, visited_spaces):
    dx, dy = distance(prev_pos, curr.pos)
    if abs(dx) + abs(dy) > 2:   # diagonal move
        curr.pos[0] += 1 * sign(dx)
        curr.pos[1] += 1 * sign(dy)
    elif abs(dx) > 1:   # horizonal move
        curr.pos[0] += 1 * sign(dx)
    elif abs(dy) > 1:   # vertial move
        curr.pos[1] += 1 * sign(dy)
    else:
        pass # optimeize by breaking here
    if curr.nxt is None:
        visited_spaces.add(tuple(curr.pos))


sample_data = lib.read_input("input/sample/sample_09.txt")
sample_data_extra = lib.read_input("input/sample/sample_09_extra.txt")
full_data = lib.read_input("input/full/input_09.txt")

ropes = [Rope(2), Rope(10)]
for line in full_data:
    direction, moves = line.split(" ")
    moves = int(moves)

    while moves:
        for rope in ropes:
            move_head(rope.head.pos, direction)
            knot = rope.head.nxt
            while knot is not None:
                move_knot(knot.prv.pos, knot, rope.tail_locations)
                knot = knot.nxt
        moves -= 1

print(len(ropes[0].tail_locations), len(ropes[1].tail_locations))

