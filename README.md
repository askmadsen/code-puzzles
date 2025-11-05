# Code Puzzles

Welcome to my **Code Puzzles** repository, a collection of Python solutions for challenges from multiple years of advent of code. To access the problems and puzzle inputs see the official webpage: [Advent of Code](https://adventofcode.com/about)

## Repository Structure

- `run.py` – Unified CLI to run any solution.
- `YEAR/` – Folder for each year (e.g., `2015`, `2016`), containing:
  - `DayX/` – Solutions for each day.
  - `README.md` – Highlights, interesting approaches, or notes for that year.
- Each day may contain:
  - `solution.py` – Fast and/or slow implementations.

## Usage

Run any solution from the root folder using the CLI:

```bash
python run.py --year YEAR --day DayX --part <1|2> --method <fast|slow|both> --input path/to/input.txt
```

### Arguments

- `YEAR` – The year of the Advent of Code challenge (e.g., `2015`).
- `DayX` – The day of the challenge (e.g., `Day1`, `Day12`).
- `--part` – The part of the day’s problem to solve:
  - `1` – Part 1
  - `2` – Part 2
- `--method` – Which solution to run:
  - `fast` – Optimized/efficient solution
  - `slow` – Brute-force or slower solution
  - `both` – Run both fast and slow solutions (prints outputs and execution times for each)
- `--input` – Path to your input file. If not provided, the solution runs with an empty string.


## Years

- [2015](2015/README.md)
- [2016](2016/README.md)
- [2017](2017/README.md)


## Additional Information
- Solutions are modular and can be run individually.
- This repository does not include official input files; provide your own input when running solutions.
- Optional small test inputs may exist within each day’s folder to quickly verify correctness.
- Fast and slow implementations allow comparing brute-force vs optimized approaches.