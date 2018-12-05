from collections import defaultdict
from collections import namedtuple
import re

file_input = open('Day05/input', 'r')
file_array = file_input.read().splitlines()
file_str = file_array[0]
orig_file_str = file_str
file_input.close()

i = 0
while i < len(file_str) - 1:
    char_pair = file_str[i:i+2]
    if char_pair[0].upper() == char_pair[1].upper() and char_pair[0] != char_pair[1]:
        file_str = file_str[:i] + file_str[i+2:]
        if i > 0:
            i -= 1
    else:
        i += 1

print('a', len(file_str))

min_length = 9999999999999999999
for letter in range(97, 123):
    l = chr(letter)
    removed_letter_str = orig_file_str.replace(chr(letter), '').replace(chr(letter).upper(), '')
    i = 0
    while i < len(removed_letter_str) - 1:
        char_pair = removed_letter_str[i:i+2]
        if char_pair[0].upper() == char_pair[1].upper() and char_pair[0] != char_pair[1]:
            removed_letter_str = removed_letter_str[:i] + removed_letter_str[i+2:]
            if i > 0:
                i -= 1
        else:
            i += 1
    new_len = len(removed_letter_str)
    if new_len < min_length:
        min_length = new_len

print('b', min_length)