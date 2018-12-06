from collections import Counter
import re

file_input = open('Day06/input', 'r')
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

non_unique = -1
grid_height = len(grid)
grid_width = len(grid[0])
for x in range(0, grid_width):
    for y in range(0, grid_height):
        location_distances = [distance([x,y], loc) for loc in locations]
        min_distance = min(location_distances)
        if location_distances.count(min_distance) == 1:
            grid[y][x] = location_distances.index(min_distance)
        else:
            grid[y][x] = non_unique

#add all elements in first row to infinite elements set
infinite_elements = set([e for e in grid[0]])

#add all elements in last row to infinite elements set
infinite_elements.update([e for e in grid[len(grid)-1]])

#add all elements in far left or far right to infinite elements set
outside_elements = [[e[0], e[len(grid[0])-1]] for e in grid]
outside_elements = [item for sublist in outside_elements for item in sublist]
infinite_elements.update(outside_elements)


flat_grid = [item for sublist in grid for item in sublist]

area_counts = Counter(flat_grid)
area_counts_without_infinite = {x: area_counts[x] for x in area_counts if x not in infinite_elements}

max_area = max(area_counts_without_infinite.values())

print('a', max_area)