UV := ~/.local/bin/uv
VENV := .venv
VENV_BIN := $(VENV)/bin

.PHONY: all lint ruff mypy pyright radon clean

all: lint

lint: ruff mypy pyright radon

ruff:
	@$(VENV_BIN)/ruff check . --config ruff.toml

mypy:
	@$(VENV_BIN)/mypy .

pyright:
	@$(VENV_BIN)/pyright

radon:
	@$(VENV_BIN)/radon cc . -nc -nb -s -a | tee radon_report.txt
	@if grep -E '\bC\b|\bD\b|\bE\b|\bF\b' radon_report.txt; then \
		echo '❌ Complexidade acima do nível B encontrada!'; \
		exit 1; \
	else \
		echo '✅ Complexidade dentro dos limites.'; \
	fi

clean:
	rm -rf $(VENV) radon_report.txt
