def read_file_or_buffer(file_or_buffer, delim=','):
    """Reads a .csv file or buffer with a custom delimiter into a
    pandas dataframe."""
    pass

def add_squared_column(data_frame, column_name):
    """Adding the square of a row to the data frame. The new column will
    be called <old_name>_sq. Will modify the original data frame.

    Example:

    >>> a = pd.DataFrame({'A': [1,2,3]})
    >>> add_squared_column(a, 'A')
    >>> a
       A  A_sq
    0  1     1
    1  2     4
    2  3     9
    """
    pass

def transform(data_frame, new_column_name, f, *fn_args):
    """Transfom columns of a data frame to make a new column, given a
    function. Will modify the original data frame.

    Example:
    >>> a = pd.DataFrame({'A': [1,2,3],
                          'B': [0.1, 0.2, 0.3]})
    >>> f = lambda x, y: x + y
    >>> transform(a, 'C', f, 'A', 'B')
       A    B    C
    0  1  0.1  1.1
    1  2  0.2  2.2
    2  3  0.3  3.3
    """
    pass

def MSE(y_pred, y_known):
    """Calculates a approximation fo the mean squared error, given the
    true values of y and predictions (as vectors), i.e. calculates

    $$\sum_{i=1}^n (y_{pred,i} - y_{known, i})^2 / n$$

    """
    pass

def MSE_KNN(X_train, y_train, X_test, y_test, k):
    """Fits a k-Nearest neighbor regrssion model, using training data
    and calculates the mean squared error on a testing data set."""
    pass
