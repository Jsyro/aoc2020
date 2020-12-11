import re, pprint
import itertools

input_file = open('./day9_input.txt', 'r')
lines = input_file.readlines()


def x_sum_in_list(x, num, num_list):
    found_parts = False
    assert len(num_list) == x
    for (a,b) in itertools.combinations(num_list, 2):
        if a + b == num:
            found_parts = True 
    # if found_parts
    # print('find ' + str(num) + " in " + str(num_list))
    return found_parts

window = []
for line in lines:
    number = int(line)
    if len(window) < 25:
        window.append(number)
        continue

    if not x_sum_in_list(25, number, window):
        print(number)

    window.append(number)
    window.pop(0)
#part 2

