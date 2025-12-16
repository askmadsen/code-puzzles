def process_line_slow(s: str) -> int:
    s = s[1:-1]
    i = 0
    memory_chars = 0
    n = len(s)

    while i < n:
        if s[i] == "\\":
            next_char = s[i+1]
            if next_char in ["\\", '"']:
                memory_chars += 1
                i += 2
            elif next_char == "x":
                memory_chars += 1
                i += 4
        else:
            memory_chars += 1
            i += 1

    return len(s) + 2 - memory_chars

def process_line_fast(s: str) -> int:
    code_len = len(s)
    in_memory = len(bytes(s[1:-1], "utf-8").decode("unicode_escape"))
    return code_len - in_memory


def solve_part1_slow(input: str) -> int:
    lines = input.splitlines()
    return sum(map(process_line_slow, lines))

def solve_part1_fast(input: str) -> int:
    lines = input.splitlines()
    return sum(map(process_line_fast, lines))

def solve_part2_slow(input: str) -> int:
    return 0

def solve_part2_fast(input: str) -> int:
    return 0
        
        