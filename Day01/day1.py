from functools import reduce

day_1_input = open('Day01/input', 'r')
day_1_array = day_1_input.read().splitlines()
day_1_input.close()
ints = list(map(lambda x: int(x), day_1_array))

day1_pt1 = reduce((lambda x, y: x + y), ints)
print(day1_pt1)

frequency_seen_already = False
current_frequency = 0
frequencies = [current_frequency]
while not frequency_seen_already:
    for i in range(0, len(ints)):
        current_frequency += ints[i]
        if current_frequency in frequencies:
            frequency_seen_already = True
            break
        else:
            frequencies.append(current_frequency)


day1_pt2 = current_frequency
print(day1_pt2)