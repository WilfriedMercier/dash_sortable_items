## Setting up the testing environment

Setting up the environment for testing requires few steps but can be tricky. Since testing relies on Dash + [pytest](https://docs.pytest.org/en/stable/), it uses under the hood [selenium](https://www.selenium.dev/) which requires a web driver to be installed. By default, [Chromium](https://www.chromium.org/Home/) is used.

Once a web driver is installed, check with a script that the browser does open and can be controlled programmatically. Then, go to the `test/python` directory and setup the test environment with

```python
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

If not already done, create the python wheel of the package (see the [building page](building.md)) and install it with

```python
pip install -e ../..
```

## Running the test-suite manually

To run the entire test suite manually, assuming the test environment is activated, just run `#!bash pytest`. You can also specify a single file and, optionally, a class as well as a method within the class with

```bash
pytest myfile.py::myclass::mymethod
```

## Running the test-suite automatically

Alternatively, it is possible to run the test suite from the root directory without activating the test environment with the following command:

```bash
just test
```