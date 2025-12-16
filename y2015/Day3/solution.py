# Coordinate offset for each of the 4 possible moves
MOVES = {
    "^": (0,1),
    ">": (1,0),
    "v": (0,-1),
    "<": (-1,0)
}

def solve_part1_slow(input: str) -> int:
    pass

def solve_part1_fast(input: str) -> int:
    """Computes the number of houses that recieves at least 1 present from Santa."""
    x = y = 0
    visited = {(0,0)}
    for c in input:
        dx, dy = MOVES[c]
        x += dx
        y += dy
        visited.add((x,y))
    return len(visited)

def solve_part2_slow(input: str) -> int:
    pass

def solve_part2_fast(input: str) -> int:
    """Computes the number of houses that recieves at least 1 present from either Santa or Robo-Santa."""
    visited = {(0,0)}
    coords = {
        0: (0,0),
        1: (0,0)
    }
    turn = 0
    for c in input:
        x, y = coords[turn]
        dx, dy = MOVES[c]
        coords[turn] = (x + dx, y + dy)
        visited.add(coords[turn])
        turn = 1 - turn
    return len(visited)