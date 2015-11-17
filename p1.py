N = 1000
def fibonacci():
    cache[n] = cache.get(n, 0) or (n <= 1 and 1 or fib(n-1) + fib(n-2))
    return cache[n]
n = 0
i = 0
while fib(i) <= 4000000:
     if not fib(i) % 2: n = n + fib(i)
     i = i + 1

print n
