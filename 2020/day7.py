import re, pprint

input_file = open('./day7_input.txt', 'r')
lines = input_file.readlines()

contents = {}

for line in lines:
    line = line.strip('.\n') 
    line = line.replace('bags','')
    line = line.replace('bag','')
    line = line.replace('  ',' ')
    parent_children = line.split(' contain ')
    parent = parent_children[0]
    children_arr = parent_children[1].split(',')
    if children_arr == ['no other ']:
        continue
    children = {' '.join(x.strip().split(' ')[1:]): int(x.strip().split(' ')[0]) for x in children_arr}
    contents[parent] = children
pprint.pp(contents)


def find_all_parents(set_of_bags, contents):
    init_size = len(set_of_bags)
    for k,v in contents.items(): 
        if not set_of_bags & set(v.keys()):
            continue 
        set_of_bags.add(k)
    new_size = len(set_of_bags)
    if init_size != new_size:
        set_of_bags = find_all_parents(set_of_bags, contents)
    return set_of_bags

bags = set(['shiny gold'])
bags = find_all_parents(bags,contents)

print(len(bags))