from collections import deque
import shutil
import random 
from time import sleep

TERMNAL_WIDTH, TERMINAL_HEIGHT = shutil.get_terminal_size()
RAIN_DENSITY = 0.05
EMPTY_LINE =  " " * TERMNAL_WIDTH

lines = deque([EMPTY_LINE for _ in range(TERMINAL_HEIGHT)], maxlen=TERMINAL_HEIGHT)

def nex_line(source):
    row = ["|" if char == "v" else " " for char in source]
    for idx, _ in enumerate(row):
        if random.random() < RAIN_DENSITY:
            row[idx] = "v"

    return "".join(row)

while True:
    row = nex_line(lines[0])
    lines.appendleft(row)
    for line in lines:
        print(line)
    sleep(0.05)
