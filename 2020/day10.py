import re, pprint
import itertools

input_file = open('./day10_input.txt', 'r')
lines = input_file.readlines()

jolt_ratings = [0]
for line in lines: 
    jolt_ratings.append(int(line))
jolt_ratings.sort()
jolt_ratings.append(jolt_ratings[-1]+3)
distribution = [0,0,0]
last_rating = 0
for adapter_rating in jolt_ratings:
    distribution[adapter_rating-last_rating-1] += 1
    last_rating = adapter_rating
print(distribution)


cache_dict = {}

#part 2
def num_of_ways_to_target(adapter_index, target_joltage):
    if (adapter_index,target_joltage) in cache_dict:
        return cache_dict[adapter_index,target_joltage]
    if adapter_index == 0:
        if 0 <= target_joltage <= 3: 
            cache_dict[adapter_index,target_joltage] = 1 
            return 1
        else:
            cache_dict[adapter_index,target_joltage] = 0 
            return 0 
    diff = target_joltage - jolt_ratings[adapter_index]
    if diff > 3:
        cache_dict[adapter_index,target_joltage] = 0
        return 0
    #use it
    partition_1 = num_of_ways_to_target(adapter_index-1, target_joltage-diff)  
    #don't use it
    partition_2 = num_of_ways_to_target(adapter_index-1, target_joltage)

    cache_dict[adapter_index,target_joltage] = partition_1+partition_2
    return partition_1 + partition_2

print(jolt_ratings)
print(num_of_ways_to_target(len(jolt_ratings)-2,jolt_ratings[-1]))