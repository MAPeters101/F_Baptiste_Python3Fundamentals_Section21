from time import perf_counter, sleep
start = perf_counter()
print(start)
end = perf_counter()
print(end)
print('-'*80)

start = perf_counter()
sleep(3)
end = perf_counter()
elapsed = end - start
print(elapsed)
print('-'*80)




