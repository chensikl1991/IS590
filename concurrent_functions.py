"""Supporting functions for the code in 'multiprocess_example.py' and 'multithreading_example.py'
IS590PR  J. Weible
"""

import time
import numpy as np


def f_sleepy(x):
    """Compute and return x squared.

    This function takes 1 second to execute, but nearly all of that time is "sleeping".  That will
    explicitly yield to the OS task switcher immediately after its real "work" of computing the square
    is done.  So this kind of mostly-idle task can be readily run concurrently with many other similar
    tasks, regardless of whether they are processes or threads.

    :param x: a number
    :return: x squared.

    >>> a = f_sleepy(70)    #doctest: +NORMALIZE_WHITESPACE
    4900
    >>> a = f_sleepy(100)   #doctest: +NORMALIZE_WHITESPACE
    10000
    >>> a = f_sleepy('q')   # raises an Exception with bad input
    Traceback (most recent call last):
     ...
    TypeError: can't multiply sequence by non-int of type 'str'

    """
    time.sleep(1)  # delay to force this function to be slow.
    answer = x * x
    print(answer, ' ', end='', flush=True)
    return answer


def f_busy(x):
    """This function also returns x squared, but before doing that, it generates a lot of random
    np.ndarrays so that (on my computer at least), it takes approximately 1 second to complete.

    Since this function keeps one CPU very busy, it will not yield early to the OS task switcher
    like f_sleepy() does.  Thus this is a realistic simulator of CPU-bound parallel tasks.

    :param x: a number
    :return: x squared

    >>> a = f_busy(7)    #doctest: +NORMALIZE_WHITESPACE
    49
    >>> a = f_busy(10)   #doctest: +NORMALIZE_WHITESPACE
    100
    """
    for i in range(900):
        junk = np.random.uniform(0, 1000, size=100000)
    answer = x * x
    print(answer, ' ', end='', flush=True)
    return answer


def time_f(func, data):
    """Run the specified function on the data, and report how long it took to execute.

    :param func: The function we want executed by time_f()
    :param data: The data (parameter) to send through to func()
    :return: result of executing func()

    >>> r = time_f(f_sleepy, 3)  #doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
    9
    total elapsed time: ...s. Main process CPU time: ...s
    <BLANKLINE>
    """
    start_p = time.process_time()
    start = time.time()
    result = func(data)
    elapsed_p = time.process_time() - start_p
    elapsed = time.time() - start
    print('\ntotal elapsed time: {:0.4f}s. Main process CPU time: {:0.4f}s\n'.format(elapsed, elapsed_p))
    return result

