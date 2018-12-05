from collections import defaultdict
from collections import namedtuple
import re

file_input = open('Day04/input', 'r')
file_array = file_input.read().splitlines()
file_input.close()

file_array_len = len(file_array)

file_array.sort()

def new_guard(line):
    return 'Guard' in line

def falls_asleep(line):
    return 'falls' in line

def wakes_up(line):
    return 'wakes' in line
    
def get_hour(line):
    return int(line[12:14])

def get_minute(line):
    return int(line[15:17])

def get_guard(line):
    return int(line.split('#')[1].split(' ')[0])

guards = []

i = 0
while i < file_array_len:
    current_line_text = file_array[i]
    hour = get_hour(current_line_text)
    minute = get_minute(current_line_text)
    if new_guard(current_line_text):
        current_guard = get_guard(current_line_text)
        guard_list = [i[0] for i in guards]
        if current_guard not in guard_list:
            minutes = list()
            for minute in range(0, 60):
                minutes.append([minute, 0])
            guards.append([current_guard, minutes])
        guard_i = [i[0] for i in guards].index(current_guard)
    elif falls_asleep(current_line_text):
        if hour != 0:
            break
        else:
            sleep_start = minute
    elif wakes_up(current_line_text):
        sleep_end = minute - 1
        for m in range(sleep_start, sleep_end + 1):
            guards[guard_i][1][m][1] += 1
    i += 1

max_sum = 0
for g in range(0, len(guards)):
    minute_sum = 0
    for m in range(0, 60):
        minute_sum += guards[g][1][m][1]
    if minute_sum > max_sum:
        max_sum = minute_sum
        max_sum_guard = g
        max_sum_guard_id = guards[g][0]

max_min_amt = 0
for m in range(0, 60):
    if guards[max_sum_guard][1][m][1] > max_min_amt:
        max_min_amt = guards[max_sum_guard][1][m][1]
        max_min = m

print('a', max_sum_guard_id * max_min)

abs_max_min_amt = 0
for g in range(0, len(guards)):
    max_min_amt = 0
    for m in range(0, 60):
        if guards[g][1][m][1] > max_min_amt:
            max_min_amt = guards[g][1][m][1]
            max_min = m
    if max_min_amt > abs_max_min_amt:
        abs_max_min_amt = max_min_amt
        abs_max_min = max_min
        abx_max_guard_id = guards[g][0]

print('b', abx_max_guard_id * abs_max_min)