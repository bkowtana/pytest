from multiprocessing import Pool
import threading
import time



def test(numb):
    time.sleep(0.1)
    # print("Worker no: {}".format(numb))
    return()

def T(numb):
    threads = []
    MaxP = numb
    i = 0
    start = time.time()
    while i < Tlist.__len__():
        if threading.active_count() <= MaxP:
            thread = threading.Thread(target=test, args=(Tlist[i],))
            thread.start()
            threads.append(thread)
            i += 1
    for t in threads:
        t.join()
    totaltime = time.time() - start
    return(totaltime)

def P(numb):
    start = time.time()
    with Pool(numb) as p:
        p.map(test, Tlist)
    totaltime = time.time() - start
    return(totaltime)

if __name__ == "__main__":
    Tlist = range(10000,10200)
    print("Thread time  : {}".format(T(10)))
    print("Pool time    : {}".format(P(10)))


