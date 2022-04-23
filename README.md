# project-with-xela

this is an empty project you can use to commit your python example code

## To use:

Python packaging is it's own special hell. To avoid this, use virtualenv. Developers here are responsible for creating a virtual python environment:


Ubuntu:

First install virtualenv:

```
python3 -m pip install virtualenv
```

Now that virtualenv is installed, create a virtual environment, and `source` it.

```
python3 -m virtualenv venv
source venv/bin/activate
```

You should see a `(venv)` in your terminal prompt. You should always `source venv/bin/activate` before doing anything!

**After activating your virtualenv**, install the requirements:

```
pip install -r requirements.txt
```
