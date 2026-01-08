from typing import Any

from sympy import Expr, sympify

from stemcore.core.errors import ERR_SYMPIFY_ERRORS


def is_maths_function(obj: Any) -> bool:
    """
    Check whether an object is a usable mathematical function.

    Parameters
    ----------
    obj : object
        Object to test.

    Returns
    -------
    bool
        True if `obj` is callable and not a class, False otherwise.

    Notes
    -----
    Classes are callable but are excluded since they represent
    constructors rather than mathematical functions. Callable
    instances, including NumPy ufuncs such as ``np.sin``, are accepted.

    Examples
    --------
    >>> import numpy as np
    >>> import stemcore as stc
    >>> 
    >>> stc.is_maths_function(np.sin)
    True
    >>> stc.is_maths_function(lambda x: x**2)
    True
    >>> stc.is_maths_function(int)
    False
    """
    if not callable(obj):
        return False

    # Classes are callable but represent constructors
    if isinstance(obj, type):
        return False

    return True


def is_symexpr(obj: Any) -> bool:
    """
    Check whether an object is a symbolic expression with free symbols.

    A symbolic expression is defined as one containing at least one
    free symbol (variable), excluding defined constants.

    Parameters
    ----------
    obj : object
        Object to test.

    Returns
    -------
    bool
        True if `obj` represents a symbolic expression with free 
        symbols, False otherwise.

    Notes
    -----
    Only SymPy expressions are considered. String inputs are parsed using
    ``sympify`` and rejected if parsing fails or if no free symbols are
    present.

    Examples
    --------
    >>> import sympy as sym
    >>> x, y = sym.symbols('x y')

    >>> is_symexpr(sym.pi/4)
    False
    >>> is_symexpr(sym.pi/x)
    True
    >>> is_symexpr(x**2 + x*y - 5)
    True
    >>> is_symexpr('x**2 + y')
    True
    >>> is_symexpr('3.14')
    False
    >>> is_symexpr(42)
    False
    """
    if isinstance(obj, Expr):
        return bool(obj.free_symbols)

    if isinstance(obj, str):
        try:
            expr = sympify(obj)
        except ERR_SYMPIFY_ERRORS:
            return False

        if isinstance(expr, Expr):
            return bool(expr.free_symbols)

    return False