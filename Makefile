PYTHON := python3
GREEN := \033[0;32m
RED := \033[0;31m
RESET := \033[0m

.PHONY: run compile

run:
	@test -n "$(INPUT)" || (printf "$(RED)%s$(RESET)\n" 'Usage: make run INPUT=path/to/file.py' && exit 1)
	@printf "$(GREEN)%s$(RESET)\n" '$(PYTHON) compile.py --input "$(INPUT)" --output "$(INPUT:.py=.bf)"'
	@$(PYTHON) compile.py --input "$(INPUT)" --output "$(INPUT:.py=.bf)"
	@printf "$(GREEN)%s$(RESET)\n" '$(PYTHON) run.py --input "$(INPUT:.py=.bf)"'
	@$(PYTHON) run.py --input "$(INPUT:.py=.bf)"

compile:
	@test -n "$(INPUT)" || (printf "$(RED)%s$(RESET)\n" 'Usage: make compile INPUT=path/to/file.py' && exit 1)
	@printf "$(GREEN)%s$(RESET)\n" '$(PYTHON) compile.py --input "$(INPUT)" --output "$(INPUT:.py=.bf)"'
	@$(PYTHON) compile.py --input "$(INPUT)" --output "$(INPUT:.py=.bf)"
