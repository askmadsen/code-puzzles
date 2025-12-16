import hashlib

def check_range(max_int, secret_key, prefix) -> int | None:
    """Computes the first integer which md5 hash with the secret key has prefix as prefix."""
    base_md5 = hashlib.md5(secret_key)
    for n in range(1, max_int + 1):
        m = base_md5.copy()
        m.update(str(n).encode('ascii'))
        if m.hexdigest().startswith(prefix):
            return n
    return None


def solve_part1_slow(input: str) -> int:
    """Computes the smallest integer up to max_int which md5 hash with the input results in a prefix of 00000."""
    max_int = 1000000
    prefix = "00000"
    secret_key = input.encode("utf-8")
    return check_range(max_int, secret_key, prefix)
    

def solve_part1_fast(input: str) -> int:
    pass

def solve_part2_slow(input: str) -> int:
    """Computes the smallest integer up to max_int which md5 hash with the input results in a prefix of 000000"""
    max_int = 2000000
    prefix = "000000"
    secret_key = input.encode("utf-8")
    return check_range(max_int, secret_key, prefix)

def solve_part2_fast(input: str) -> int:
    pass