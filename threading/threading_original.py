import time
import threading

def do_something(sleepTime):
    print("Sleeping for {time} second(s)...".format(time=sleepTime))
    time.sleep(sleepTime)
    print("Done sleeping {time} seconds(s)...".format(time=sleepTime))


def execute(listofSeconds):
    thread_list = [threading.Thread(target=do_something, args=[sec]) for sec in listofSeconds]
    for i in range(len(thread_list)): thread_list[i].start()
    for i in range(len(thread_list)): thread_list[i].join()


if __name__ == "__main__":
    threadSleepList = [5, 4, 3, 2, 1]
    start = time.perf_counter()
    execute(threadSleepList)
    finish = time.perf_counter()
    duration = round(finish - start, 2)
    print("Program Duration is {length}".format(length=duration))
