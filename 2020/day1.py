
input_file = open('./day1_input.txt', 'r')

num_array = []
for line in input_file.readlines():
    num_array.append(int(line.strip()))

key_num1, key_num2 = 0,0

#n^2
for x in num_array:
    for y in num_array:
        if x+y == 2020:
            key_num1 = x  
            key_num2 = y

print (key_num1)
print (key_num2)
print (key_num1+key_num2)
print (key_num1*key_num2)

## part 2
#n^3
for x in num_array:
    for y in num_array:
        for z in num_array:
            if x+y+z == 2020:
                key_num1 = x  
                key_num2 = y
                key_num3 = z

print (key_num1+key_num2+key_num3)
print (key_num1*key_num2*key_num3)