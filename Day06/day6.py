from collections import Counter
import re

file_input = open('Day06/test_input', 'r')
file_array = file_input.read().splitlines()
file_input.close()

locations = [[int(i) for i in re.findall(r'\d+', line)] for line in file_array]

min_loc = [min([loc[0] for loc in locations]), min([loc[1] for loc in locations])]
max_loc = [max([loc[0] for loc in locations]), max([loc[1] for loc in locations])]

grid = []
for y in range(0, max_loc[1] + 1):
    grid.append([0]*(max_loc[0]+1))

def distance(loc1, loc2):
    return abs(loc2[0] - loc1[0]) + abs(loc2[1] - loc1[1])


for x in range(0, len(grid[0])):
    for y in range(0, len(grid)):
        location_distances = [distance([x,y], loc) for loc in locations]
        min_distance = min(location_distances)
        if location_distances.count(min_distance) == 1:
            grid[y][x] = location_distances.index(min_distance)
        else:
            grid[y][x] = -1


breakpoint()