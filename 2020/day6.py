import re, pprint

input_file = open('./day6_input.txt', 'r')
lines = input_file.readlines()


def group_ans(list_people_ans): 
    answers = set(''.join(list_people_ans))
    return len(answers)

group = []
ans_sum = 0
for line in lines:
    if line.strip() == '':
        ans_sum += group_ans(group)
        group = []        
    else:
        #another answer
        group += line.strip()

if group:
    ans_sum += group_ans(group)

print(ans_sum)