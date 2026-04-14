from __future__ import annotations

import sys

def build_bracket_map(program: str) -> dict[int, int]:
    stack: list[int] = []
    bracket_map: dict[int, int] = {}

    for index, instruction in enumerate(program):
        if instruction == "[":
            stack.append(index)
        elif instruction == "]":
            if not stack:
                raise ValueError(f"Unexpected closing bracket at position {index}")
            opening_index = stack.pop()
            bracket_map[opening_index] = index
            bracket_map[index] = opening_index

    if stack:
        raise ValueError(f"Unclosed opening bracket at position {stack[-1]}")

    return bracket_map

def read_program(input_file: str) -> str:
    with open(input_file, "r", encoding="utf-8") as file:
        source = file.read()

    return "".join(char for char in source if char in "><+-.,[]")

def run_program(input_file: str) -> None:
    program = read_program(input_file)
    bracket_map = build_bracket_map(program)

    tape = [0]
    pointer = 0
    instruction_pointer = 0

    while instruction_pointer < len(program):
        instruction = program[instruction_pointer]

        if instruction == ">":
            pointer += 1
            if pointer == len(tape):
                tape.append(0)
        elif instruction == "<":
            pointer -= 1
            if pointer < 0:
                raise ValueError("Tape pointer moved left of cell 0")
        elif instruction == "+":
            tape[pointer] = (tape[pointer] + 1) % 256
        elif instruction == "-":
            tape[pointer] = (tape[pointer] - 1) % 256
        elif instruction == ".":
            sys.stdout.write(chr(tape[pointer]))
        elif instruction == ",":
            value = sys.stdin.buffer.read(1)
            tape[pointer] = value[0] if value else 0
        elif instruction == "[":
            if tape[pointer] == 0:
                instruction_pointer = bracket_map[instruction_pointer]
        elif instruction == "]":
            if tape[pointer] != 0:
                instruction_pointer = bracket_map[instruction_pointer]

        instruction_pointer += 1

    sys.stdout.flush()
    print(pointer)
    for start in range(0, len(tape), 64):
        print(f"Block {start//64} :", tape[start:start + 64])
