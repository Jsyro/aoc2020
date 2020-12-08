import re, pprint

input_file = open('./day5_input.txt', 'r')
lines = input_file.readlines()

max_seat_id = 0

for line in lines:
    b_str = line.strip() 
    b_str = b_str.replace('B','1')
    b_str = b_str.replace('F','0')
    b_str = b_str.replace('R','1')
    b_str = b_str.replace('L','0')

    row = int(b_str[:7],2)
    col = int(b_str[7:],2)

    seat_id =(row*8)+col
    
    max_seat_id = max([seat_id,max_seat_id])

print(max_seat_id)