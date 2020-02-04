#equivalent de range

def gen_fibo(n):
    a,b = 0,1
    if n == 0 or n == 1:
        yield n
    for i in range(2,n+1):
        a,b = b, a+b
        yield b

for i in gen_fibo(10):
    print(i)

def mon_range(n):
    i = 0
    while i < n:
        yield i
        i += 1

for i in mon_range(10):
    print(i)