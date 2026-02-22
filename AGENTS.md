# AGENTS.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview
Minimal Python 3.12 project managed with `uv`. No external dependencies currently configured.

## Commands

### Setup
```bash
uv sync
```

### Run
```bash
uv run main.py
uv run test.py
```

### Add dependencies
```bash
uv add <package>
```

## Architecture
- `main.py` — entry point, exposes a `main()` function
- `test.py` — standalone scripts (currently `fizzbuzz`); no test framework is configured yet
