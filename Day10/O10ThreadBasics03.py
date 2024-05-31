
import threading
import time

def doJob(secs, tname):
    print(f"Function going to sleep....{threading.current_thread().name}")
    time.sleep(2)
    print(f"Just woke up.......{threading.current_thread().name}")

thrd1 = threading.Thread(target=doJob, name="thrd1")
thrd2 = threading.Thread(target=doJob, name="thrd2")
thrd3 = threading.Thread(target=doJob, name="thrd3")

s = time.perf_counter()

threads = []

for i  in range(500):
    t = threading.Thread(target=doJob, name="thrd"+str(i), args=[2, "thrd" + str(i)])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

e = time.perf_counter()
print(f"Total time taken is {round(e - s, 2)}")