from typing import List

from matplotlib import pyplot as plt

elements = [1, 5, 10, 50, 100]

def read_sort(name: str, n: int) -> List[float]:
    with open("wyniki.txt") as f:
        for line in f:
            if line.split(":")[0] != name:
                continue
            if "002:" in line:
                break
            skip = len(name.split(" "))
            res = [float(i[:-1]) for i in line.strip().split(" ")[skip:]][:n + 1]
            return res


bubble_y = read_sort("bubble sort", 4)
insertion_y = read_sort("insertion sort", 4)
selection_y = read_sort("selection sort", 4)
merge_y = read_sort("merge sort", 4)
heap_y = read_sort("heap sort", 4)
quick_middle_y = read_sort("quick sort middle", 4)
quick_last_y = read_sort("quick sort last", 4)
counting_y = read_sort("counting sort", 4)

plt.xlabel('Ilość elementów')
plt.ylabel('Czas wykonania(sekundy)')
plt.title('Wydajność czasowa algorytmów')

plt.plot(elements, bubble_y)
plt.plot(elements, insertion_y)
plt.plot(elements, selection_y)
plt.plot(elements, merge_y)
plt.plot(elements, heap_y)
plt.plot(elements, quick_middle_y)
plt.plot(elements, quick_last_y)
plt.plot(elements, counting_y)

plt.legend(['Bubble Sort', 'Insertion Sort', 'Selection Sort', 'Merge Sort', 'Heap Sort', 'Quick Sort Middle',
            'Quick Sort Last', 'Counting Sort'])

if "__main__" == __name__:
    plt.show()
