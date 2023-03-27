# Python Package 
The idea of this package is that functions which most likely will be used in multiple Woonstad Rotterdam projects can be imported from this central package.

## Usage
See [docs](<link>) for extensive documentation.


### Examples
<details><summary>timeit</summary>

> ```python
> from package_name.decorators import timeit
>
> @timeit
> def square(x):
>    result = x * x
>    time.sleep(1)  # simulate some computation
>    return result
> 
> square(3)
> ```
        

Running this code will results in a logging message which shows the execution time:
> ```bash
> 2023-03-26 06:22:03.437 | DEBUG    | __main__:<module>:14 - Function 'square' executed in 1.000057 s
> ```

</details>

## For contributors
Follow the following steps to add code:


### 1. Installation

Inside a virtual Python(>=3.9) environment: 
```bash
git clone <git link>
cd <package_name>
pip install -e ".[dev]"
pre-commit install
```

### 2. Write your code

1. Choose in which (sub)module your function/class should reside (or add a new one)
2. Switch to a new branch using `git switch -c <branch-name>`
3. Write the code for the function/class. 
    - Make sure to use [type hinting](https://docs.python.org/3/library/typing.html) for function parameters. 
    - Choose easily-understandable variable names (no single letters or unobvious abbrevations)
    - All code and comments must be in English
4. Add tests to the [`tests`](tests/) directory using `pytest`. [ChatGPT](https://chat.openai.com/chat) is excellent in helping to write good and many tests. Make sure **to not send any sensitive data or code to ChatGPT**. Ask for edge case tests too.
    - After writing the tests, run `coverage run -m pytest`. Make sure all tests pass, if not, adapt your code.
    - Run `coverage report` and make sure your code has a 100% coverage. If not, add (different kinds of) tests.
5. If all tests have passed and your coverage is 100%, add docstrings ([Numpy format](https://python.plainenglish.io/how-to-write-numpy-style-docstrings-a092121403ba)) and possibly some comments inside the code. Again, as long as your code doesn't contain sensitive information, feel free to use [ChatGPT](https://chat.openai.com/chat). **Make sure to always properly check ChatGPT's output**. Preferebly ask ChatGPT to add an `Examples` section the docstrings.
6. Ideally add documentations to the function inside [docs](https://dev.azure.com/woonstad/Data_Science/_git/woonstad_rotterdam?path=/docs.md) and the [Examples](#examples) section of this README.

### 3. Commit your code

Because this package is used in different Woonstad Projects, it is important that the `main` branch is **always** at production level. Direct commits to the `main` branch are therefore **blocked**.



To ensure production-level quality code, [`pre-commit`](https://pre-commit.com/) checks if your code adheres to production-level quality code using the following libraries:
- [`isort`](https://pycqa.github.io/isort/): A Python utility that sorts imports alphabetically and automatically separates them into sections and by type.
- [`black`](https://black.readthedocs.io/en/stable/): An opinionated code formatter that formats Python code to be consistent and readable.
- [`flake8`](https://flake8.pycqa.org/en/latest/): A tool that combines several Python code quality checkers and linters to help enforce style and programming rules.
- [`mypy`](https://mypy.readthedocs.io/en/stable/): A static type checker for Python that helps catch common programming errors and improve code quality.
- [`interrogate`](https://interrogate.readthedocs.io/en/latest/): A tool for checking the quality and consistency of docstrings in Python code.
- [`darglint`](https://github.com/terrencepreilly/darglint): A tool for linting function arguments and checking that they adhere to PEP8 standards.
- [`pytest`](https://docs.pytest.org/en/7.2.x/): A testing framework that makes it easy to write and run tests in Python.
- [`coverage`](https://coverage.readthedocs.io/en/7.2.2/): A tool for measuring the code coverage of Python code, which helps identify areas that lack test coverage.
- [`pylint`](https://pylint.org/): A Python linter that checks for errors, code smells, and other issues to help improve code quality.

When committing code using `git commit -m <message>`, `pre-commit` will run these packages against your commit. If any of these tests fail, your commit will be rejected. Please adjust your code to ensure your code follows this packages standards.  
If you believe your error is too strict or irrelevant, feel free to add an ignore of that error to the relevant config file (one of `.coveragerc`, `.flake8`, `.pre-commit-config.yaml`, `.pylintrc`, `pyproject.toml`, `setup.cfg`).  
When committing, `black` will automatically reformat your code to this package standards if it doesn't adhere yet. Therefore, **you might need to re-add the changes** made by `black` using `git add <files>` and then commit again using `git commit -m <message>`.

### 4. Create pull request

