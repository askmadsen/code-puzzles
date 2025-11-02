def solve_part1_slow(input: str) -> int:
    """
    Calculate the final floor using a slow, explicit loop.

    Args:
        input (str): String of '(' and ')' characters representing floor changes.

    Returns:
        int: Final floor after following all instructions.
    """
    floor = 0
    for c in input:
        if c == '(':
            floor += 1
        elif c == ')':
            floor -= 1
    return floor

def solve_part1_fast(input: str) -> int:
    """
    Calculate the final floor using string count for faster computation.

    Args:
        input (str): String of '(' and ')' characters representing floor changes.

    Returns:
        int: Final floor after following all instructions.
    """
    return input.count('(') - input.count(')')


def solve_part2_slow(input: str) -> int:
    """
    Find the position of the first character that causes entry into the basement
    using a slow, explicit loop.

    Args:
        input (str): String of '(' and ')' characters representing floor changes.

    Returns:
        int: 1-based position of the first character that results in floor -1.
    """
    floor = 0
    pos = 0
    for c in input:
        if floor == -1:
            return pos
        elif c == '(':
            floor += 1
        elif c == ')':
            floor -= 1
        pos += 1

def solve_part2_fast(input: str) -> int:
    """
    Find the position of the first character that causes entry into the basement
    using an optimized loop with enumerate.

    Args:
        input (str): String of '(' and ')' characters representing floor changes.

    Returns:
        int: 1-based position of the first character that results in floor -1.
    """
    floor = 0
    for i, c in enumerate(input, 1):
        floor += 1 if c == '(' else -1
        if floor == -1:
            return i