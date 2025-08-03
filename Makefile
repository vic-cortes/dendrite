.PHONY: format

format:
	echo "Running code formatting..."
	uv run ruff check --fix

server_up:
	echo "Starting Mock S7 Server..."
	uv run utils/server.py