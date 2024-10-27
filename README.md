# Code Kata Python Template

This is the code kata template for python created by [Aula de Software Libre de la Universidad de Córdoba](https://www.uco.es/aulasoftwarelibre/)

You can use this repository as a template or open it directly by clicking here:

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/aulasoftwarelibre/codekata-template-python)

Codespace install all dependencies automatically, if you prefer to install locally follow these steps:

## Step 1. Use this repository as a template

Press the button "Use this template" and create a new repository on your space.

## Step 2. Clone the repository

Clone locally your repository.

## Step 3. Install package manager

This template uses [uv](https://docs.astral.sh/uv/) package manager.

To install it you can follow the [official installation manual](https://docs.astral.sh/uv/getting-started/installation/).

### Fast installation

You can install running this:

```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

If `uv` command does not works is because it requires `$HOME/.cargo/bin` into your `$PATH`.

Run this and/or add to your shell config script:

```
export PATH=$HOME/.cargo/bin:$PATH
```

## Step 4. Install requirements

And install requirements

```
uv sync
```

## Step 5. Execute test

```
uv run pytest
```

You can also use tests runner in your IDE.
