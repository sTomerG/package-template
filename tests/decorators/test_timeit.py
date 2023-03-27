import logging

from package_name.decorators import timeit


def test_timeit_decorator(caplog):
    # Create a mock function to be decorated
    def mock_func():
        return "Hello, World!"

    # Decorate the mock function with the timeit decorator
    decorated_func = timeit(mock_func)

    # make sure logging is at level debug
    with caplog.at_level(logging.DEBUG):
        # Call the decorated function
        result = decorated_func()

        # Check that the result is the same as the original function
        assert result == mock_func()
        assert "mock_func" in caplog.text
        assert "executed" in caplog.text
