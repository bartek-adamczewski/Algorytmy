import random
from timeit import Timer

from BubbleSort import bubble_sort
from CountSort import count_sort
from HeapSort import heap_sort
from InsertionSort import insertion_sort
from MergeSort import merge_sort
from QuickSortMiddle import quick_sort as quick_sort_middle
from QuickSortLast import quick_sort as quick_sort_last
from SelectionSort import selection_sort


def benchmark():
    data_steps = [1, 5, 10, 50, 100, 500, 1000, 5000, 7500, 10000]
    data = list(range(1, data_steps[-1]))
    random.shuffle(data)


    def benchmark_sort(name: str, func, number_of_runs: int):
        for n in data_steps:
            time_taken = Timer(lambda: func(data[:n-1].copy())).timeit(number=number_of_runs)
            print(f"{name}: ({n} elementów): {time_taken/number_of_runs}s")

    number_of_runs = 1
    print("Algorytmy proste: ")
    benchmark_sort("bubble sort", bubble_sort, number_of_runs)
    benchmark_sort("insertion sort", insertion_sort, number_of_runs)
    benchmark_sort("selection sort", selection_sort, number_of_runs)

    number_of_runs = 50
    print("Algorytmy złożone: ")
    benchmark_sort("merge sort", merge_sort, number_of_runs)
    benchmark_sort("heap sort", heap_sort, number_of_runs)
    benchmark_sort("quick sort middle", quick_sort_middle, number_of_runs)
    benchmark_sort("quick sort last", quick_sort_last, number_of_runs)
    benchmark_sort("counting sort", count_sort, number_of_runs)



if __name__ == "__main__":
    benchmark()
