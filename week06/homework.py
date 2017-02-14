def return_unique(iterable):
    '''
    Return the unique elements from an iterable.

    Example:

    >>> list(return_unique('abcabc'))
    ['a', 'c', 'b']
    '''
    pass

def fib(n, k0, k1):
    '''A generator returning the first $N + 1$ elements of the Fibonacci
    series given starting with values $k_0$ and $k_1$, such that 
    $$k_i = k_{i-1} + k_{i-2},\quad i = 2, \ldots, N$$.

    Example:

    >>> list(fib(5, 2, 3))
    [2, 3, 5, 8, 13]

    '''
    pass

def safe_call(f):
    '''Tries to call return f. Catches ValueErrors (and only thonse),
    returning None in that case.

    Example:

    >>> safe_call(lambda : 3)
    3
    >>> def raise_value_error():
    ...     raise ValueError()
    ...
    >>> safe_call(raise_value_error) == None
    True
    >>> def raise_name_error():
    ...     raise NameError()
    ...
    >>> safe_call(raise_name_error)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "homework.py", line 16, in safe_call
        return f()
      File "<stdin>", line 2, in raise_name_error
    NameError

    '''
    pass

def curve_predict(f, X_train, y_train, X_test):
    '''Given training data `X_train, y_train` and a function `f` performs
    a least-squares fit using `scipy` and predicts the values for
    `X_test`.

    Example:
    >>> import numpy as np
    >>> def f(x, a, b, c):
    ...     return a + b*x + c*x**2
    ...
    >>> x = np.arange(0, 1, 0.2)
    >>> y = f(x, 1, 2, 3)
    >>> curve_predict(f, x, y, x)
    array([ 1.  ,  1.52,  2.28,  3.28,  4.52])

    '''
    pass
