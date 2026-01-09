"""
============
stemcore
============

`stemcore` is a Python library with core functions in
scientific, engineering and data-intensive applications."

See the webpage for more information and documentation:

    https://stemcore.stemfard.org
"""

import sys

if sys.version_info < (3, 9):
    raise ImportError('stemcore requires Python 3.9 or above.')
del sys

__version__ = '0.0.1'
__author__ = 'John Indika'
__credits__ = 'STEM Research'
__email__ = "stemcore@stemfard.org"
__description__ = "Core functions in STEM and mathematics applications"
__url__ = "https://stemcore.stemfard.org"
__license__ = "MIT"
__copyright__ = f"Copyright (c) 2026 {__credits__}"

from .core import(
    # convert 
    arr_to_numeric,
    
    # _decimals
    numeric_format,
    
    # _is_dtypes
    is_maths_function, is_symexpr,
    
    # _strings
    str_data_join, str_data_join_contd,
    
    # _symbolic
    sym_lambdify_expr,
)

__all__ = [
    # convert
    "arr_to_numeric",
    
    # decimals
    "numeric_format",
    
    # is_dtypes
    "is_maths_function", "is_symexpr",
    
    # strings
    "str_data_join", "str_data_join_contd",
    
    # symbolic
    "sym_lambdify_expr", "sym_expr_to_numpy_function"
]

#===========================================================================#
#                                                                           #
# STEM RESEARCH :: AI . APIs . Innovate :: https://stemcore.stemfard.org   #
#                                                                           #
#===========================================================================#