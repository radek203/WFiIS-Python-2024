import random
import sys
import time

sys.path.append('build/lib.linux-x86_64-cpython-311')

import mod


def sortuj(arr):
    for i in range(1, len(arr)):
        elem = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > elem:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = elem
    return arr


print(mod.met(1, 2))
print(mod.met(1, 2, 5))
print(mod.met(1, 2, 5, [2, 3, 4]))

for size in [10, 100, 1000, 10000]:
    print("Dla rozmiaru:", size)
    arr = [random.randint(0, size) for _ in range(size)]
    start = time.time()
    mod.sortuj(arr)
    print("C:", time.time() - start)
    start = time.time()
    sortuj(arr)
    print("Python:", time.time() - start)
    start = time.time()
    arr.sort()
    print("Python wbudowana:", time.time() - start)

print(mod.mnozenie([[2, 3], [4, 5]], [[4, 5], [1, 2]]))
