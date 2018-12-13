import re
import time

from collections import deque, defaultdict

def play_game(max_players, last_marble):
    scores = defaultdict(int)
    circle = deque([0])

    for marble in range(1, last_marble + 1):
        if marble % 23 == 0:
            circle.rotate(7)
            scores[marble % max_players] += marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)

    return max(scores.values()) if scores else 0

start_time = time.time()

input = '452 players; last marble is worth 70784 points'
test_input = '9 players; last marble is worth 25 points: high score is 37305'

test = False

do_a = False
do_b = True

if test:
    input = test_input

input_ints = [int(e) for e in re.findall(r'\d+', input)]

player_count = input_ints[0]
last_marble = input_ints[1]


if do_a:
    high_score = play_game(player_count, last_marble)

    print('a', high_score)

if do_b:
    high_score = play_game(player_count, last_marble*100)

    print('b', high_score)

print("--- %s seconds ---" % (time.time() - start_time))

breakpoint()