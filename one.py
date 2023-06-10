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

start=time.time()
num_factor=0
with open('endian.bin', "rb") as file:
    for i in range(5000):
        n=int.from_bytes(file.read(4),'big')
        file.read(1)
        num_factor += factor(n)


endd=time.time()-start
print(num_factor)
print(endd)