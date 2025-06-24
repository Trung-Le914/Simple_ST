def approx_sinh(x, n):
    """
    Approximate the hyperbolic sine of x using the Taylor series expansion.
    Parameters:
    x (float): The input value.
    n (int): Number of terms in the Taylor series expansion.
    Returns:
    float: Approximate value of sinh(x) using n+1 terms.
    """
    result = x
    
    for i in range(1,n+1):
        result += (x**(2*i+1))/(factorial(2*i+1))
    
    return result

