def solve_part1_slow(input: str) -> int:
    """Calculate the final floor using a slow loop."""
    floor = 0
    for c in input:
        floor = floor + 1 if c == '(' else floor - 1 
    return floor

def solve_part1_fast(input: str) -> int:
    """Calculate the final floor using string count for faster computation."""
    return input.count('(') - input.count(')')


def solve_part2_slow(input: str) -> int:
    """
    Find the position of the first character that causes entry into the basement
    using a slow, explicit loop.
    """
    floor = 0
    pos = 0
    for c in input:
        if floor == -1:
            return pos
        floor = floor + 1 if c == '(' else floor - 1 
        pos += 1

def solve_part2_fast(input: str) -> int:
    """
    Find the position of the first character that causes entry into the basement
    using an optimized loop with enumerate.
    """
    floor = 0
    for i, c in enumerate(input, 1):
        floor += 1 if c == '(' else -1
        if floor == -1:
            return i