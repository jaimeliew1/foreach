

# `foreach`

`foreach` is a tiny Python package that provides a parallel for loop implementation using multiprocessing.

## Installation

You can install the package using pip:

```bash
pip install foreach
```

## Usage

```python
from foreach import foreach

def square(x):
    return x**2

params = [1, 2, 3, 4, 5]
result = foreach(square, params)
print(result)
# [1, 4, 9, 16, 25]
```

## `foreach` Parameters

```python
foreach(func: Callable, params: List, parallel: bool = True) -> List)
```
- `func` (callable): The function to apply to each element.
- `params` (list): The list of parameters to apply the function to.
- `parallel` (bool): If True, use multiprocessing for parallel execution. Default is True.




## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
