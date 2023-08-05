# Advent of Code 2022
# Day 10


import lib
from numpy import full


class Crt:
    def __init__(self, rows=6, row_pixels=40):
        self.rows = rows
        self.row_pixels = row_pixels
        self.display = full((self.rows, self.row_pixels), '0')
        self.sprite = range(3)

    def draw_pixel(self, cpu_cycle):
        row = cpu_cycle // self.row_pixels
        pixel = cpu_cycle % self.row_pixels
        display_char = '#' if pixel in self.sprite else '.'
        self.display[row, pixel] = display_char

    def update_sprite(self, x_val):
        self.sprite = range(x_val - 1, x_val + 2)

    def print_display(self):
        [print(''.join([p for p in row])) for row in self.display]

class Cpu:
    def __init__(self, cycle=0, x=1, crt=Crt()):
        self.cycle = cycle
        self.x = x
        self.checked_cycles = [20, 60, 100, 140, 180, 220]
        self.signals = []
        self.crt = crt

    def execute_noop(self):
        self.execute_cycle()

    def execute_addx(self, x_val):
        self.execute_cycle()
        self.execute_cycle()
        self.x += x_val
        self.crt.update_sprite(self.x)

    def execute_cycle(self):
        self.crt.draw_pixel(self.cycle)
        self.cycle += 1
        if self.cycle in self.checked_cycles:
            self.signals.append(self.cycle * self.x)


sample_input_data = lib.read_input("input/sample/sample_10.txt")
full_input_data = lib.read_input("input/full/input_10.txt")

cpu = Cpu()
for ins in full_input_data:
    if ins == "noop":
        cpu.execute_noop()
    else:
        x_val = int(ins.split(" ")[-1])
        cpu.execute_addx(x_val)

print(sum(cpu.signals))
cpu.crt.print_display()

