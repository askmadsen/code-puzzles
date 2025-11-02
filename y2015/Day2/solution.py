def wrapping_paper(dim: str) -> int:
    """
    Calculate the required wrapping paper for a single box.

    Args:
        dim (str): Dimensions of the box as 'LxWxH'.

    Returns:
        int: Total square feet of wrapping paper needed, including extra for the smallest side.
    """
    l, w, h = map(int, dim.split('x'))
    return 2*l*w + 2*l*h + 2*w*h + min(l*w, l*h, w*h) 

def ribbon(dim: str) -> int:
    """
    Calculates the required ribbon lenght for a single box.

    Args:
        dim (str): Dimensions of the box as 'LxWxH'.

    Returns:
        int: Total length of feet of ribbon needed, including extra for the bow.
    """
    l, w, h = map(int, dim.split('x'))
    return l * w * h + min((2*l + 2*w), (2*l + 2*h), (2*w + 2*h))


def solve_part1_slow(input: str) -> int:
    pass

def solve_part1_fast(input: str) -> int:
    """
    Calculates the total requrired amount of wrapping paper.

    Args:
        input (str): Lines of dimensions for different boxes as 'LxWxH'

    Returns:
        int: Total square feet of wrapping paper for all boxes. 
    """
    return sum(wrapping_paper(dim) for dim in input.splitlines())

def solve_part2_slow(input: str) -> int:
    pass

def solve_part2_fast(input: str) -> int:
    """
    Calculates the total requrired length of ribbon.

    Args:
        input (str): Lines of dimensions for different boxes as 'LxWxH'

    Returns:
        int: Total length in feet of ribbon for all boxes. 
    """
    return sum(ribbon(dim) for dim in input.splitlines())

        
        