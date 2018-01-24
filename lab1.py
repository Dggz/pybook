import threading
import time

import numpy as np

n=int(input("First matrix rows: "))
k=int(input("Columns for first, rows for second: "))
m=int(input("Second matrix columns: "))

a=np.random.randint(10,size=(n,k))
b=np.random.randint(10,size=(k,m))

res=np.zeros((n,m))

print(a.shape)

nworkers=int(input("Give number of workers: "))

def matrix_product(row, end):
    global a
    global b
    res[row:end]=np.dot(a[row:end], b)


start=time.time()
matrix_product(0,n)
end=time.time()
print("1 thread: %s" % str(end-start))


start=time.time()
threads = []

for i in range(0, n,int(n/nworkers)):
    th=threading.Thread(
        target=matrix_product,
        args=(i, int(min(i + n / nworkers + 1, n))))
    threads.append(th)
    th.start()

for th in threads:
    th.join()

end=time.time()
print(str(nworkers)+" threads: %s" % str(end-start))




