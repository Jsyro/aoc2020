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
# pprint.pp(contents)


all_parents = set()
def find_parent_tree(init_bag, contents, depth):
    print('starting bag')
    print(init_bag)
    one_level_up_parents = set()
    for k,v in contents.items():
        if init_bag in v.keys():
            print('found_parent')
            one_level_up_parents.add(k)
            all_parents.add(k)
    if one_level_up_parents:
        print('take another lap')
        for p in one_level_up_parents:
            print(p)
            print('find all parents of')
            find_parent_tree(p,contents,depth+1)
    else:
        print('all done')
    return

find_parent_tree('shiny gold',contents,1)
print(all_parents)
print(len(all_parents))

# def find_all_parents(set_of_bags, contents):
#     print(set_of_bags)
#     init_size = len(set_of_bags)
#     for k,v in contents.items(): 
#         if any(i in set_of_bags for i in set(v.keys())):
#             set_of_bags.add(k)
#     new_size = len(set_of_bags)
#     if init_size != new_size:
#         set_of_bags = find_all_parents(set_of_bags, contents)
#     return set_of_bags

# bags = set(['shiny gold'])
# bags = find_all_parents(bags,contents)

# print(len(bags))