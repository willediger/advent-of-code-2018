from collections import Counter
import re

test = False
day = 7

input_path = 'Day' + format(day, '02d') + '/'
if test:
    input_path += 'test_'
input_path += 'input.txt'

file_input = open(input_path, 'r')
file_array = file_input.read().splitlines()
file_input.close()

dependencies = [[l[5:6], l[36:37]] for l in file_array]
#[1] depends on [0]

total = list(set([item for sublist in dependencies for item in sublist]))

def ready(finished_list, dependencies_list):
    ready_beginning = set([d[0] for d in dependencies_list if d[0] not in [d[1] for d in dependencies_list]])
    ready_after_finished = set([d[1] for d in dependencies_list if d[0] in finished_list])
    not_ready = set([d[1] for d in dependencies_list if d[0] not in finished_list])
    return sorted(list((ready_beginning | ready_after_finished) - set(finished_list) - not_ready))

finished = []

while len(finished) < len(total):
    ready_list = ready(finished, dependencies)
    finished.append(ready_list[0])

finished_str = ''.join(finished)

print('a', finished_str)