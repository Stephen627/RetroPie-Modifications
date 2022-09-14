all: python_executable
	@echo 'Done'
install_dependencies:
	@echo '=== Installing Dependencies'
	pip install pyinstaller
python_executable:
	@echo '=== Making python executable'
	@pyinstaller --onefile -n commands --hidden-import namespace.cloud ./commands/main.py
cleanup:
	rm -r build
	rm commands.spec
