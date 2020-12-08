import re, pprint

input_file = open('./day6_input.txt', 'r')
lines = input_file.readlines()


def group_ans(list_people_ans): 
    answers = set(''.join(list_people_ans))
    return len(answers)



def group_ans_all(list_people_ans): 
    sets = []
    for l in list_people_ans:
        s = set(l)
        sets.append(s)
    
    all_set = list(sets)[0]
    for s in sets: 
        all_set = all_set & s

    print(all_set)
    print(list_people_ans)

    return len(all_set)


group = []
all_ans_sum = 0
ans_sum = 0

for line in lines:
    if line.strip() == '':
        ans_sum += group_ans(group)
        all_ans_sum += group_ans_all(group)
        group = []        
    else:
        #another answer
        group.append(line.strip())

if group:
    ans_sum += group_ans(group)
    all_ans_sum += group_ans_all(group)

print(ans_sum)
print(all_ans_sum)