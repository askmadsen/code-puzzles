import re
import numpy as np

REGEX = re.compile(r"(toggle|turn on|turn off) (\d+),(\d+) through (\d+),(\d+)")

def parse_line(line: str) -> tuple[str, int, int, int, int]:
    """Parses a line using a regular expression."""
    cmd, x1, y1, x2, y2 = re.match(REGEX, line).groups()
    x1, y1, x2, y2 = map(int, (x1, y1, x2, y2))
    return cmd, x1, y1, x2, y2

def solve_part1_slow(input: str) -> int:
    pass

def solve_part1_fast(input: str) -> int:
    """Counts the number of lights that are turned on after all instructions."""
    grid = np.zeros((1000, 1000), dtype = int)
    lines = input.split("\n")
    for line in lines:
        cmd, x1, y1, x2, y2 = parse_line(line)
        if cmd == "turn on":
            grid[y1:y2+1, x1:x2+1] = 1
        elif cmd == "turn off":
            grid[y1:y2+1, x1:x2+1] = 0
        else: # cmd = toggle
            grid[y1:y2+1, x1:x2+1] ^= 1
    return grid.sum()


def solve_part2_slow(input: str) -> int:
    pass

def solve_part2_fast(input: str) -> int:
    """Computes the total brightness of the lights after all instructions."""
    grid = np.zeros((1000, 1000), dtype = int)
    lines = input.split("\n")
    for line in lines:
        cmd, x1, y1, x2, y2 = parse_line(line)
        if cmd == "turn on":
            grid[y1:y2+1, x1:x2+1] += 1
        elif cmd == "turn off":
            grid[y1:y2+1, x1:x2+1] = np.clip(
                grid[y1:y2+1, x1:x2+1] - 1,
                0,
                None
            )
        else: # cmd = toggle
            grid[y1:y2+1, x1:x2+1] += 2
    return grid.sum()