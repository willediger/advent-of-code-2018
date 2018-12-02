from functools import reduce

day_1_input = open('input', 'r')
day_1_array = day_1_input.read().splitlines()
day_1_input.close()
ints = list(map(lambda x: int(x), day_1_array))
ints_sum = reduce((lambda x, y: x + y), ints)
print(ints_sum)