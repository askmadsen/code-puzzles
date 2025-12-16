def is_nice_part1(s: str) -> int:
    """Returns 1 if the string is nice and 0 otherwise according to the rules of part 1."""
    vowels = 0
    double_char = False
    i = 0
    n = len(s)

    vowels_set = {'a', 'e', 'i', 'o', 'u'}
    forbidden_pairs = {"ab", "cd", "pq", "xy"}

    while i < n:
        c = s[i]
        if c in vowels_set:
            vowels += 1
        if i + 1 < n:
            pair = c + s[i + 1]
            if pair in forbidden_pairs:
                return 0    # string naughty
            if not double_char and c == s[i+1]:
                double_char = True
        i += 1
    return int(vowels >= 3 and double_char)

def is_nice_part2(s: str) -> int:
    """Returns 1 if the string is nice and 0 otherwise according to the rules of part 2."""
    pairs = set()
    repeats = False
    has_pair = False
    i = 0
    n = len(s) 

    while i < n:
        c = s[i]
        if not has_pair and i + 1 < n:
            pair = c + s[i+1]
            if not pair in pairs:
                pairs.add(pair)
            else:
                has_pair = True
        if i + 2 < n:
            if c == s[i+2]:
                repeats = True
                if c == s[i+1]: # 3 repeat letters, skip one
                    i += 1
        i += 1
    return int(repeats and has_pair)
            

def solve_part1_slow(input: str) -> int:
    """Counts the number of nice strings in the input."""
    strings = input.splitlines()
    return sum(map(is_nice_part1, strings))

def solve_part1_fast(input: str) -> int:
    pass

def solve_part2_slow(input: str) -> int:
    """Counts the number of nice strings in the input."""
    strings = input.splitlines()
    return sum(map(is_nice_part2, strings))

def solve_part2_fast(input: str) -> int:
    pass
        
        