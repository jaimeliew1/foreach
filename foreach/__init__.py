import sys
from multiprocessing import get_context
from typing import Callable, Iterable, List, Literal, Optional

from tqdm import tqdm


def foreach(
    func: Callable,
    params: Iterable,
    parallel: bool = True,
    processes: Optional[int] = None,
    callback: Optional[Callable] = None,
    context: Optional[Literal["fork", "spawn", "forkserver"]] = None,
) -> List:
    """
    Parallelly apply a given function to each element in the input iterable.

    Parameters:
    - func (Callable): The function to apply to each element.
    - params (Iterable): The iterable of parameters to apply the function to.
    - parallel (bool): If True, use multiprocessing for parallel execution.
    - processes (int): Number of processes to use in parallel execution (default is None, letting Pool decide).
    - callback (Callable): Optional callback function to execute after each iteration.
    - context (str): Context of how multiprocessing spawns new processes.
    Returns:
    - List: A list of results from applying the function to each element.
    """

    N = len(params) if hasattr(params, "__len__") else None

    out = []
    if parallel:
        with get_context(context).Pool(processes=processes) as pool:
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
