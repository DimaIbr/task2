
from multiprocessing import Process, Lock
from multiprocessing.sharedctypes import Value
import mmap
import time



def factor(n):
    Ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            Ans.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        Ans.append(n)
    return len(Ans)

def max_factor(start,endd,Ans):
    num_factor = 0
    with open('endian.bin', "rb") as file, mmap.mmap(file.fileno(), length=0, access=mmap.ACCESS_READ) as buf:
        for i in range(start, endd):
            n=int.from_bytes(buf[i*5:i*5+4],'big')
            num_factor+=factor(n)
    Ans.value+=num_factor


if __name__ == '__main__':
    start = time.time()
    ves=5000
    lock = Lock()
    Ans = Value('i',0,lock=lock)
    p = Process(target=max_factor, args=(0,int(ves/2),Ans))
    p2=Process(target=max_factor, args=(int(ves/2), ves,Ans))
    #p2 = Process(target=factor, args=(temp_ves,))
    p.start()
    p2.start()
    p.join()
    p2.join()
    endd = time.time() - start
    print(Ans.value)
    print(endd)