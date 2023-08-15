# Advent of Code 2022
# Day 11


import lib


class Monkey:
    op_map = {
        "+": lambda a,b: a + b,
        "*": lambda a,b: a * b
    }

    def __init__(self, data):
        self.id = data[0][-2]
        self.items = [int(el.replace(",", "")) for el in data[1].strip().split(" ")[2:]]
        self.operator, self.operand = data[2].split(" ")[-2:]
        self.divisor = int(data[3].split(" ")[-1])
        self.targets = [int(data[4][-1]), int(data[5][-1])]

    def process_items(self, monkeys):
        while self.items:
            new_val = self.perform_operation(self.items.pop(0))
            target = self.targets[not self.perform_div_test(new_val)]
            monkeys[target].items.append(new_val)

    def perform_operation(self, item):
        operand = item if self.operand == "old" else int(self.operand)
        return Monkey.op_map[self.operator](item, operand) // 3

    def perform_div_test(self, item):
        return item % self.divisor == 0

    def print(self):
        print(f"Monkey {self.id}\n"
              f"Items: {self.items}\n"
              f"operator: {self.operator} operand: {self.operand}\n"
              f"divisor: {self.divisor} targets: {self.targets}\n"
        )

class MonkeyManager:
    def __init__(self, input_data, rounds=20):
        self.monkeys = self.construct_monkeys(input_data)
        self.rounds = rounds
        self.monkey_activity = [0] * len(self.monkeys)

    # list comprehension
    def construct_monkeys(self, input_data):
        monkeys = []
        monkey_data = []
        for line in input_data:
            if line:
                monkey_data.append(line)
            else:
                monkeys.append(Monkey(monkey_data))
                
                monkey_data = []
        monkeys.append(Monkey(monkey_data)) # add final monkey
        return monkeys

    def execute_turn(self):
        for turn in range(self.rounds):
            for i, monkey in enumerate(self.monkeys):
                self.monkey_activity[i] += len(monkey.items)
                monkey.process_items(self.monkeys)

    def compute_monkey_business(self):
        sorted_activity = sorted(self.monkey_activity, reverse=True)
        return sorted_activity[0] * sorted_activity[1]


sample_input_data = lib.read_input("input/sample/sample_11.txt")
full_input_data = lib.read_input("input/full/input_11.txt")


monkey_manager = MonkeyManager(full_input_data)
monkey_manager.execute_turn()

print(f"monkey business {monkey_manager.compute_monkey_business()}")

