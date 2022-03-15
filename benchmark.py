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
    # data_steps = [1, 5, 10, 50, 100, 500, 1000, 5000, 7500, 10000]
    # data = list(range(1, data_steps[-1]))
    # random.shuffle(data)
    #
    #
    # def benchmark_sort(name: str, func, number_of_runs: int):
    #     for n in data_steps:
    #         time_taken = Timer(lambda: func(data[:n-1].copy())).timeit(number=number_of_runs)
    #         print(f"{name}: ({n} elementów): {time_taken/number_of_runs}s")
    #
    # number_of_runs = 1
    # print("Algorytmy proste: ")
    # benchmark_sort("bubble sort", bubble_sort, number_of_runs)
    # benchmark_sort("insertion sort", insertion_sort, number_of_runs)
    # benchmark_sort("selection sort", selection_sort, number_of_runs)
    #
    # number_of_runs = 50
    # print("Algorytmy złożone: ")
    # benchmark_sort("merge sort", merge_sort, number_of_runs)
    # benchmark_sort("heap sort", heap_sort, number_of_runs)
    # benchmark_sort("quick sort middle", quick_sort_middle, number_of_runs)
    # benchmark_sort("quick sort last", quick_sort_last, number_of_runs)
    # benchmark_sort("counting sort", count_sort, number_of_runs)
    #
    # ### Sekcja 2
    # data.sort()
    #
    data_steps = [50, 100, 200, 300, 500, 750, 1000, 2500, 5000, 7500]
    # number_of_runs = 100
    # benchmark_sort("insertion sort (sorted data)", insertion_sort, number_of_runs)
    # benchmark_sort("quick sort middle (sorted data)", quick_sort_middle, number_of_runs)
    # number_of_runs = 1
    # benchmark_sort("quick sort last (sorted data)", quick_sort_last, number_of_runs)

    ## Sekcja 3
    print("Rozkład danych a) [1, 100*n]")
    for n in data_steps:
        data = list(range(1, 100*n))
        random.shuffle(data)
        number_of_runs = 10
        time_taken = Timer(lambda: quick_sort_middle(data[:n - 1].copy())).timeit(number=number_of_runs)
        print(f"quick sort middle: ({n} elementów): {time_taken / number_of_runs}s")

    for n in data_steps:
        data = list(range(1, 100 * n))
        random.shuffle(data)
        number_of_runs = 10
        time_taken = Timer(lambda: count_sort(data[:n - 1].copy())).timeit(number=number_of_runs)
        print(f"counting sort: ({n} elementów): {time_taken / number_of_runs}s")

    print("Rozkład danych b) [1, 0.01*n]")
    for n in data_steps:
        data = list(range(1, int(0.01*n)))
        random.shuffle(data)
        number_of_runs = 10
        time_taken = Timer(lambda: quick_sort_middle(data[:n - 1].copy())).timeit(number=number_of_runs)
        print(f"quick sort middle: ({n} elementów): {time_taken / number_of_runs}s")

    for n in data_steps:
        data = list(range(1, int(0.01 * n)))
        random.shuffle(data)
        number_of_runs = 10
        time_taken = Timer(lambda: count_sort(data[:n - 1].copy())).timeit(number=number_of_runs)
        print(f"counting sort: ({n} elementów): {time_taken / number_of_runs}s")


if __name__ == "__main__":
    benchmark()
