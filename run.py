import tyro
import importlib
import time
from pathlib import Path
from typing import Optional


def main(
    year: int,
    day: str,
    part: int = 1,
    method: str = "fast",  # "fast", "slow", or "both"
    input: Optional[str] = None,  # path to input file
):
    """
    Run a solution for a given year/day/part.
    """
    module_path = f"y{year}.{day}.solution"
    try:
        module = importlib.import_module(module_path)
    except ModuleNotFoundError:
        print(f"❌ Module for Year {year}, Day {day} not found.")
        return

    # Load input
    input_str = ""
    if input:
        input_path = Path(input)
        if input_path.is_file():
            input_str = input_path.read_text()
        else:
            print(f"⚠️ Input file '{input}' not found. Running with empty input.")

    # Determine which methods to run
    methods_to_run = [method] if method != "both" else ["fast", "slow"]

    any_run = False
    for m in methods_to_run:
        fn_name = f"solve_part{part}_{m}"
        fn = getattr(module, fn_name, None)

        if fn is None:
            print(f"🚫 {m.title()} solution for Part {part} is not implemented.")
            continue

        any_run = True
        start = time.time()
        try:
            result = fn(input_str)
        except Exception as e:
            print(f"❌ Error running {fn_name}: {e}")
            continue
        end = time.time()
        duration = end - start

        # Format duration nicely (ms if small, s if large)
        time_str = f"{duration*1000:.3f} ms" if duration < 1 else f"{duration:.3f} s"
        print(f"[{m.upper()}] Part {part} → Output: {result} | Time: {time_str}")

    if not any_run:
        print("⚠️ No implemented solutions found for the given configuration.")


if __name__ == "__main__":
    tyro.cli(main)
