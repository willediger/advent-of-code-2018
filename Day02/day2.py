from functools import reduce
from collections import Counter

file_input = open('Day02/test_input', 'r')
file_array = file_input.read().splitlines()
file_input.close()

for i in range(0, len(file_array)):
    x = Counter(file_array[i])
    y = type(x)
    print(Counter(file_array[i]))
