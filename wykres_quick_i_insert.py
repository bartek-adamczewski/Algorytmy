from typing import List

from matplotlib import pyplot as plt

elements = [50, 100, 200, 300, 500, 750, 1000, 2500, 5000, 7500]

def read_sort(name: str, start: int = 0) -> List[float]:
    start = False
    with open("wyniki.txt") as f:
        for line in f:
            if "002:" in line:
                start = True
                continue
            if "003:" in line:
                break
            if start and line.split(":")[0] != name:
                continue
            if start:
                skip = len(name.split(" "))
                res = [float(i[:-1]) for i in line.strip().split(" ")[skip:]]
                return res

insertion_y = read_sort("insertion sort (sorted data)", 5)
unsorted_q_m_y = read_sort("quick sort middle", 5)
unsorted_q_e_y = read_sort("quick sort last", 5)
unsorted_insertion_y = read_sort("insertion sort", 5)
quick_sort_middle_y = read_sort("quick sort middle (sorted data)", 5)
quick_sort_last_y = read_sort("quick sort last (sorted data)", 5)

plt.xlabel('Ilość elementów')
plt.ylabel('Czas wykonania(sekundy)')
plt.title('Wydajność czasowa algorytmów')

plt.plot(elements, unsorted_q_m_y)
plt.plot(elements, unsorted_q_e_y)
# plt.plot(elements, unsorted_insertion_y)
plt.plot(elements, insertion_y)
plt.plot(elements, quick_sort_middle_y)
# plt.plot(elements, quick_sort_last_y)

plt.legend(["QuickSort Middle", "QuickSort Last", "Insertion Sort", "Insertion Sort (posortowane)", "QuickSort Middle (posortowane)", "QuickSort Last (posortowane)"])
# plt.legend(["QuickSort Middle", "QuickSort Last", "Insertion Sort (posortowane)", "QuickSort Middle (posortowane)"])

plt.show()

