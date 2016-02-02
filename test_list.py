import timeit

start = timeit.default_timer()

a = []

for _ in range(5000000):
    a.append(_)

stop = timeit.default_timer()

print(stop-start)
