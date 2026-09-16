# Dash Sortable Items
A set of Dash components built with React that provide an interface to generate sortable items within a group.

## Manual installation

### Building the package

To install manually the package, first clone this repository, then setup a virtual environment and activate it with

```bash
python -m venv .venv
source .venv/bin/activate
```

To build the package, we use [just](https://just.systems/man/en/) which can be installed with

```
apt install just
```

To build the package, we need to install [Node.js](https://nodejs.org/en) and npm which can be installed with [nvm](https://github.com/nvm-sh/nvm) using the commands

```bash
nvm install
nvm use
```

Now, we need to install the python and Node dependencies using

```bash
just install
```

and, if necessary, clean old build files with 

```bash
just clean
```

If you just want to build the files, use

```bash
just build
```

If you rather want to generate the python wheel to install the library in your working environment run

```bash
just package
```

### Installing the python module

You can install manually this python library in your current environment by executing the following command in this directory 

```bash
pip install -e ./
```