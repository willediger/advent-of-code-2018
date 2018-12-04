from collections import defaultdict
from collections import namedtuple
import re

file_input = open('Day04/test_input', 'r')
file_array = file_input.read().splitlines()
file_input.close()

file_array_len = len(file_array)

data = file_array
