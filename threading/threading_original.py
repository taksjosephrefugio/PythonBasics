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