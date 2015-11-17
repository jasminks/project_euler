cache = {}
def fibonacci(n):
    cache[n] = cache.get(n, 0) or (n <= 1 and 1 or fibonacci(n-1) + fibonacci(n-2))
    return cache[n]
n = 0
i = 0
while fibonacci(i) <= 4000000:
     if not fibonacci(i) % 2: n = n + fibonacci(i)
     i = i + 1

print n
