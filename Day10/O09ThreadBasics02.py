
import threading
import time

def doJob():
    print(f"Function going to sleep....{threading.current_thread().name}")
    time.sleep(2)
    print(f"Just woke up.......{threading.current_thread().name}")

thrd1 = threading.Thread(target=doJob, name="thrd1")
thrd2 = threading.Thread(target=doJob, name="thrd2")
thrd3 = threading.Thread(target=doJob, name="thrd3")

s = time.perf_counter()

thrd1.start()
thrd2.start()
thrd3.start()

thrd1.join()
thrd2.join()
thrd3.join()

e = time.perf_counter()

print(f"Total time taken is {round(e - s, 2)}")