from collections import defaultdict
from collections import namedtuple
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



breakpoint()