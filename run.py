import tyro
import importlib
import time
from pathlib import Path
from typing import Optional, Literal
from dataclasses import dataclass



@dataclass 
class RunConfig:
    """
    Configuration for running the Advent of Code CLI.

    Attributes:
        year (int): Which Advent of Code year to run.  
        day (int): Which Advent of Code day to run.
        part (int): Which Advent of Code part to run. Default value is 1.
        method (str): Which method to run.
        input (Optional[str]): Path to input file or an input string.
    """
    year: int
    day: int
    part: int = 1
    method: Literal["fast", "slow", "both"] = "fast"
    input: Optional[str] = None


def main():
    """
    Runs an advent of code solution for a given year/day/part.
    """
    configs = tyro.cli(RunConfig)
    module_path = f"y{configs.year}.Day{configs.day}.solution"
    try:
        module = importlib.import_module(module_path)
    except ModuleNotFoundError:
        print(f"Module for Year {configs.year}, Day {configs.day} not found.")
        return

    # Load input
    input_str = ""
    if input is not None:
        input_path = Path(input)
        if input_path.is_file():  # It's a file path
            input_str = input_path.read_text()
        else:  # Treat it as a direct string input
            input_str = str(input)
        # Determine which methods to run
    methods_to_run = [configs.method] if configs.method != "both" else ["fast", "slow"]

    any_run = False
    for m in methods_to_run:
        fn_name = f"solve_part{configs.part}_{m}"
        fn = getattr(module, fn_name, None)

        if fn is None:
            print(f"{m.title()} solution for Part {configs.part} is not implemented.")
            continue

        any_run = True
        start = time.time()
        try:
            result = fn(input_str)
        except Exception as e:
            print(f"Error running {fn_name}: {e}")
            continue
        end = time.time()
        duration = end - start

        # Formats duration as ms or s depending on duration time
        time_str = f"{duration*1000:.3f} ms" if duration < 1 else f"{duration:.3f} s"
        print(f"[{m.upper()}] Part {configs.part} → Output: {result} | Time: {time_str}")

    if not any_run:
        print("No implemented solutions found for the given configuration.")


if __name__ == "__main__":
    main()