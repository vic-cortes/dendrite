.PHONY: format

format:
	echo "Running code formatting..."
	uv run ruff check --fix