from typing import List

from matplotlib import pyplot as plt

elements = [50, 100, 200, 300, 500, 750, 1000, 2500, 5000, 7500]

def read_sort(name: str, start: int = 0) -> List[float]:
    start = False
    with open("wyniki.txt") as f:
        for line in f:
            if "003:" in line:
                start = True
                continue
            if start and line.split(":")[0] != name:
                continue
            if start:
                skip = len(name.split(" "))
                res = [float(i[:-1]) for i in line.strip().split(" ")[skip:]]
                return res

quick_sort_middle_a_y = read_sort("quick sort middle (a)", 5)
quick_sort_middle_b_y = read_sort("quick sort middle (b)", 5)
counting_sort_a_y = read_sort("counting sort (a)", 5)
counting_sort_b_y = read_sort("counting sort (b)", 5)

plt.xlabel('Ilość elementów')
plt.ylabel('Czas wykonania(sekundy)')
plt.title('Wydajność czasowa algorytmów')

plt.plot(elements, quick_sort_middle_a_y)
plt.plot(elements, counting_sort_a_y)
plt.plot(elements, quick_sort_middle_b_y)
plt.plot(elements, counting_sort_b_y)

plt.legend(["QuickSort [1, 100*n]", "Counting Sort [1, 100*n]", "QuickSort [1, 0.01*n]", "Counting Sort [1, 0.01*n]"])

plt.show()

