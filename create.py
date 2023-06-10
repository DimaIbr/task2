from random import randint
ves=5000
file_handler = open("endian.bin", "wb")


for i in range(ves):
    n=randint(0,2**32-1)
    if i< 20:
        print(n)
    file_handler.write(int(n).to_bytes(4, "big"))
    file_handler.write(b'\n')

file_handler.close()