# Code Kata Python Template

This is the code kata template for python created by [Aula de Software Libre de la Universidad de Córdoba](https://www.uco.es/aulasoftwarelibre/)

You can use this repository as a template or open it directly by clicking here:

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/aulasoftwarelibre/codekata-template-python)

Codespaces installs all dependencies automatically. If you prefer to work locally, follow these steps.

## Step 1. Use this repository as a template

Press the button "Use this template" and create a new repository on your space. Then clone it locally.

## Step 2. Install uv

This template uses the [uv](https://docs.astral.sh/uv/) package manager. Follow the [official installation guide](https://docs.astral.sh/uv/getting-started/installation/), or run:

```
# Linux and macOS
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

You don't need to install Python: uv downloads the right version for you.

## Step 3. Install dependencies

```
uv sync
```

## Step 4. Run the tests

```
uv run pytest
```

While doing the kata, you can keep the tests running in the background. They run again every time you save a file:

```
uv run ptw .
```

You can also use the test runner in your IDE. In VS Code, use **Run Tests with Coverage** in the Testing panel to see which lines your tests cover.

## Code quality checks

These checks also run on every push and pull request:

```
uv run ruff format   # format the code
uv run ruff check    # lint
uv run mypy          # type check
```
