<p align="center">
	<img src="https://www.python.org/static/community_logos/python-logo-generic.svg" alt="Python" width="180" />
</p>

<h1 align="center">Learn Python</h1>

<p align="center">
	A step-by-step Python learning lab built from fundamentals, algorithms, and small practical projects.
</p>

<p align="center">
	<img src="https://img.shields.io/badge/Python-3.14%2B-3776AB?style=for-the-badge&logo=python&logoColor=FFD43B" alt="Python 3.14 or newer" />
	<img src="https://img.shields.io/badge/Learning_by-Doing-F2C94C?style=for-the-badge" alt="Learning by doing" />
	<img src="https://img.shields.io/badge/Projects-Practical-2D9CDB?style=for-the-badge" alt="Practical projects" />
</p>

## What this repository is

This is a hands-on Python learning repository. Each topic starts with a focused concept, then turns that concept into an
implementation you can read, run, modify, and extend.

The goal is simple: learn the idea, see the mechanics, and build something small enough to understand completely.

## What you will learn

- Python syntax, variables, strings, collections, loops, functions, lambdas, and exceptions
- Object-oriented programming with inheritance, abstraction, encapsulation, properties, and special methods
- Recursion, dynamic programming, searching, sorting, graphs, backtracking, and shortest paths
- Core data structures including linked lists and hash tables
- Practical problem-solving with validation, state management, input handling, and reusable functions
- How to turn a specification into a small working program, such as a budget app, cipher, inventory, tracker, or
  simulator
- How to read existing code, trace behavior, debug mistakes, and improve an implementation step by step

## Learning path

The folders are intentionally arranged as a progression rather than a single finished application:

```text
1. basic/                         Python language fundamentals
2. oop/                           Object-oriented programming
3. Recursion/                     Recursive thinking
4. dynamic_programing/            Reusable solutions to optimization problems
5. algorithms/                    Classic algorithms and graph problems
6. building_a_*/                  Small projects that combine the ideas
7. isbn_validator/                Validation and real-world input rules
8. medical_records_validator/     Structured data validation
9. user_configuration_manager/   Configuration and persistence concepts
```

## Project map

### Foundations

| Area                  | Topics and examples                                                                                                         |
|-----------------------|-----------------------------------------------------------------------------------------------------------------------------|
| `basic/`              | Debugging, dictionaries, exceptions, dynamic attributes, numbers, lambdas, lists, loops, sets, strings, and special methods |
| `oop/`                | Abstraction, encapsulation, inheritance, name mangling, polymorphism, and properties                                        |
| `Recursion/`          | Recursive function design and base cases                                                                                    |
| `dynamic_programing/` | Climbing stairs, coin change, and Fibonacci problems                                                                        |

### Algorithms and data structures

| Area                      | Implementations                                                                                                                                                                                                 |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `algorithms/`             | Binary search, breadth-first search, depth-first search, merge sort, quick sort, selection sort, Luhn validation, N-Queens, shortest path, Tower of Hanoi, square-root bisection, and adjacency-list conversion |
| `building_a_linked_list/` | A linked list data structure                                                                                                                                                                                    |
| `building_a_hash_table/`  | A hash table implementation                                                                                                                                                                                     |

### Small practical projects

| Folder                                     | Project                                      |
|--------------------------------------------|----------------------------------------------|
| `building_a_budget_app/`                   | Track spending with a simple budget workflow |
| `building_a_caesar_cipher/`                | Encode and decode text with a Caesar cipher  |
| `building_a_character_status_tracker/`     | Manage changing character state              |
| `building_a_cipher/`                       | Work with a Vigenere cipher                  |
| `building_a_discount_calculator/`          | Calculate discounts from user input          |
| `building_a_email_simulator/`              | Simulate email-style interactions            |
| `building_a_media_catalogue/`              | Organize a media collection                  |
| `building_a_musical_instrument_inventory/` | Model and manage inventory items             |
| `building_a_player_interface/`             | Practice interfaces and player behavior      |
| `building_a_polygon_area_calculator/`      | Calculate areas for different shapes         |
| `building_a_salary_tracker/`               | Track salary information                     |
| `character_create/`                        | Create and validate a character              |
| `isbn_validator/`                          | Validate ISBN values                         |
| `luhn_algorithm_for_error-checking/`       | Apply the Luhn error-checking algorithm      |
| `medical_records_validator/`               | Validate medical record data                 |
| `secret_code_extractor/`                   | Extract information from encoded input       |
| `user_configuration_manager/`              | Work with user configuration data            |

## Getting started

### 1. Clone the repository

```bash
git clone <repository-url>
cd PythonBasic
```

### 2. Install uv

This repository uses [uv](https://docs.astral.sh/uv/) to manage Python versions, the project environment, and dependencies. On Windows, install it with WinGet:

```powershell
winget install --id=astral-sh.uv -e
```

You can also use uv's [official installation methods](https://docs.astral.sh/uv/getting-started/installation/).

### 3. Create the project environment

Python 3.14 or newer is expected by the project configuration. If Python 3.14 is not already installed, let uv install it:

```bash
uv python install 3.14
```

Sync the environment from `pyproject.toml`:

```bash
uv sync
```

This creates or updates the local `.venv` environment and installs the locked project dependencies. You do not need to activate the environment when using `uv run`.

### 4. Run a lesson or project

Most exercises are standalone Python files. Run one from the repository root through the managed environment:

```bash
uv run python algorithms/binary_search/binary_search.py
uv run python building_a_budget_app/budget_app.py
```

Read the file first, predict what it will do, run it, then change one thing and run it again. That loop is the core of
this repository.

## A practical study loop

1. Choose one folder and read the smallest example first.
2. Write down the input, output, and main idea before running it.
3. Execute the script and compare the result with your prediction.
4. Change an edge case, a value, or one part of the algorithm.
5. Explain the implementation in your own words and build a small variation.

## Development tools

The project is configured for Python 3.14+ and includes development tooling for formatting and static analysis:

```bash
uv run black .
uv run pyrefly check
```

## Repository philosophy

> Understand the concept. Implement the smallest useful version. Test the edge cases. Then make it yours.

This repository favors readable code and practical repetition over hiding the learning process behind large frameworks.
The projects are intentionally small so you can inspect every moving part.

## Helpful references

- [Python documentation](https://docs.python.org/3/)
- [Python logo and usage guidelines](https://www.python.org/community/logos/)
- [Python Beginner's Guide](https://wiki.python.org/moin/BeginnersGuide)

## License

This repository is for learning and experimentation.
