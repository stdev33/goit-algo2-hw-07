import random
import time
from LRUCache import LRUCache


ARRAY_SIZE = 100_000
QUERY_COUNT = 50_000
CACHE_SIZE = 1000


array = [random.randint(1, 1000) for _ in range(ARRAY_SIZE)]


queries = []
for _ in range(QUERY_COUNT):
    if random.random() < 0.5:
        L = random.randint(0, ARRAY_SIZE - 1)
        R = random.randint(L, ARRAY_SIZE - 1)
        queries.append(("Range", L, R))
    else:
        index = random.randint(0, ARRAY_SIZE - 1)
        value = random.randint(1, 1000)
        queries.append(("Update", index, value))


def range_sum_no_cache(L, R):
    return sum(array[L : R + 1])


def update_no_cache(index, value):
    array[index] = value


cache = LRUCache(CACHE_SIZE)


def range_sum_with_cache(L, R):
    cached_result = cache.get((L, R))
    if cached_result is not None:
        return cached_result

    result = sum(array[L : R + 1])  # O(N)
    cache.put((L, R), result)
    return result


def update_with_cache(index, value):
    array[index] = value
    cache.invalidate_range(index)


start_time = time.time()
for query in queries:
    if query[0] == "Range":
        range_sum_no_cache(query[1], query[2])
    elif query[0] == "Update":
        update_no_cache(query[1], query[2])
time_no_cache = time.time() - start_time


start_time = time.time()
for query in queries:
    if query[0] == "Range":
        range_sum_with_cache(query[1], query[2])
    elif query[0] == "Update":
        update_with_cache(query[1], query[2])
time_with_cache = time.time() - start_time


print(f"Час виконання без кешування: {time_no_cache:.2f} секунд")
print(f"Час виконання з LRU-кешем: {time_with_cache:.2f} секунд")
