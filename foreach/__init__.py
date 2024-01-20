import sys
from multiprocessing import Pool
from typing import Callable, Iterable, List

from tqdm import tqdm


def foreach(
    func: Callable,
    params: Iterable,
    parallel: bool = True,
    processes: int = None,
    callback: Callable = None,
) -> List:
    """
    Parallelly apply a given function to each element in the input iterable.

    Parameters:
    - func (Callable): The function to apply to each element.
    - params (Iterable): The iterable of parameters to apply the function to.
    - parallel (bool): If True, use multiprocessing for parallel execution.
    - processes (int): Number of processes to use in parallel execution (default is None, letting Pool decide).
    - callback (Callable): Optional callback function to execute after each iteration.

    Returns:
    - List: A list of results from applying the function to each element.
    """

    N = len(params) if hasattr(params, "__len__") else None

    out = []
    if parallel:
        with Pool(processes=processes) as pool:
            for result in tqdm(pool.imap(func, params), total=N):
                out.append(result)
                if callback:
                    callback(result)
        return out
    else:
        for param in tqdm(params):
            result = func(param)
            out.append(result)
            if callback:
                callback(result)
        return out


sys.modules[__name__] = foreach
