import timeit

start = timeit.default_timer()

a = ()

for _ in range(50000):
    a += (_,)

stop = timeit.default_timer()

print(stop-start)
