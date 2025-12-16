from dataclasses import dataclass
from typing import Literal, Optional
import tyro
from pathlib import Path


# Templates
TEMPLATE_DIR = Path("aoc_templates")
SOLUTION_TEMPLATE_FILE = TEMPLATE_DIR / "solutions_template.py"
README_TEMPLATE_FILE = TEMPLATE_DIR / "readme_template.md"
INIT_TEMPLATE_FILE = TEMPLATE_DIR / "__init__.py"

SOLUTION_TEMPLATE = SOLUTION_TEMPLATE_FILE.read_text()
README_TEMPLATE = README_TEMPLATE_FILE.read_text()
INIT_TEMPLATE = INIT_TEMPLATE_FILE.read_text()


@dataclass 
class Generate:
    """
    Configuration for generating the folder structure for an Advent of Code year.
    
    Attributes:
        year (int): The specifie year to generate the folder structure for.
        num_days (int): How many days to generate for the specified year.
        base_path (str): The base path to generate the folder structure from.
    """

    year: int
    num_days: int
    base_path: str = "." 

@dataclass
class Reset:
    """
    Configuration for the resetting solutions to an Advent of Code year.

    Attributes:
        year (int): The specified year to reset solutions.
        start (int): The first day to reset from. Default it 1. 
        end (int): The last day to reset from. Default is 25.
        base_path (str): The base path to reset from.
    """

    year: int
    start: int = 1
    end: int = 25
    base_path: str = "."



@dataclass
class SetupConfig:
    """
    Configuration for the Advent of Code setup CLI.
    
    Attributes:
        mode (Generate | Reset): The generate or reset configurations.

    """
    mode: Generate | Reset


def generate_table(num_days: int, completed_days: set[int] = set()) -> str:
    """
    Generate Markdown table rows for the README.

    Args:
        num_days (int): How many days to generate for the specified year.
        completed_days (set[int]): A set of the days with an existing solution. 
    """
    rows = []
    for d in range(1, num_days + 1):
        part1 = "&#10004;" if d in completed_days else ""
        part2 = "&#10004;" if d in completed_days else ""
        link = f"[solution](./Day{d}/solution.py)"
        rows.append(f"| {d}   | {part1}  | {part2}  | {link} |")
    return "\n".join(rows)    


def write_if_missing(path: Path, content: str):
    """
    Write file only if it doesn't exist.
    
    Args:
        path (Path): The path to write to.
        content (str): The content to write to the file.
    """
    if not path.exists():
        path.write_text(content)


def generate_year(year: int, num_days: int, base_path: str):
    """
    Generate year folder and all day subfolders.
    
    Args:
        year (int): The year 
        num_days (int): Number of Advent of Code puzzles for the given year.
        base_path (str): The base path for the year folder placement.
    """
    year_path = Path(base_path) / f"y{year}"
    year_path.mkdir(exist_ok=True)

    # Write year-level __init__.py
    write_if_missing(year_path / "__init__.py", INIT_TEMPLATE)

    # Generate day folders
    for day in range(1, num_days + 1):
        generate_day(year_path, day)

    # Generate README
    generate_readme(year_path, year, num_days)


def generate_day(year_path: Path, day: int):
    """
    Generate a single day folder with solution.py and __init__.py.
    
    Args:
        year_path (Path): The path to the year folder.
        day (int): The number corresponding to the day.
    """
    day_path = year_path / f"Day{day}"
    day_path.mkdir(exist_ok=True)

    # solution.py
    solution_file = day_path / "solution.py"
    write_if_missing(solution_file, SOLUTION_TEMPLATE)

    # __init__.py
    write_if_missing(day_path / "__init__.py", INIT_TEMPLATE)


def generate_readme(year_path: Path, year: int, num_days: int):
    """
    Generate the README.md for the year.

    Args:
        year_path (Path):
        year (int):
        num_days (int):
    """
    table_rows = generate_table(num_days)
    completed_count = 0  # default; could later detect completed days

    readme_text = README_TEMPLATE.format(
        year=year,
        total_days=num_days,
        completed_count=completed_count,
        table_rows=table_rows
    )
    (year_path / "README.md").write_text(readme_text)



def reset_year(year: int, start: int, end: int, base_path: str):
    """
    Reset solution files for a year or day range.
    
    Args:
        year (int): 
        start (int):
        end (int):
        base_path (str):
    """
    year_path = Path(base_path) / f"y{year}"

    for day in range(start, end + 1):
        day_path = year_path / f"Day{day}"
        if day_path.exists():
            solution_file = day_path / "solution.py"
            solution_file.write_text(SOLUTION_TEMPLATE)
        else:
            print(f"[SKIP] Day{day} does not exist; skipping.")

    # Regenerate README for full year (optional: could detect max day)
    all_days = [p for p in year_path.iterdir() if p.is_dir() and p.name.startswith("Day")]
    if all_days:
        generate_readme(year_path, year, len(all_days))


def main():
    config = tyro.cli(SetupConfig)

    if isinstance(config.mode, Generate):
        generate_year(
            config.mode.year,
            config.mode.num_days,
            config.mode.base_path
        )
    elif isinstance(config.mode, Reset):
        reset_year(
            config.mode.year,
            config.mode.start,
            config.mode.end,
            config.mode.base_path
        )
    else:
        raise ValueError("Unknown mode")



if __name__ == "__main__":
    main()