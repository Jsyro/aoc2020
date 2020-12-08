import re, pprint

input_file = open('./day8_input.txt', 'r')
instructions = input_file.readlines()

instructions_ran = set()
current_index = 0
accumulator = 0 

while current_index not in instructions_ran:
    instructions_ran.add(current_index)
    curr_instruction = instructions[current_index]
    instruction_array = curr_instruction.split(' ')
    cmd = instruction_array[0]
    arg = instruction_array[1]

    if cmd == 'acc':
        accumulator += int(arg)
        current_index += 1
    elif cmd == 'jmp':
        current_index += int(arg)
    elif cmd == 'nop':
        current_index += 1

print(accumulator)
