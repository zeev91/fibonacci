def fibonacci(n):
        a = b = 1
        for i in range(n):
            yield a 
            a, b = b, a + b

print(sum(fibonacci(10000)))
