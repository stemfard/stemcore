from numpy import ndarray


def str_data_join(
    data: list | tuple | ndarray,
    delim: str = ", ",
    is_quoted: bool = False,
    use_map: bool = True,
    use_and: bool = False
) -> str:
    """
    Join a sequence of values into a single string.

    Parameters
    ----------
    data : list, tuple, or ndarray
        Sequence of values to join.
    delim : str, default ", "
        String inserted between values.
    is_quoted : bool, default False
        Whether to quote each value.
    use_map : bool, default True
        Whether to use ``map`` for string conversion.
    use_and : bool, default False
        Whether to insert ``"and"`` before the final item.

    Returns
    -------
    data_str : str
        Joined string representation of the input sequence.

    Notes
    -----
    NumPy arrays are converted to lists before processing. If `use_and`
    is True, the delimiter may be adjusted to produce grammatically
    correct output.

    Examples
    --------
    >>> import stemcore as stc
    >>>
    >>> stc.str_data_join([1, 2, 3])
    '1, 2, 3'
    >>> stc.str_data_join([1, 2, 3], use_and=True)
    '1, 2 and 3'
    >>> stc.str_data_join(['a', 'b'], is_quoted=True)
    "'a', 'b'"
    """
    if len(data) == 0:
        return ""

    if len(data) == 1:
        val = str(data[0])
        return f'"{val}"' if is_quoted else val

    if isinstance(data, ndarray):
        data = data.tolist()

    if use_and and len(data) > 1:
        data_copy = list(data)
        if len(data_copy) > 2:
            data_copy.insert(-1, "and")
            delim = ", "
        else:
            if is_quoted:
                return f"'{data_copy[0]}' and '{data_copy[1]}'"
            else:
                return f"{data_copy[0]} and {data_copy[1]}"
            
        data = data_copy

    if use_map:
        if is_quoted:
            data_str = map(lambda x: f"'{x}'", data)
        else:
            data_str = map(str, data)
        data_str = delim.join(data_str)
    else:
        if is_quoted:
            data_str = [f"'{v}'" for v in data]
        else:
            data_str = [str(v) for v in data]
        data_str = delim.join(data_str)

    data_str = data_str.replace(", 'and',", " and").replace(", and,", " and")

    return data_str

    
def str_data_join_contd(
    data,
    head: int = 5,
    tail: int = 3,
    use_map: bool = True,
    is_quoted: bool = False
):
    """
    Join a sequence of values into a truncated string representation.

    If the length of `data` exceeds `head + tail`, only the first `head`
    and last `tail` elements are shown, separated by an ellipsis ('...').
    
    Parameters
    ----------
    data : list, tuple, or ndarray
        Sequence of values to join.
    head : int, default 10
        Number of leading elements to display when truncation occurs.
    tail : int, default 3
        Number of trailing elements to display when truncation occurs.
    use_map : bool, default True
        Whether to use ``map`` for string conversion (faster for large sequences).
    is_quoted : bool, default False
        Whether to quote each value in the output string.

    Returns
    -------
    str
        Joined string representation of the sequence. If truncated, an
        ellipsis ('...') separates the leading and trailing elements.

    Notes
    -----
    - NumPy-style truncation behavior is used: truncation occurs only when 
      the sequence length exceeds ``head + tail``.
    - Symmetric truncation ensures that both the start and end of the sequence
      are shown.
    - NumPy arrays are implicitly converted to lists when joining.

    Examples
    --------
    >>> import stemcore as stc
    >>>
    >>> stc.str_data_join_contd([1, 2, 3])
    '1, 2, 3'
    >>> stc.str_data_join_contd(range(21))
    '0, 1, 2, 3, 4, ..., 18, 19, 20'
    >>> stc.str_data_join_contd(['a', 'b', 'c', 'd', 'e', 'f', 'g'], head=3, tail=2)
    'a, b, c, ..., f, g'
    >>> stc.str_data_join_contd(['a', 'b', 'c'], is_quoted=True)
    "'a', 'b', 'c'"
    """
    n = len(data)
    if n == 0:
        return ""

    kwargs = {
        "use_map": use_map,
        "is_quoted": is_quoted
    }

    # Truncate only if necessary
    if n <= head + tail:
        return str_data_join(data, **kwargs)

    head_str = str_data_join(data[:head], **kwargs)
    tail_str = str_data_join(data[-tail:], **kwargs)

    return f"{head_str}, ..., {tail_str}"