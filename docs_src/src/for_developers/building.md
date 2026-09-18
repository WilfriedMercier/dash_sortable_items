## Setting up the enviroment

To manually install the python library, first clone this repository, then setup a virtual environment, activate it, and install [just](https://just.systems/man/en/) with

```bash
python -m venv .venv
source .venv/bin/activate
apt install just
```

We also need to install [Node.js](https://nodejs.org/en) and npm which can be installed with [nvm](https://github.com/nvm-sh/nvm) with

```bash
nvm install
nvm use
```

To install the python and Node dependencies required to build the package run

```bash
just install
just clean
```

## Building the python library for testing

To build the package, that is launch the process that transforms the React/Typescript files into a runnable python library that is compatible with Dash, use

```bash
just build
```

## Building the python library to install locally

Alternatively, one can generate a python wheel that can be installed in any virtual environment with

```bash
just package
```

Afterwards, the library can be installed from the root directory with

```bash
pip install -e ./
```