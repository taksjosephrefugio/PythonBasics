import time
import concurrent.futures


def do_something(sleepTime):
    print("Sleeping for {time} second(s)...".format(time=sleepTime))
    time.sleep(sleepTime)
    return("Done sleeping {time} seconds(s)...".format(time=sleepTime))


def execute(listofSeconds):
    # create threads where the input is a list of sleep time in seconds
    executor = concurrent.futures.ThreadPoolExecutor()
    threadList = [executor.submit(do_something, sec) for sec in listofSeconds]

    # prints results of threads as they come in (should be in ascending order in this case)
    completed_returns = concurrent.futures.as_completed(threadList)
    for thread in completed_returns: print(thread.result())

    # # prints results in the order that they are started
    # for thread in threadList: print(thread.result())

if __name__ == "__main__":
    threadSleepList = [5, 4, 3, 2, 1]
    start = time.perf_counter()
    execute(threadSleepList)
    finish = time.perf_counter()
    duration = round(finish - start, 2)
    print("Program Duration is {length}".format(length=duration))
