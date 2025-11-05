def wrapping_paper(dim: str) -> int:
    """
    Calculates the required wrapping paper for a single box.
    """
    l, w, h = map(int, dim.split('x'))
    return 2*l*w + 2*l*h + 2*w*h + min(l*w, l*h, w*h) 

def ribbon(dim: str) -> int:
    """
    Calculates the required ribbon lenght for a single box.
    """
    l, w, h = map(int, dim.split('x'))
    return l * w * h + min((2*l + 2*w), (2*l + 2*h), (2*w + 2*h))


def solve_part1_slow(input: str) -> int:
    pass

def solve_part1_fast(input: str) -> int:
    """
    Calculates the total requrired amount of wrapping paper for all boxes in the input.
    """
    return sum(wrapping_paper(dim) for dim in input.splitlines())

def solve_part2_slow(input: str) -> int:
    pass

def solve_part2_fast(input: str) -> int:
    """
    Calculates the total required length of ribbon for all boxes in the input.
    """
    return sum(ribbon(dim) for dim in input.splitlines())

        
        