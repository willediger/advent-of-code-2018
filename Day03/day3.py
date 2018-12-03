from functools import reduce
from collections import Counter
# import numpy

file_input = open('Day03/test_input', 'r')
file_array = file_input.read().splitlines()
file_input.close()

file_array_len = len(file_array)

def boundary(str):
    without_at_sign = str.split("@")[1]
    split_on_top_x = without_at_sign.split(',')
    top_left_x = int(split_on_top_x[0]) + 1
    split_on_top_y = split_on_top_x[1].split(':')
    top_left_y = int(split_on_top_y[0]) + 1
    split_on_width = split_on_top_y[1].split('x')
    bottom_right_x = top_left_x + int(split_on_width[0]) - 1
    bottom_right_y = top_left_y + int(split_on_width[1]) - 1
    return ((top_left_x, top_left_y), (bottom_right_x, bottom_right_y))

test_str = '#1 @ 1,3: 4x4'
expected_result = ((2, 4), (5, 7))
test_result = boundary(test_str)
assert test_result == expected_result