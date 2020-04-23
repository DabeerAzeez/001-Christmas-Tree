import threading
import random
import os
import time

print_lock = threading.Lock()

tree = list(open('ChristmasTree.txt').read().rstrip())

# Read the entire file, strip trailing spaces off the right side, convert to list because
# strings are immutable in python, so using lists containing each character is an alternate
# route that allows modifications; we can render it as a string at the end using .join

yellow = []             # Initialize empty coordinate lists for the colours
red = []
blue = []
green = []

def lights(color, indexes):
    off = True
    while True:
        with print_lock:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(''.join(tree))

        for index in indexes:
            tree[index] = colours(color) if off else '●'

        off = not off

        time.sleep(random.uniform(0.5, 1.5))

def colours(color):
    if color == 'red':
        return f'\033[91m●\033[0m'
    if color == 'green':
        return f'\033[92m●\033[0m'
    if color == 'yellow':
        return f'\033[93m●\033[0m'
    if color == 'blue':
        return f'\033[94m●\033[0m'

for i, c in enumerate(tree):        # Using enumerate to find those coordinates
    if c == 'Y':
        yellow.append(i)
        tree[i] = '●'                # Replace each colour in the list with a blank dot which we will
    if c == 'R':                     # colour later
        red.append(i)
        tree[i] = '●'
    if c == 'G':
        green.append(i)
        tree[i] = '●'
    if c == 'B':
        blue.append(i)
        tree[i] = '●'

#Initialize four threads for the four colours

ty = threading.Thread(target=lights, args=('yellow', yellow), daemon=True)
tr = threading.Thread(target=lights, args=('red', red), daemon=True)
tg = threading.Thread(target=lights, args=('green', green), daemon=True)
tb = threading.Thread(target=lights, args=('blue', blue), daemon=True)

for thread in [ty, tr, tg, tb]:
    thread.start()

for thread in [ty, tr, tg, tb]:
    thread.join()
