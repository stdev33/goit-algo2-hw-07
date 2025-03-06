import timeit
import matplotlib.pyplot as plt
from functools import lru_cache
from SplayTree import SplayTree


# Calculate Fibonacci numbers using LRU Cache
@lru_cache(maxsize=None)
def fibonacci_lru(n):
    if n <= 1:
        return n
    return fibonacci_lru(n - 1) + fibonacci_lru(n - 2)


# Calculate Fibonacci numbers using Splay Tree
def fibonacci_splay(n, tree):
    if n <= 1:
        return n
    result = tree.find(n)
    if result is not None:
        return result
    result = fibonacci_splay(n - 1, tree) + fibonacci_splay(n - 2, tree)
    tree.insert(n, result)
    return result


fibonacci_numbers = list(range(0, 951, 50))  # 0, 50, 100, ..., 950
lru_times = []
splay_times = []

# Performing tests
for n in fibonacci_numbers:
    # Measuring time for LRU Cache usage
    lru_time = timeit.timeit(lambda: fibonacci_lru(n), number=5) / 5
    lru_times.append(lru_time)

    # Measuring time for Splay Tree usage
    tree = SplayTree()
    splay_time = timeit.timeit(lambda: fibonacci_splay(n, tree), number=5) / 5
    splay_times.append(splay_time)


print("\nРезультати порівняння продуктивності:")
print(f"{'n':<10}{'LRU Cache Time (s)':<25}{'Splay Tree Time (s)':<25}")
print("-" * 60)
for i, n in enumerate(fibonacci_numbers):
    print(f"{n:<10}{lru_times[i]:<25.8f}{splay_times[i]:<25.8f}")


plt.figure(figsize=(10, 6))
plt.plot(fibonacci_numbers, lru_times, marker="o", linestyle="-", label="LRU Cache")
plt.plot(fibonacci_numbers, splay_times, marker="x", linestyle="-", label="Splay Tree")
plt.xlabel("Число Фібоначчі (n)")
plt.ylabel("Середній час виконання (секунди)")
plt.title("Порівняння часу виконання для LRU Cache та Splay Tree")
plt.legend()
plt.grid(True)
plt.savefig("plot.png")
plt.show()
