import random
import time
import threading
import concurrent.futures
executor = concurrent.futures.ThreadPoolExecutor()
dataVal = 0
stop_threads_flag = False


# Updates the value of global var dataVal with a random number b/w 0-9
def update_data():
    global dataVal
    while stop_threads_flag is False:
        dataVal = random.randrange(10)
        print("Successful data update...")
        time.sleep(1)


# Prints the value of global var dataVal
def print_data():
    while stop_threads_flag is False:
        print("Data: ", dataVal)
        time.sleep(2)


if __name__ == "__main__":
    # Start all threads
    t1 = executor.submit(update_data)
    t2 = executor.submit(print_data)

    '''
    # Alternative way
    threadlist = [threading.Thread(target=update_data), threading.Thread(target=print_data)]
    for thread in threadlist: thread.setDaemon(True)
    for thread in threadlist: thread.start()
    for thread in threadlist: thread.join()
    '''

    # Poll for threads to stop
    stop_threads_flag = (True if int(input()) == 1 else False)







