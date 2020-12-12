import re, pprint
import itertools
import copy
input_file = open('./day11_input.txt', 'r')
lines = input_file.readlines()
seat_map = []

for l in lines: 
    seat_map.append(list(l.strip()))

def count_neighbours(array,row, col):
    count = 0

    for x in range(row-1,row+2):
        for y in range(col-1,col+2):
            try:
                if  x >= 0 and y >= 0 and array[x][y] == '#':
                    count+=1
            except IndexError:
                pass

    if array[row][col] == '#':
        count -= 1
    return count


def execute_round(in_map):
    new_map = copy.deepcopy(in_map)
    change = False
    seats_emptied=0
    seats_filled=0
    for row_num, row in enumerate(in_map):
        for col_num, item in enumerate(row):
            if item== ".":
                continue
            num_neighbours = count_neighbours(in_map,row_num,col_num)
            if num_neighbours >= 4 and item=="#":
                new_map[row_num][col_num] = "L"
                seats_emptied += 1
                change=True
            elif num_neighbours == 0 and item=="L":
                new_map[row_num][col_num] = "#"
                change=True
                seats_filled += 1
            else:
                pass
    print(seats_emptied)
    print(seats_filled)
    return new_map,change

any_change = True
round_count = 0 
while any_change:
    seat_map,any_change = execute_round(seat_map)
    round_count += 1
    
    print(round_count)
    print()

filled_seats = 0
for r in seat_map:
    print(''.join(r))
    for c in r:
        if c == "#":
            filled_seats+=1
print(filled_seats)
