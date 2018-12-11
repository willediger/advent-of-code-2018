from collections import Counter
import re

test = False
day = 8

do_a = False

input_path = 'Day' + format(day, '02d') + '/'
if test:
    input_path += 'test_'
input_path += 'input.txt'

file_input = open(input_path, 'r')
file_array = file_input.read().splitlines()
file_input.close()

license_strs = file_array[0].split()
license_numbers = [int(e) for e in license_strs]

def meta_total(nums):
    children_count = nums[0]
    meta_count = nums[1]

    remaining_nums = nums[2:]

    children_total = 0
    for c in range(children_count):
        child = meta_total(remaining_nums)
        remaining_nums = child[1]
        children_total += child[0]
    
    meta = remaining_nums[:meta_count]
    remaining_nums = remaining_nums[meta_count:]
    
    return [children_total + sum(meta), remaining_nums]

result = meta_total(license_numbers)

total_meta = result[0]

print('a', total_meta)

breakpoint()