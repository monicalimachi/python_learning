def fibo_y(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    yield a

for item in range(10):
    for i in fibo_y(item):
        print(i)