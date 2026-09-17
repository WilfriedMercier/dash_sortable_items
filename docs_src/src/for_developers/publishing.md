## Building the docs locally

### Manual build

To build the docs locally, go to the `docs_src` directory and, if not already done, create a virtual environment with

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Then, you can build the docs with 

```bash
mkdocs build
```

or serve the docs with live updates with

```bash
mkdocs serve
```

### Automatic build using the justfile

Assuming the virtual environment in the `docs_src` directory already exists with the dependencies installed and that the virtual environment in the root directory is already activated, it is possible to build the docs with the command

```bash
just build-docs
```

or to serve the docs with live updates with

```bash
just serve-docs
```