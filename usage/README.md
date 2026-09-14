# Running the examples

To run the different examples, create and activate a python virtual environment with

```bash
python -m venv .venv
source .venv/bin/activate
```

And then install the dependencies with

```bash
pip install -r requirements.txt
```

Do not forget to also build the `dash_sortable_items` python package in the root folder with

```bash
just package
```

and then to install it from the root directory with 

```bash
pip install -e ./
```