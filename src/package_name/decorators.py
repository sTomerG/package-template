import logging
import time

logger = logging.getLogger("__name__")


def timeit(func):
    """
    Decorator that measures the execution time of a function.

    Parameters
    ----------
    func : callable
        The function to be decorated.

    Returns
    -------
    wrapped : callable
        A new function that wraps the original function and measures its execution time.

    """

    def wrapped(*args, **kwargs):
        """
        A wrapper function that measures the execution time of the original function.

        Parameters
        ----------
        *args : tuple
            The positional arguments to be passed to the original function.
        **kwargs : dict
            The keyword arguments to be passed to the original function.

        Returns
        -------
        result : any
            The result of the original function.

        """
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        logger.debug(f"Function '{func.__name__}' executed in {end - start:f} s")
        return result

    return wrapped
