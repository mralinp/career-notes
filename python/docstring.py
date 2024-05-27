def factorial(n):
    """
    Calculate the factorial of a non-negative integer.

    The factorial of a non-negative integer n is the product of all positive
    integers less than or equal to n. It is denoted as n!.

    Args:
        n (int): A non-negative integer whose factorial is to be computed.

    Returns:
        int: The factorial of the input integer n.
        
    Raises:
        ValueError: If n is a negative integer.

    Examples:
        >>> factorial(5)
        120
        >>> factorial(0)
        1
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result