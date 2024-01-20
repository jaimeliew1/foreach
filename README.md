

# `foreach`

`foreach` is a tiny Python package that provides a parallel for loop implementation using multiprocessing.

## Installation

You can install the package using pip:

```bash
pip install foreach
```

## Usage

```python
import foreach

def square(x):
    return x**2

params = [1, 2, 3, 4, 5]
result = foreach(square, params)
print(result)
# [1, 4, 9, 16, 25]
```

## `foreach` Parameters

```python
foreach(func: Callable, params: Iterable, parallel: bool = True, num_processes: int = None, callback: Callable = None) -> List
```

- `func` (callable): The function to apply to each element.
- `params` (iterable): The iterable of parameters to apply the function to.
- `parallel` (bool): If True, use multiprocessing for parallel execution. Default is True.
- `num_processes` (int): Number of processes to use in parallel execution (default is None, letting Pool decide).
- `callback` (callable): Optional callback function to execute after each iteration.

Returns:
- List: A list of results from applying the function to each element.


## Examples

### Sequential Execution

```python
import foreach

def square(x):
    return x**2

params = [1, 2, 3, 4, 5]
result = foreach(square, params, parallel=False)
print(result)
# [1, 4, 9, 16, 25]
```


### Callback Functionality

```python
import foreach

def square(x):
    return x**2

params = [1, 2, 3, 4, 5]

def callback(x):
    print(f"Processed: {x}")

result = foreach(square, params, callback=callback)
# Processed: 1
# Processed: 4
# Processed: 9
# Processed: 16
# Processed: 25
```

### Customizing Number of Processes

```python
import foreach

def square(x):
    return x**2

params = [1, 2, 3, 4, 5]
result = foreach(square, params, num_processes=2)
print(result)
# [1, 4, 9, 16, 25]
```
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
