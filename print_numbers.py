import threading
from time import sleep

THREADS = 3
event = threading.Condition()
target = 1


def worker(thread_ind, N):
    global target
    for _ in range(N):
        with event:
            event.wait_for(lambda: thread_ind % THREADS == target)
            target = (target + 1) % THREADS
            print(thread_ind, end = '')


if __name__ == '__main__':
    N = int(input())
    workers = [threading.Thread(target=worker, args=(i, N)) for i in range(1, 4)]
    for w in workers:
        w.start()

    for _ in range(N * 3):
        with event:
            event.notify_all()
        sleep(0.0001)

    for w in workers:
        w.join()
