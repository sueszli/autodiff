# autodiff 💨

A bare-bones implementation of **forward-mode autodiff** (AD / Automatic Differentiation) using Python's AST (Abstract Syntax Tree) purely for educational purposes.

Credit to [Ivan Yashchuk](https://github.com/IvanYashchuk) for providing the initial implementation.

<br>

_Quick install:_

```bash
# clone
git clone https://github.com/sueszli/autodiff
cd autodiff

# install dependencies
if command -v python3 &>/dev/null; then echo "Python 3 is installed."; else echo "Python 3 is not installed."; fi
python3 -m pip install --upgrade pip > /dev/null
pip3 install pipreqs > /dev/null && rm -rf requirements.txt > /dev/null && pipreqs . > /dev/null
pip3 install -r requirements.txt > /dev/null

# run unit tests
python3 autodiff.py


<<###OUTPUT
Original function:

def f(x):
    return exp(x)**3 + cos(x) * x + 10**2

Transformed function:

def f_forward_ad(x: DualNum) -> DualNum:
    return DualNumOps.custom_add(DualNumOps.custom_add(DualNumOps.custom_pow(DualNumOps.custom_exp(x), 3), DualNumOps.custom_mul(DualNumOps.custom_cos(x), x)), (10 ** 2))

----------------------------------------------------------------------
Ran 6 tests in 0.388s

OK
###OUTPUT
```

<br><br>

_Further reading:_

- Python AST
  - Official documentation for Python AST: https://docs.python.org/3/library/ast.html
  - Additional documentation for Python AST: https://greentreesnakes.readthedocs.io/en/latest/index.html
- Forward AD and dual numbers:
  - https://en.wikipedia.org/wiki/Automatic_differentiation#Automatic_differentiation_using_dual_numbers
  - https://youtu.be/5F6roh4pmJU?si=LW1ZKKvaGdl9shCz&t=555
- Other implementations:
  - https://gist.github.com/nihalkenkre/e51619241de182d8de07acc277787182
