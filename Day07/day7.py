from collections import Counter
import re

test = False
day = 7

do_a = False

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

def ready(finished_list, dependencies_list, working_list = []):
    ready_beginning = set([d[0] for d in dependencies_list if d[0] not in [d[1] for d in dependencies_list]])
    ready_after_finished = set([d[1] for d in dependencies_list if d[0] in finished_list])
    not_ready = set([d[1] for d in dependencies_list if d[0] not in finished_list])
    return sorted(list((ready_beginning | ready_after_finished) - set(finished_list) - not_ready - set(working_list)))

if do_a:
    finished = []

    while len(finished) < len(total):
        ready_list = ready(finished, dependencies)
        finished.append(ready_list[0])

    finished_str = ''.join(finished)

    print('a', finished_str)


if test:
    worker_count = 2
    addl_time = 0
else:
    worker_count = 5
    addl_time = 60

total_with_times = [[e, ord(e) - 64 + addl_time] for e in total]

finished = []
time = -1
workers = [[-1, None]] * worker_count
while len(finished) < len(total):
    finished.extend([e[1] for e in workers if e[0] <= time and e[1] is not None])
    for w in range(len(workers)):
        if workers[w][1] in finished:
            workers[w] = [time, None]
    working = [e[1] for e in workers if e[1] is not None or e[0] < time]
    ready_list = ready(finished, dependencies, working)

    for i in range(len(ready_list)):

        free_workers_count = len([e for e in workers if e[0] <= time])
        if free_workers_count > 0:
            next_ready_with_time = [e for e in total_with_times if e[0] == ready_list[i]][0]
            next_free_worker_idx = [(i, w) for i, w in enumerate(workers) if w[1] is None][0][0]
            workers[next_free_worker_idx] = [next_ready_with_time[1] + time, next_ready_with_time[0]]
        else:
            break


    time = min([e[0] for e in workers if e[1] is not None or e[0] < time])
    

breakpoint()

finish_time = max([w[0] for w in workers]) + 1

print('b', finish_time)