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

    return found_parts

window = []
missing_no = 0
for line in lines:
    number = int(line)
    if len(window) < 25:
        window.append(number)
        continue
    if not x_sum_in_list(25, number, window):
        missing_no = number
    window.append(number)
    window.pop(0)
#part 2
print(missing_no)

var_window=[]
for line in lines:
    number = int(line)
    if sum(var_window) == missing_no:
        print(max(var_window)+min(var_window))
        break
    if sum(var_window) < missing_no:
        var_window.append(number)
    while sum(var_window) > missing_no:
        var_window.pop(0)
        if sum(var_window) == missing_no:
            print(max(var_window)+min(var_window))
            break

