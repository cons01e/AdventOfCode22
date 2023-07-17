# Advent of Code 2022
# Day 9
# todo: optimize tail_locations data structure


import lib


def sign(x):
    return 1 if x > 0 else -1

class KnotNode:
    def __init__(self, prv, nxt, pos):
        self.prv = prv
        self.nxt = nxt
        self.pos = pos

    def distance(self, knot):
        dx = knot.pos[0] - self.pos[0]
        dy = knot.pos[1] - self.pos[1]
        return (dx, dy)

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

    def move_head(self, direction):
        match direction:
            case "R":
                self.head.pos[0] += 1
            case "L":
                self.head.pos[0] -= 1
            case "D":
                self.head.pos[1] += 1
            case "U":
                self.head.pos[1] -= 1
        self.move_knot(self.head, self.head.nxt)

    def move_knot(self, prev, curr):
        move_next = True
        dx, dy = curr.distance(prev)

        if abs(dx) + abs(dy) > 2:   # diagonally
            curr.pos[0] += 1 * sign(dx)
            curr.pos[1] += 1 * sign(dy)
        elif abs(dx) > 1:           # horizonally
            curr.pos[0] += 1 * sign(dx)
        elif abs(dy) > 1:           # vertially
            curr.pos[1] += 1 * sign(dy)
        else:
            move_next = False

        if curr.nxt is None:
            self.tail_locations.add(tuple(curr.pos))
            move_next = False

        if move_next:
            self.move_knot(curr, curr.nxt)


sample_data = lib.read_input("input/sample/sample_09.txt")
sample_data_extra = lib.read_input("input/sample/sample_09_extra.txt")
full_data = lib.read_input("input/full/input_09.txt")

ropes = [Rope(2), Rope(10)]
for line in full_data:
    direction, moves = line.split(" ")
    moves = int(moves)

    for _ in range(moves):
        for rope in ropes:
            rope.move_head(direction)

print(len(ropes[0].tail_locations), len(ropes[1].tail_locations))

