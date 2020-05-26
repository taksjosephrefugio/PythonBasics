import time
import concurrent.futures


def do_something(sleepTime):
    print("Sleeping for {time} second(s)...".format(time=sleepTime))
    time.sleep(sleepTime)
    return("Done sleeping {time} seconds(s)...".format(time=sleepTime))


def execute(secondslist, manner, printMethod):
    executor = concurrent.futures.ThreadPoolExecutor()

    if manner is "ThreadPoolExecutor":
        threadlist = [executor.submit(do_something, sec) for sec in secondslist]
        if printMethod is "as_completed":
            threadsWithResults = concurrent.futures.as_completed(threadlist)
            for thread in threadsWithResults: print(thread.result())
        elif printMethod is "in_order_of_started":
            for thread in threadlist: print(thread.result())

    elif manner is "executorMaps":
        threadlist = executor.map(do_something, secondslist)
        if printMethod is "as_completed":
            print("As completed can't be achieved with executor.maps")
        elif printMethod is "in_order_of_started":
            for results in threadlist: print(results)


if __name__ == "__main__":
    threadSleepList = [5, 4, 3, 2, 1]
    printMethod = {"as_completed": "as_completed", "in_order_of_started": "in_order_of_started"}
    manner = {"ThreadPoolExecutor": "ThreadPoolExecutor", "executorMaps": "executorMaps"}

    start = time.perf_counter()

    try: execute(threadSleepList, manner["executorMaps"], printMethod["in_order_of_started"], )
    except KeyError: print("Either Printing Method or Manner is not specified properly")

    finish = time.perf_counter()
    duration = round(finish - start, 2)
    print("Program Duration is {length}".format(length=duration))
