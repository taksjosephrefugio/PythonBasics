import time
from threading_original import execute

threadSleepList = [5, 4, 3, 2, 1]

if __name__ == "__main__":
    start = time.perf_counter()
    execute(threadSleepList)
    finish = time.perf_counter()
    duration = round(finish-start, 2)
    print("Program Duration is {length}".format(length=duration))
