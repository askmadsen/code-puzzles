# Code Puzzles

Welcome to my **Code Puzzles** repository, a collection of Python solutions for challenges from multiple years of Advent of Code. To access the problems and puzzle inputs see the official webpage: [Advent of Code](https://adventofcode.com/about)



## Requirements
Before running any of the puzzle solutions, make sure you have the following installed:

- Python 3.10+  
- Tyro  (for running the CLI commands)
- NumPy (used in some solutions for numerical operations)

Install all Python dependencies via:

```bash
pip install -r requirements.txt
```

## Project Structure

```
code-puzzles/
├─ run.py                 # Unified CLI to run all solutions. Prints output and execution time
├─ setup.py               # Unified CLI for complete folder setup or resetting solutions
├─ requirements.txt       # Requirements for running the puzzle solutions
├─ README.md              # Project overview and usage instructions
├─ aoc_templates/         # Folder with templates
|   ├─ template.md        # Used to autogenerate the README file for a generated year
|   ├─ template.py        # Used to autogenerate the solutions file for a given day
├─ y2025/                 # Folder for Advent of Code year 2025
│   ├─ README.md          # Year overview highlighting solved puzzles and interesting solutions
│   ├─ Day01/             # Folder for each day 1 in year 2025
│   │   ├─ solution.py    # Fast and slow implementations of the puzzle for that day
│   │   └─ (optional test/input files)
│   ├─ Day02/             
│   │   ├─ solution.py
│   │   └─ (optional test/input files)
│   └─ Day03/ …
├─ y2024/
│   ├─ README.md
│   ├─ Day01/
│   │   ├─ solution.py
│   │   └─ …
│   └─ Day02/ …
└─ y2023/ …
```

## Setup

Clone the repository

```bash
git clone https://github.com/askmadsen/code-puzzles.git
```

To generate the entire folder structure for a given Advent of Code year

```bash
# Generates the folder structure for year 2025 with 12 puzzle days.
python setup.py mode:generate --mode.year 2025 --mode.num-days 12
```


To reset an entire year or part of solutions for a given Advent of Code year


```bash
# Resets the solutions for year 2025 from day 2 until day 5.
python setup.py mode:reset --mode.year 2025 --mode.start 2 --mode.end 5

# Resets all solutions for year 2024.
python setup.py mode_reset --mode.year 2024 
```


## Usage

To run any puzzle solution, navigate to the root folder and use the following CLI:


```bash
# Runs both solutions to part 1 of the puzzle from year 2015, day 1 on the given input file
python run.py --year 2015 --day 1 --part 1 --method both --input y2015/Day1/input.txt

# Runs the fast solution to part 2 of the puzzle from year 2020, day 20 on the given input file
python run.py --year 2020 --day 20 --part 2 --method fast --input y2020/Day20/input.txt

# Runs the slow solution to part 2 of the puzzle from year 2020, day 20 on the input 203023
python run.py --year 2020 --day 20 --part 2 --method fast --input 203023
```

## Years

| Year    | Progress          | Link                      |
|---------|-------------------|---------------------------|
| 2015    | 15/50 &#11088;     | [2015](y2015/README.md)   |
| 2016    | 0/50 &#11088;     | [2016](y2016/README.md)   |
| 2017    | 0/50 &#11088;     | [2017](y2017/README.md)   |
| 2018    | 0/50 &#11088;     | [2018](y2018/README.md)   |
| 2019    | 0/50 &#11088;     | [2019](y2019/README.md)   |
| 2020    | 0/50 &#11088;     | [2020](y2020/README.md)   |
| 2021    | 0/50 &#11088;     | [2021](y2021/README.md)   |
| 2022    | 0/50 &#11088;     | [2022](y2022/README.md)   |
| 2023    | 0/50 &#11088;     | [2023](y2023/README.md)   |
| 2024    | 0/50 &#11088;     | [2024](y2024/README.md)   |
| 2025    | 0/50 &#11088;     | [2025](y2025/README.md)   |

> **Note:** Resetting solutions for a specific year will clear that year's solution files
> and regenerate its README table. The global progress table above is **not affected**.


## Additional Information
- This repository does **not** include official puzzle inputs, puzzle descriptions, or any other Advent of Code content. Only my own solutions to the puzzles are provided. The repository does **not** use the Advent of Code brand beyond mentioning the brand name and linking to the [official site](https://adventofcode.com/about).  
- Optional small test inputs may exist within each day’s folder to quickly verify correctness.
- Fast and slow implementations allow comparing brute-force vs optimized approaches.