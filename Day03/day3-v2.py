from collections import defaultdict
from collections import namedtuple
import re

file_input = open('Day03/input', 'r')
file_array = file_input.read().splitlines()
file_input.close()

file_array_len = len(file_array)

data = file_array

Claim = namedtuple('Claim', ['claim_number', 'start_x', 'start_y', 'width', 'height'])
claims = [re.findall(r'-?\d+', line) for line in file_array]
claims = [Claim(*line_list) for line_list in claims]

claims = map(lambda s: map(int, re.findall(r'-?\d+', s)), data)

m = defaultdict(list)
overlaps = {}
for (claim_number, start_x, start_y, width, height) in claims:
  overlaps[claim_number] = set()
  for i in range(start_x, start_x + width):
    for j in range(start_y, start_y + height):
      if m[(i,j)]:
        for number in m[(i, j)]:
          overlaps[number].add(claim_number)
          overlaps[claim_number].add(number)
      m[(i,j)].append(claim_number)

print("a", len([k for k in m if len(m[k]) > 1]))
print("b", [k for k in overlaps if len(overlaps[k]) == 0][0])


print('asdf')