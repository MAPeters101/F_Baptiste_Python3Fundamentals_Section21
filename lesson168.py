from time import perf_counter, sleep
start = perf_counter()
print(start)
end = perf_counter()
print(end)
print('-'*80)

start = perf_counter()
sleep(1)
#sleep(3)
end = perf_counter()
elapsed = end - start
print(elapsed)
print('-'*80)

from time import gmtime
print(gmtime(1_000_000_000))
print(gmtime(0))
#print(gmtime(-1_000_000_000))
print(gmtime(-43_200))


