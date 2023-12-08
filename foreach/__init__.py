from typing import Callable, List
from multiprocessing import Pool
from tqdm import tqdm


def foreach(func: Callable, params: List, parallel: bool = True) -> List:
    """
    Parallelly apply a given function to each element in the input list.

    Parameters:
    - func (Callable): The function to apply to each element.
    - params (List): The list of parameters to apply the function to.
    - parallel (bool): If True, use multiprocessing for parallel execution.

    Returns:
    - List: A list of results from applying the function to each element.
    """
    N = len(params)
    out = []
    if parallel:
        with Pool() as pool:
            for x in tqdm(pool.imap(func, params), total=N):
                out.append(x)
        return out
    else:
        for param in tqdm(params):
            out.append(func(param))
        return out
