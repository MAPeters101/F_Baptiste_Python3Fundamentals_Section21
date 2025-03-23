from time import perf_counter, sleep
start = perf_counter()
print(start)
end = perf_counter()
print(end)
print('-'*80)

start = perf_counter()
sleep(.1)
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
print('='*80)

# import time
# print(time.time())
from time import time
print(time())
print(gmtime(time()))
print('-'*80)

current = gmtime(time())
print(current[0])
print(current.tm_year)
print(current[0:2])
print('.'*80)

now = time()
tomorrow = now + (24 * 60 * 60)
print(gmtime(now))
print(gmtime(tomorrow))
print(tomorrow - now)
print('-'*80)

from calendar import timegm
now_epoch = time()
print(now_epoch)
now_struct = gmtime(now_epoch)
print(now_struct)
print(timegm(now_struct))


