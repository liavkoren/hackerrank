'''
Simple Text Editor
https://www.hackerrank.com/challenges/simple-text-editor

In this challenge, you must implement a simple text editor. Initially, your
editor contains an empty string, S. You must perform Q operations of the
following types:

1    append(W) - Append string W to the end of S.
2    delete(k) - Delete the last k characters of S.
3    print(k) - Print the kth character of .
4    undo - Undo the last (not previously undone) operation of type or 1 or 2,
reverting S to the state it was in prior to that operation.

# Sample Input
8
1 abc   [add]
3 3     [print]
2 3     [del 3]
1 xy    [add]
3 2     [print]
4       [undo]
4       [undo]
3 1     [print]

# Sample Output
c
y
a

---

class Instruction(object):
    def __init__(self, type, word=None, k=None):

class Solver(object):
    def __init__(self, raw_input):
        self.instructions = [build_instruction(line) for line in raw_input]
        self.buffer = ''
        self.undo = []
        self.solve()

    def do_instruction(self, inst):
        if inst.type == append:
            buffer += append to buffer,
            undo_stack.append(inst)
        elif ins.type == delete:
            inst.word = buffer[-inst.k:]
            buffer = buffer[0:-inst.k]
            undo_stack.append(ins)
        elif ins.type == print:
            print

    def solve(self):
        for inst in instructions:
            if inst.type == undo:
                inst_to_invert = undo_stack.pop()
                if inst_to_invert.type == append:
                    inst = new delete instruction
                elif inst_to_invert.type == delete:
                    inst = new append instruction
            do_instruction(inst)
'''
import fileinput


class Instruction(object):
    APPEND = '1'
    DELETE = '2'
    PRINT = '3'
    UNDO = '4'

    def __init__(self, type, arg=None):
        self.type = type
        if arg:
            try:
                arg = int(arg)
            except ValueError:
                pass
        self.arg = arg
        self.word = None

    def __repr__(self):
        return u'Instruction({self.type}, arg={self.arg})'.format(self=self)

    @staticmethod
    def build(line):
        try:
            instruction_type, arg = line.split(' ')
            return Instruction(instruction_type, arg=arg)
        except ValueError:
            return Instruction('4')


class Solver(object):
    def __init__(self, input):
        self.instructions = [Instruction.build(line.strip()) for line in input]
        self.buffer = ''
        self.undo = []

    def do_instruction(self, inst):
        if inst.type == Instruction.APPEND:
            self.buffer += inst.arg

        elif inst.type == Instruction.DELETE:
            self.buffer = self.buffer[0:-inst.arg]

        elif inst.type == Instruction.PRINT:
            print self.buffer[inst.arg - 1]

    def invert(self, instruction):
        if instruction.type == Instruction.APPEND:
            return Instruction(Instruction.DELETE, arg=len(instruction.arg))
        elif instruction.type == Instruction.DELETE:
            return Instruction(Instruction.APPEND, arg=instruction.word)

    def go(self):
        for inst in self.instructions:
            if inst.type == Instruction.UNDO:
                instruction = self.undo.pop()
                inst = self.invert(instruction)

            elif inst.type == Instruction.DELETE:
                inst.word = self.buffer[-inst.arg:]
                self.undo.append(inst)

            elif inst.type == Instruction.APPEND:
                self.undo.append(inst)

            self.do_instruction(inst)

input = [line for line in fileinput.input()]

solver = Solver(input[1:])
solver.go()

test1 = '''1 abc
3 3
2 3
1 xy
3 2
4
4
3 1'''
