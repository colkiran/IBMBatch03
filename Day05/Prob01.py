

import time
def timeCalc(fnc):

    def helper(cntr):
        print("function starting to execute.....")
        st  = time.perf_counter()
        fnc(cntr)
        et = time.perf_counter()
        print("function executed successfully......")
        print(f"The time taken by the function is {round(et - st, 2)}")

    return helper

@timeCalc
def fun(tm):
    lst = []
    for i in range(tm):
        for j in range(1, i+1):
            lst.append(j ** 3)


fun(6500)
