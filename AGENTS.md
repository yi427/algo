# Repository Guidelines

## Project Structure & Module Organization

This repository stores algorithm templates, study notes, and problem solutions.

- `templates/python/` and `templates/swift/`: reusable algorithm implementations such as `quick_pow`, `dsu`, and `trie`.
- `templates/python/tests/`: Python template tests. Current examples use `pytest`.
- `docs/algorithms/` and `docs/data-structures/`: Chinese study notes for algorithms and data structures.
- `problems/leetcode/` and `problems/lanqiao/`: problem write-ups named by platform ID, for example `204.md` or `17152.md`.

When adding a new solution, keep the explanation in a standalone Markdown file and update the platform README index in the same directory.

## Build, Test, and Development Commands

There is no global build system. Use small, file-level checks instead.

- `python -m pytest templates/python/tests`: run all Python template tests.
- `python -m pytest templates/python/tests/test_quick_pow.py`: run a focused test file.
- `python templates/python/quick_pow.py`: manually exercise the modular exponent example from stdin.
- `swiftc -parse-as-library templates/swift/quick_pow.swift`: syntax-check a Swift template without creating an app entry point.

Run commands from the repository root unless a script requires otherwise.

## Coding Style & Naming Conventions

Use 4-space indentation in Python and Swift. Follow the existing naming patterns:

- Python files and functions: `snake_case`, for example `euler_sieve.py`.
- Python classes and Swift types: `PascalCase`, for example `QuickPow`.
- Swift methods: `camelCase`.
- Problem notes: numeric filenames such as `50.md` or `5003.md`.

Keep Markdown notes in Chinese, consistent with the current docs. Prefer concise comments and reusable template code over problem-specific shortcuts.

## Testing Guidelines

Python tests use `pytest` and live under `templates/python/tests/`. Name files `test_<module>.py` and prefer parametrized cases for edge conditions. Add or update tests whenever changing shared Python templates such as fast power, DSU, or trie logic.

Swift templates do not currently have an automated test suite, so at minimum perform a syntax check with `swiftc`.

## Commit & Pull Request Guidelines

Recent commits use short Chinese summaries focused on the artifact added, such as `新增蓝桥杯 17152 题：最大区间` or `补充 20135 题 Sₙ 推导的两种方法`. Follow that style: start with the change type (`新增`, `补充`, `修正`) and include the platform or module name.

Pull requests should briefly explain scope, list affected paths, and mention any updated indexes or linked templates. If you add a problem write-up, note the problem ID and algorithm category.
