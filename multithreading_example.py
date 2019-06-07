"""Simple experiment with multi-threading.
IS590PR  J. Weible

With multiple threads active, try running this in PyCharm's "Concurrency Diagram" mode.
"""

from threading import Thread
import concurrent_functions as cf


def single_thread_sleepy(data):
    result = []
    for i in data:
        result.append(cf.f_sleepy(i))
    return result


def single_thread_busy(data):
    result = []
    for i in data:
        result.append(cf.f_busy(i))
    return result


def parallel_threads_sleepy(data):
    # Create a list to keep track of all threads created:
    thread_list = []
    for i in data:
        thread_list.append(Thread(target=cf.f_sleepy, args=[i], daemon=False))
        thread_list[i].start()  # begin executing the thread

        if i % 5 == 0:
            thread_list[i].join()


    # don't return until making sure EVERY thread has finished:
    # join() waits until specified thread is complete before the loop continues to create more
    for t in thread_list:
        t.join()
    return


def parallel_threads_busy(data):
    # Create a list to keep track of all threads created:
    thread_list = []
    for i in data:
        thread_list.append(Thread(target=cf.f_busy, args=[i], daemon=False))
        thread_list[i].start()  # begin executing the thread

        # join() waits until specified thread is complete before the loop continues to create more
        if i % 5 == 0:
            thread_list[i].join()

    # don't return until making sure EVERY thread has finished:
    for t in thread_list:
        t.join()
    return


if __name__ == '__main__':
    d = list(range(10))
    print('The input data list: \n', d)

    print('single_thread_sleepy()...')
    cf.time_f(single_thread_sleepy, d)

    print('single_thread_busy()...')
    cf.time_f(single_thread_busy, d)

    # Even hundreds of these "sleepy" task threads can run concurrently without any significant increase
    # in total run time:
    print('parallel_threads_sleepy()...')
    cf.time_f(parallel_threads_sleepy, d)

    # But two or more of these CPU-intensive threads will compete for CPU all the time (because they're all in
    # the same process). Thus because of extra overhead and task switching, they might even perform WORSE overall
    # than a sequential non-concurrent version in a single process does (like single_thread_busy above):
    print('parallel_threads_busy()...')
    cf.time_f(parallel_threads_busy, d)



