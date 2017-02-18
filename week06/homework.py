def lin_reg_coefs(X, colname_x, colname_y, degree):
    '''
    Given a pandas data frame X, and column names x and y, will fit
    a polynomial of a given degree to X[x], X[y].

    Example:

    >>> x = range(10)
    >>> y = [i**2 + 2*i + 42 for i in x]
    >>> data = pd.DataFrame({'x': x, 'y': y})
    >>> homework.lin_reg_coefs(data, 'x', 'y', 2)
    array([ 42.,   2.,   1.])
    '''
    pass

def relevant_features(X, y):
    '''
    Given a (X * p) feature matrix X and a traget vector y, returns a list of
    booleans indicating which columns of X should receive a regression coefficient
    different from zero.    
   
    Example:
    >>> # note: this can go wrong sometimes!
    >>> # Our confidence intervalse cover 99% of the cases...
    >>> from sklearn.datasets import make_regression
    >>> X,y, coef = make_regression(200, 20, 15, coef=True, noise=20)
    >>> list(zip(coef, homework.relevant_features(X, y)))
    [(0.0, False),
    (23.494316236763936, True),
    (21.331578893815628, True),
    (74.303855112117361, True),
    (0.0, False),
    (48.853119042392947, True),
    (6.7305423143776411, True),
    (79.323657173596274, True),
    (28.987193637283958, True),
    (25.507666479434789, True),
    (73.995697853045456, True),
    (47.861532159016228, True),
    (47.236919314310832, True),
    (16.450140733678388, True),
    (93.746262789889883, True),
    (0.0, False),
    (34.354181663053218, True),
    (0.0, False),
    (0.0, False),
    (61.573901192150096, True)]
    '''
    pass

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
