#!/usr/bin/python

import time
from multiprocessing import Process, Value, Lock
import md5

# startValue = "abcdef"
startValue = "yzbqklnj"

def func(hashAddition, lock, finished):
    while finished.value != 1:
        with lock:
            hashAddition.value += 1
            i = hashAddition.value
        md5hash = md5.new("%s%i" % (startValue, i)).hexdigest()
        if md5hash[:6] == "000000":
            print "%s%i %s" % (startValue, i, md5hash[:5])
            finished.value = 1

if __name__ == '__main__':
    v = Value('i', 0)
    finished = Value('i', 0)
    lock = Lock()
    procs = [Process(target=func, args=(v, lock, finished)) for i in range(2)]

    for p in procs: p.start()
    for p in procs: p.join()

    print v.value
