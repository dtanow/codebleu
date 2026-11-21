# CLAUDE.md - Guidelines for CodeBLEU

## Commands
- Install: `pip install -e .[all,test]` (macOS: `pip install -e .\[all,test\]`)
- Run tests: `python -m pytest`
- Run single test: `python -m pytest tests/test_codebleu.py::test_function_name -v`
- Lint: 
  - `python -m isort codebleu --check`
  - `python -m black codebleu --check`
  - `python -m ruff codebleu`
  - `python -m mypy codebleu`

## Code Style
- Line length: 120 characters
- Python: 3.9+ with strict typing
- Formatting: Black with isort (profile: black)
- Imports: group by standard, third-party, first-party; combine as_imports
- Naming: snake_case for functions/variables, PascalCase for classes
- Type annotations: required for all functions, use generics appropriately
- Error handling: use pytest.raises for testing, descriptive asserts
- Test coverage: maintain high coverage, use parametrized tests

## Project Structure
- Core metrics in root codebleu/ directory
- Language-specific resources in keywords/
- Parser utilities in parser/
- Type safety enforced with py.typed