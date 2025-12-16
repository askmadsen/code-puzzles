def get_value(token: str, values) -> int:
    """Returns the value of the token."""
    if token.isdigit():
        return int(token)
    return values.get(token)

def process_instructions(tokens: list[str], instructions):
    """Processes a list of tokens into its instructions."""
    match tokens:
        case [a, "AND", b, "->", target]:
            instructions[target] = a + " AND " + b
        case [a, "OR", b, "->", target]:
            instructions[target] = a + " OR " + b
        case [a, "RSHIFT", b, "->", target]:
            instructions[target] = a + " RSHIFT " + b
        case [a, "LSHIFT", b, "->", target]:
            instructions[target] = a + " LSHIFT " + b
        case ["NOT", a, "->", target]:
            instructions[target] = "NOT " + a
        case [a, "->", target]:
            instructions[target] = a

def provide_signal(expr, wire, values):
    """Provides a signal to the wire if the components providing a signal to the wire has a signal."""
    match expr:
        case [a, "AND", b]:
            a = get_value(a, values)
            b = get_value(b, values)
            if a != None and b != None:
                values[wire] = a & b
        case [a, "OR", b]:
            a = get_value(a, values)
            b = get_value(b, values)
            if a != None and b != None:
                values[wire] = a | b
        case [a, "RSHIFT", b]:
            a = get_value(a, values)
            b = get_value(b, values)
            if a != None and b != None:
                values[wire] = a >> b
        case [a, "LSHIFT", b]:
            a = get_value(a, values)
            b = get_value(b, values)
            if a != None and b != None:
                values[wire] = a << b
        case ["NOT", a]:
            a = get_value(a, values)
            if a != None:
                values[wire] = ~a
        case [a]:
            a = get_value(a, values)
            if a is not None:
                values[wire] = a


def solve_part1_slow(input: str) -> int:
    pass

def solve_part1_fast(input: str) -> int:
    """Computes the signal of wire a."""
    instructions = {}
    values = {}
    lines = input.split("\n")
    for line in lines:
        tokens = line.split()
        process_instructions(tokens, instructions)
    while 'a' not in values:
        for wire, expr in instructions.items():
            if wire in values:
                continue
            else:
                provide_signal(expr.split(), wire, values)
    return values['a']

def solve_part2_slow(input: str) -> int:
    pass

def solve_part2_fast(input: str) -> int:
    """Computes the signal of wire a, after resetting all wires and providing wire b with the start value of wire a."""
    instructions = {}
    values = {}
    lines = input.split("\n")
    for line in lines:
        tokens = line.split()
        process_instructions(tokens, instructions)
    while 'a' not in values:
        for wire, expr in instructions.items():
            if wire in values:
                continue
            else:
                provide_signal(expr.split(), wire, values)
    value_a = values['a']
    values = {'b': value_a}
    while 'a' not in values:
        for wire, expr in instructions.items():
            if wire in values:
                continue
            else:
                provide_signal(expr.split(), wire, values)
    return values['a']