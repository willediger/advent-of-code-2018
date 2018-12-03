from functools import reduce
from collections import Counter
# import numpy

file_input = open('Day03/input', 'r')
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

def get_id(str):
    return str.split("#")[1].split(" ")[0]

def intersection(boundary1, boundary2):
    min_x_1 = boundary1[0][0]
    max_x_1 = boundary1[1][0]
    min_x_2 = boundary2[0][0]
    max_x_2 = boundary2[1][0]
    min_y_1 = boundary1[0][1]
    max_y_1 = boundary1[1][1]
    min_y_2 = boundary2[0][1]
    max_y_2 = boundary2[1][1]
    x_collision = min_x_1 <= min_x_2 <= max_x_1 or min_x_2 <= min_x_1 <= max_x_2
    y_collision = min_y_1 <= min_y_2 <= max_y_1 or min_y_2 <= min_y_1 <= max_y_2
    if x_collision and y_collision:
        min_common_x = max(min_x_1, min_x_2)
        max_common_x = min(max_x_2, max_x_1)
        min_common_y = max(min_y_1, min_y_2)
        max_common_y = min(max_y_2, max_y_1)
        return ((min_common_x, min_common_y), (max_common_x, max_common_y))
    else:
        return None

def intersected_pixels(single_intersection):
    intersected_pixels_running = set()
    for i in range(single_intersection[0][0], single_intersection[1][0] + 1):
        for j in range(single_intersection[0][1], single_intersection[1][1] + 1):
            intersected_pixels_running.add((i, j))
    return intersected_pixels_running

boundaries = list(map(lambda x: boundary(x), file_array))

intersections = []
intersections_count = [0] * file_array_len
for i in range(0, file_array_len):
    for j in range(i + 1, file_array_len):
        intersect = intersection(boundaries[i], boundaries[j])
        if intersect is not None:
            intersections.append(intersect)
            intersections_count[i] += 1
            intersections_count[j] += 1

intersected_pixels_list = list(map(lambda x: intersected_pixels(x), intersections))

intersected_pixels_set = set.union(*intersected_pixels_list)

intersected_pixels_count = len(intersected_pixels_set)

print(intersected_pixels_count)
# 115242

index_with_no_intersections = intersections_count.index(0)
id_of_no_intersections = get_id(file_array[index_with_no_intersections])

print(id_of_no_intersections)
# 1046

test_str = '#1 @ 1,3: 4x4'
expected_result = ((2, 4), (5, 7))
test_result = boundary(test_str)
assert test_result == expected_result