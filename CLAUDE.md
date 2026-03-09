# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a personal algorithm learning repository for recording algorithm templates, study notes, and problem solutions across multiple programming languages.

## Repository Structure

- `templates/{language}/` - Algorithm template implementations by language (currently: python, swift)
- `docs/data-structures/` - Data structure study notes and documentation
- `docs/algorithms/` - Algorithm study notes and documentation (e.g., quick_pow.md)
- `problems/leetcode/` - LeetCode problem solutions with README.md index
- `problems/lanqiao/` - Lanqiao (蓝桥杯) problem solutions with README.md index

## Working with This Repository

When adding algorithm templates:
- Place language-specific implementations in the corresponding `templates/{language}/` directory
- Keep templates focused and reusable
- Use consistent naming across languages for the same algorithm
- Templates may include multiple variants (e.g., `quick_pow` and `quick_pow_with_mod` for different use cases)

When adding problem solutions:
- Organize by platform (leetcode or lanqiao)
- Solutions can be in any of the supported languages
- Create a markdown file for each problem with links to template code
- Update the platform's README.md index file with problem classification

When writing documentation:
- Use Chinese for notes (user's preferred language)
- Place in appropriate subdirectory under `docs/`
