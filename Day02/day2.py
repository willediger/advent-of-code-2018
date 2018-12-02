from functools import reduce
from collections import Counter

file_input = open('Day02/input', 'r')
file_array = file_input.read().splitlines()
file_input.close()

count_of_twos = 0
count_of_threes = 0
for i in range(0, len(file_array)):
    letter_frequencies = list(Counter(file_array[i]).values())
    if 2 in letter_frequencies:
        count_of_twos += 1
    if 3 in letter_frequencies:
        count_of_threes += 1

pt1answer = count_of_twos * count_of_threes
print(pt1answer)