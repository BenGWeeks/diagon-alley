# Makefile for Diagon Alley LNbits extension

.PHONY: format check black ruff test

# Format all code
format: black ruff

# Run all checks
check: black-check ruff-check

# Format Python with black
black:
	uvx black .

# Check Python formatting with black
black-check:
	uvx black --check .

# Format/fix Python with ruff
ruff:
	uvx ruff check --fix .

# Check Python with ruff
ruff-check:
	uvx ruff check .

# Run tests
test:
	pytest tests/ -v
