input_file = open('./day3_input.txt', 'r')

lines = input_file.readlines()

line_length = len(lines[0])-1
tree_count = 0

for n, line in enumerate(lines):
    x = n*3
    if line[x%line_length] == '#':
        tree_count += 1

print (tree_count)
## part 2
print('PART 2')
results = []

for right_offset in (1,3,5,7):
    tree_count = 0 
    for n, line in enumerate(lines):
        x = n*right_offset
        if line[x%line_length] == '#':
            tree_count += 1
    print (tree_count)
    results.append(tree_count)

tree_count = 0 
for n, line in enumerate(lines):
    if n % 2 == 0:
        continue
    x = n*1
    if line[x%line_length] == '#':
        tree_count += 1

print (tree_count)
results.append(tree_count)

res = 1
for r in results:
    res *= r

print (res)