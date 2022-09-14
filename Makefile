all:
python_executable:
	@pyinstaller --onefile -n commands --hidden-import namespace.cloud ./commands/main.py
cleanup:
	rm -r build
	rm commands.spec
