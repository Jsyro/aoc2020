import re, pprint

input_file = open('./day8_input.txt', 'r')
instructions = input_file.readlines()



def try_and_solve(instructions):
    max_index = 0
    current_index = 0
    accumulator = 0 
    instructions_ran = set()
    while current_index not in instructions_ran:
        max_index = max(current_index,max_index)
        instructions_ran.add(current_index)
        if current_index > 611:
            break
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
    return accumulator,max_index

print(try_and_solve(instructions))

#part 2
for x, ins in enumerate(instructions):
    instruction_array = ins.split(' ')
    cmd = instruction_array[0]
    arg = instruction_array[1]
    if cmd == 'acc':
        continue
    elif cmd == 'jmp':
        mod_instructions = instructions[:]
        mod_instructions[x] = 'nop ' + arg
    elif cmd == 'nop':
        mod_instructions = instructions[:]
        mod_instructions[x] = 'jmp ' + arg
    
    acc,max_ind = try_and_solve(mod_instructions)
    if max_ind > 611:
        print('modified instruction ' + str(x))
        print('accumulator value ' + str(acc))


