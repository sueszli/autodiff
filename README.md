# autodiff ✎ᝰ

A bare-bones implementation of forward-mode automatic differentiation (AD) using Python's abstract syntax tree (AST) for educational purposes.

Special thanks to [Ivan Yashchuk](https://github.com/IvanYashchuk) @ Nvidia for guidance and feedback

<br>

_Content:_

- Introduction to building interpreters with JAX: `jax-inverse-function.ipynb`
- Automatic differentiation: `autodiff.py`
- Performance optimization by leveraging PyTorch (2-3x speedup): `pytorch-ast-optimization.py`

<br>

_Quick install:_

```bash
pip install -r requirements.txt
python3 autodiff.py

<< ////
Original function:

def f(x):
    return exp(x)**3 + cos(x) * x + 10**2

Transformed function:

def f_forward_ad(x: DualNum) -> DualNum:
    return DualNumOps.custom_add(DualNumOps.custom_add(DualNumOps.custom_pow(DualNumOps.custom_exp(x), 3), DualNumOps.custom_mul(DualNumOps.custom_cos(x), x)), (10 ** 2))

----------------------------------------------------------------------
Ran 6 tests in 0.388s

OK
////
```
