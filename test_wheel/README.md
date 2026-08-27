# Testing the python wheel

To test the python wheel, create a virtual environment and activate it with

```bash
pyton -m venv venv
source venv/bin/activate
```

Then, in the parent directory, install dash and the python wheel with

```bash
pip install dash
pip install -e ./
```

You should now be able to run `test_wheel.py` and check that the wheel was installed correctly.