import ast
from dataclasses import dataclass
from math import exp, cos, sin
from pprint import pprint
from collections import namedtuple
from numbers import Number


@dataclass
class DualNum:
    value: float
    derivative: float

    def __init__(self, value: float, derivative: float = 0):
        self.value = value
        self.derivative = derivative

    def __add__(self, other):
        return DualNum(self.value + other.value, self.derivative + other.derivative)

    def __mul__(self, other):
        return DualNum(
            self.value * other.value,
            self.derivative * other.value + self.value * other.derivative,
        )

    def __pow__(self, k: int):
        return DualNum(self.value**k, self.derivative * k * self.value ** (k - 1))

    def exp(self):
        return DualNum(exp(self.value), self.derivative * exp(self.value))

    def cos(self):
        return DualNum(cos(self.value), -self.derivative * sin(self.value))


# insert string containing function into local namespace
F_STR = """
def f(x):
    return exp(x)**3 + cos(x) * x + 10**2
"""
exec(F_STR)
assert "f" in locals(), "f is not defined in the local namespace"


# parse tree
tree = ast.parse(F_STR)
"""
Module(
    body=[
        FunctionDef(
            body=[
                Return(
                    value=BinOp(
                        
                        left=BinOp(
                            left=BinOp( <------ `exp(x)**3` AS LEFT
                                left=Call(
                                    func=Name(id='exp', ctx=Load()),
                                    name='f',
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(arg='x')],
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        defaults=[]
                                    ),
                                    args=[Name(id='x', ctx=Load())],
                                    keywords=[]
                                ),
                                op=Pow(),
                                right=Constant(value=3)
                            ),
                            
                            op=Add(), <------ LEFT + RIGHT
                            
                            right=BinOp( <------ `cos(x) * x` AS RIGHT
                                left=Call(
                                    func=Name(id='cos', ctx=Load()),
                                    args=[Name(id='x', ctx=Load())],
                                    keywords=[]
                                ),
                                
                                op=Mult(),
                                
                                right=Name(id='x', ctx=Load())
                            )
                            ),
                        
                            op=Add(),
                        
                            right=BinOp(left=Constant(value=10),
                        
                            op=Pow(),
                        
                            right=Constant(value=2)
                        )
                    )
                )
            ],
            decorator_list=[],
            type_params=[]
        )
    ],
    type_ignores=[]
)
"""


# get the derivative of f(x) at x
def f_forward_ad(x: DualNum) -> DualNum:
    # walk AST and replace nodes with custom functions
    for node in ast.walk(tree):
        # print instance of node
        print(node)

        # if isinstance(node, ast.Add):
        #     print("Add", node)
        # elif isinstance(node, ast.Mult):
        #     print("Mult", node)
        # elif isinstance(node, ast.Call):
        #     print("Call", node)
        # elif isinstance(node, ast.Pow):
        #     print("Pow", node)
        # elif isinstance(node, ast.Constant):
        #     print("Constant", node)
        # elif isinstance(node, ast.Name):
        #     print("Name", node)

    # Execute the modified AST
    # exec(compile(tree, filename="<ast>", mode="exec"))

    # Return the result

    return f(0)  # type: ignore


f_forward_ad(DualNum(666))

# # Test the function with a simple function
# FUNCTION_STRING = """
# def f(x):
#    return x**2
# """
# exec(FUNCTION_STRING)
# assert "f" in locals(), "f is not defined in the local namespace"

# x = DualNum(2, 1)
# result = f_forward_ad(x)
# assert result.value == 4, "The primal value is incorrect"
# assert result.derivative == 4, "The derivative is incorrect"

# # Test the function with a complex function
# FUNCTION_STRING = """
# def f(x):
#    return exp(x)**3 + cos(x) * x + 10**2
# """
# exec(FUNCTION_STRING)
# assert "f" in locals(), "f is not defined in the local namespace"

# x = DualNum(2, 1)
# result = f_forward_ad(x)
# assert abs(result.value - 148.386) < 1e-3, "The primal value is incorrect"
# assert abs(result.derivative - 1064.182) < 1e-3, "The derivative is incorrect"
