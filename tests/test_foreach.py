import foreach


def square(x):
    return x**2


def test_sequential_square():
    params = [1, 2, 3, 4, 5]
    result = foreach(square, params, parallel=False)
    expected_result = [1, 4, 9, 16, 25]
    assert result == expected_result


def test_parallel_square():
    params = [1, 2, 3, 4, 5]
    result = foreach(square, params, parallel=True)
    expected_result = [1, 4, 9, 16, 25]
    assert result == expected_result


def test_iterator_parallel():
    params = range(1, 6)
    result = foreach(square, params, parallel=True)
    expected_result = [1, 4, 9, 16, 25]
    assert result == expected_result


def teset_num_processes():
    params = range(1, 6)
    result = foreach(square, params, parallel=True, processes=2)
    expected_result = [1, 4, 9, 16, 25]
    assert result == expected_result


def test_foreach_callback():
    params = [1, 2, 3, 4, 5]
    callback_results = []

    def callback(x):
        callback_results.append(x)

    result = foreach(square, params, parallel=True, callback=callback)
    assert result == [1, 4, 9, 16, 25]
    assert callback_results == result
