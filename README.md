# autodiff ✎ᝰ

A bare-bones implementation of **forward-mode autodiff** (Automatic Differentiation AD) using Python's AST (Abstract Syntax Tree) for educational purposes.

<br>

_Content:_

- Introduction to building interpreters with JAX: `jax-inverse-function.ipynb`
- Automatic differentiation: `autodiff.py`
- Performance optimizations by leveraging PyTorch: `pytorch-ast-optimization.py` (2-3x speedup)

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

<br>

Credit to [Ivan Yashchuk](https://github.com/IvanYashchuk) for providing the initial implementation.
