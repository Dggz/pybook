
# Code to execute in an independent thread
import time
def countdown(n):
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(0.2)
    return


# Create and launch a thread
from threading import Thread
t = Thread(target=countdown, args=(10, ))
t.start()
t.join()

# -----
# for extra control

import time
from threading import Thread
class CountdownTask:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, n):
        while self._running and n > 0:
            print('T-minus', n)
            n -= 1
            time.sleep(0.2)

c = CountdownTask()
t = Thread(target=c.run, args=(10,))
t.start()
t.join()      # Wait for actual termination (if needed)
c.terminate() # Signal termination


# -----
# worse version because of dependency
# import time
# from threading import Thread
#
# class CountdownThread(Thread):
#     def __init__(self, n):
#         super().__init__()
#         self.n = 0
#     def run(self):
#         while self.n > 0:
#             print('T-minus', self.n)
#             self.n -= 1
#             time.sleep(1)
#
# c = CountdownThread(5)
# c.start()

# import multiprocessing
# c = CountdownTask()
# p = multiprocessing.Process(target=c.run, args=(10,))
# p.start()
# p.join()


from threading import Thread, Event
import time

# Code to execute in an independent thread
def countdown(n, started_evt):
    print('countdown starting')
    started_evt.set()
    while n > 0:
        print('T-minus', n)
        n -= 1
        time.sleep(0.2)

# Create the event object that will be used to signal startup
started_evt = Event()

# Launch the thread and pass the startup event
print('Launching countdown')
t = Thread(target=countdown, args=(10, started_evt))
t.start()

# Wait for the thread to start
started_evt.wait()
print('countdown is running')
t.join()


# -----
import threading
import time

class PeriodicTimer:
    def __init__(self, interval):
        self._interval = interval
        self._flag = 0
        self._cv = threading.Condition()

    def start(self):
        t = threading.Thread(target=self.run)
        t.daemon = True
        t.start()

    def run(self):
        '''
        Run the timer and notify waiting threads after each interval
        '''
        while True:
            time.sleep(self._interval)
            with self._cv:
                 self._flag ^= 1
                 self._cv.notify_all()

    def wait_for_tick(self):
        '''
        Wait for the next tick of the timer
        '''
        with self._cv:
            last_flag = self._flag
            while last_flag == self._flag:
                self._cv.wait()

# Example use of the timer
ptimer = PeriodicTimer(1)
ptimer.start()

# Two threads that synchronize on the timer
def countdown(nticks):
    while nticks > 0:
        ptimer.wait_for_tick()
        print('\nT-minus', nticks)
        nticks -= 1

def countup(last):
    n = 0
    while n < last:
        ptimer.wait_for_tick()
        print('\nCounting', n)
        n += 1

t1 = threading.Thread(target=countdown, args=(10,))
t2 = threading.Thread(target=countup, args=(5,))

t1.start()
t2.start()

t1.join()
t2.join()

# ----

# from queue import Queue
# from threading import Thread
#
# # A thread that produces data
# def producer(out_q):
#     while True:
#         # Produce some data
#         data = input()
#         if data == '0':
#             break
#         else:
#             out_q.put(data)
#
# # A thread that consumes data
# def consumer(in_q):
#     while True:
#         # Get some data
#         data = in_q.get()
#         if data == '0':
#             break
#         # Process the data
#         else:
#             print(str.upper(data))
#     exit()
#
# # Create the shared queue and launch both threads
# q = Queue()
# t1 = Thread(target=consumer, args=(q,))
# t2 = Thread(target=producer, args=(q,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# q.join()

# ----

# workaround GIL
# https://web.archive.org/web/20170704003616/http://chimera.labs.oreilly.com:80/books/1230000000393/ch12.html#_problem_205

# Processing pool (see below for initiazation)
pool = None

# Performs a large calculation (CPU bound)
def some_work(args):
    result = args ** 2
    return result

# A thread that calls the above function
# def some_thread():
#     while True:
#         r = pool.map(some_work, (3, 4, 5))
#         print(r)

# Initiaze the pool
if __name__ == '__main__':
    import multiprocessing
    pool = multiprocessing.Pool()
    pool.map(some_work, [3, 4, 5])

# Actor, actor as generator
# https://web.archive.org/web/20170704003616/http://chimera.labs.oreilly.com:80/books/1230000000393/ch12.html#_solution_206

# Exchange, publish/subscribe
# https://web.archive.org/web/20170704003616/http://chimera.labs.oreilly.com:80/books/1230000000393/ch12.html#_solution_207

# Generators as alternative to threads
# https://web.archive.org/web/20170704003616/http://chimera.labs.oreilly.com:80/books/1230000000393/ch12.html#_solution_208\



def countdown(n):
    while n > 0:
        print('T-minus', n)
        yield
        n -= 1
    print('Blastoff!')

def countup(n):
    x = 0
    while x < n:
        print('Counting up', x)
        yield
        x += 1

from collections import deque
class TaskScheduler:
    def __init__(self):
        self._task_queue = deque()

    def new_task(self, task):
        '''
        Admit a newly started task to the scheduler
        '''
        self._task_queue.append(task)

    def run(self):
        '''
        Run until there are no more tasks
        '''
        while self._task_queue:
            task = self._task_queue.popleft()
            try:
                # Run until the next yield statement
                next(task)
                self._task_queue.append(task)
            except StopIteration:
                # Generator is no longer executing
                pass

# Example use
sched = TaskScheduler()
sched.new_task(countdown(10))
sched.new_task(countdown(5))
sched.new_task(countup(15))
sched.run()
