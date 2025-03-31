class Tape:
    def __init__(self, input_str: str):
        self.tape = list(input_str)
        self.head = 0

    def read(self):
        if self.head < 0:
            self.tape = ['•'] * (-self.head) + self.tape
            self.head = 0
        elif self.head >= len(self.tape):
            self.tape += ['•'] * (self.head - len(self.tape) + 1)
        return self.tape[self.head]

    def write(self, symbol):
        self.tape[self.head] = symbol

    def move(self, direction):
        if direction == 'g':
            self.head -= 1
        elif direction == 'd':
            self.head += 1

    def __str__(self):
        tape_str = ''.join(self.tape)
        pointer = ' ' * self.head + '^'
        return f'{tape_str}\n{pointer}'


class TuringMachine:
    def __init__(self, transitions, initial_state, final_state):
        self.transitions = transitions
        self.state = initial_state
        self.final_state = final_state

    def run(self, input_str):
        tape = Tape(input_str)
        steps = 0
        while self.state != self.final_state:
            current_symbol = tape.read()
            if self.state not in self.transitions or current_symbol not in self.transitions[self.state]:
                print("No transition rule found. Halting.")
                break
            write_symbol, direction, next_state = self.transitions[self.state][current_symbol]
            tape.write(write_symbol)
            tape.move(direction)
            self.state = next_state
            steps += 1
            print(f"Étape {steps} - État: {self.state}")
            print(tape)
        print("Machine arrêtée.")


transitions = {
    'init': {
        '1': ('1', 'd', 'init'),
        '0': ('0', 'd', 'init'),
        '•': ('1', 'g', 'end')  # ajoute un 1 à la fin
    }
}
tm = TuringMachine(transitions, initial_state='init', final_state='end')
tm.run("1011")

