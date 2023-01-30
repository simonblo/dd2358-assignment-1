import numpy
import time
import timeit

def checktick(n, fn):
    t = []
    for i in range(n):
        t1 = fn()
        t2 = fn()
        while (t2 - t1) < 1e-16:
            t2 = fn()
        t.append(t2)
    return numpy.diff(t).min()

if __name__ == "__main__":
    print(f"{checktick(200, time.time):.20f}")
    print(f"{checktick(200, timeit.default_timer):.20f}")
    print(f"{checktick(200, time.time_ns)*1e-9:.20f}")
