from typing import List

from matplotlib import pyplot as plt

elements = [500, 1000, 5000, 7500, 10000]

def read_sort(name: str, start: int) -> List[float]:
    with open("wyniki.txt") as f:
        for line in f:
            if line.split(":")[0] != name:
                continue
            if "002:" in line:
                break
            skip = len(name.split(" "))
            res = [float(i[:-1]) for i in line.strip().split(" ")[skip:]][start:]
            return res

merge_y = read_sort("merge sort", 5)
heap_y = read_sort("heap sort", 5)
quick_middle_y = read_sort("quick sort middle", 5)
quick_last_y = read_sort("quick sort last", 5)
counting_y = read_sort("counting sort", 5)

plt.xlabel('Ilość elementów')
plt.ylabel('Czas wykonania(sekundy)')
plt.title('Wydajność czasowa algorytmów')

plt.plot(elements, merge_y)
plt.plot(elements, heap_y)
plt.plot(elements, quick_middle_y)
plt.plot(elements, quick_last_y)
plt.plot(elements, counting_y)

plt.legend(['Merge Sort', 'Heap Sort', 'Quick Sort Middle', 'Quick Sort Last', 'Counting Sort'])

plt.show()

