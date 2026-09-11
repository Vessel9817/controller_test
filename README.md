# Joystick Visual Test

[![License][license-badge]](LICENSE)
[![CI][ci-badge]][ci-workflow]

Note: For Windows users, use the built-in `joy.cpl` executable to visually test
and diagnose controller issues. It may also show relevant notes, such as where
to download the appropriate device drivers. However, even if it doesn't
recognize controller input, this program may still function properly, because
it relies on generic controller capabilities and uses lower-level APIs that may
supersede driver problems.

## Usage

```shell
# Create a virtual environment
py -m venv "./venv"

# Activate the virtual environment
"./venv/Scripts/activate"

# Install dependencies to the virtual environment
pip install -r requirements-freeze.txt

# Run the program in the virtual environment
py main.py
```

[license-badge]: https://raw.githubusercontent.com/Vessel9817/controller_test/refs/heads/main/license.svg
[ci-badge]: https://github.com/Vessel9817/controller_test/actions/workflows/ci.yml/badge.svg
[ci-workflow]: https://github.com/Vessel9817/controller_test/actions/workflows/ci.yml
