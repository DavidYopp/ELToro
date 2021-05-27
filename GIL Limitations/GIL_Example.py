import time
from threading import Thread
from multiprocessing import JoinableQueue, Process


num = 0
#our countdown method
def countdown(num):
    while num < 100000000:
        num += 1

#a single process example (normal execution)
start_time = time.time()
countdown(num)
end_time = time.time()

delta = end_time - start_time
print("Runtime in standard 1 thread iteration: {} seconds".format(delta))

#a multithreaded example
first_thread = Thread(target=countdown, args=(50000000,))
second_thread = Thread(target=countdown, args=(50000000,))

start_time = time.time()
first_thread.start()
second_thread.start()
first_thread.join()
second_thread.join()

end_time = time.time()
delta = end_time - start_time
print("Runtime in multiple threads: {} seconds".format(delta))

#a multiprocessing example
start_time = time.time()
joinable_queue = JoinableQueue()
joinable_queue.put([50000000,50000000])
first_thread = Process(target=countdown, args=(joinable_queue,))
end_time = time.time()
delta = end_time - start_time
print("Runtime in multiprocessing: {} seconds".format(delta))
