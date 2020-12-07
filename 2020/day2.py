input_file = open('./day2_input.txt', 'r')

lines = input_file.readlines()

valid_pw_count = 0 

for line in lines:
    #parsing
    policy = line.split(':')[0]
    password = line.split(':')[1]
   
    p_letter = policy.split(' ')[1]
    p_occ = policy.split(' ')[0]

    p_occ_min = int(p_occ.split('-')[0])
    p_occ_max = int(p_occ.split('-')[1])
    #policy
    letter_occurance = len([l for l in password if l == p_letter])

    if letter_occurance <= p_occ_max and letter_occurance >= p_occ_min:
        valid_pw_count += 1

print (valid_pw_count)


## part 2
print('PART 2')
valid_pw_count = 0 

for line in lines:
    #parsing
    policy = line.split(':')[0]
    password = line.split(':')[1]
   
    p_letter = policy.split(' ')[1]
    p_occ = policy.split(' ')[0]

    p_occ_1 = int(p_occ.split('-')[0])
    p_occ_2 = int(p_occ.split('-')[1])

    #policy
    if (password[p_occ_1] == p_letter) != (password[p_occ_2] == p_letter):
        valid_pw_count += 1

print (valid_pw_count)

