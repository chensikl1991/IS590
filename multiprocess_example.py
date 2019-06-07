"""Simple experiment with multiprocessing.
IS590PR  J. Weible

https://docs.python.org/3.6/library/multiprocessing.html"""

from multiprocessing import Pool
import concurrent_functions as cf


def single_process_sleepy(data):
    result = []
    for i in data:
        result.append(cf.f_sleepy(i))
    return result


def single_process_busy(data):
    result = []
    for i in data:
        result.append(cf.f_busy(i))
    return result


def parallel_processes_sleepy(data):
    with Pool(processes=2) as pool:   # allow up to x worker processes
        result = pool.map(cf.f_sleepy, data)    # distribute data array
    return result


def parallel_processes_busy(data):
    with Pool(processes=2) as pool:   # allow up to x worker processes
        result = pool.map(cf.f_busy, data)    # distribute data array
    return result


if __name__ == '__main__':
    d = list(range(10))
    print('The input data list: \n', d)

    print('single_process_sleepy()...')
    cf.time_f(single_process_sleepy, d)

    print('single_process_busy()...')
    cf.time_f(single_process_busy, d)

    # Even many dozens of these "sleepy" task processes can run concurrently
    # without any significant increase in total run time:
    print('parallel_processes_sleepy()...')
    r = cf.time_f(parallel_processes_sleepy, d)
    # print(r)

    # But because these "busy" tasks will intensively occupy the CPU,
    # increasing the number of simultaneous processes beyond the number
    # of real *available* CPUs will not improve performance further.
    # Except, if your CPUs have 'Hyper-threading', you might see some
    # small improvement using a number of processes up to 2 * CPU cores.

    # But beyond that there can't be any benefit:
    print('parallel_processes_busy()...')
    r = cf.time_f(parallel_processes_busy, d)
    # print(r)

