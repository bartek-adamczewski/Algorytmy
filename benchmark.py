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
    with open("wyniki.txt", "w") as f:
        data_steps = [1, 5, 10, 50, 100, 500, 1000, 5000, 7500, 10000]
        data = list(range(1, data_steps[-1]))
        random.shuffle(data)

        f.write("001:\n")
        f.write(", ".join([str(i) for i in data_steps]) + "\n")

        def benchmark_sort(name: str, func, number_of_runs: int):
            res = []
            for n in data_steps:
                time_taken = Timer(lambda: func(data[:n-1].copy())).timeit(number=number_of_runs)
                print(f"{name}: ({n} elementów): {time_taken/number_of_runs}s")
                res.append(time_taken/number_of_runs)
            f.write(f"{name}: " + ", ".join([str(i) for i in res])+",\n")

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

        # ### Sekcja 2
        data.sort()

        f.write("002:\n")
        f.write(", ".join([str(i) for i in data_steps]) + "\n")
        data_steps = [50, 100, 200, 300, 500, 750, 1000, 2500, 5000, 7500]
        number_of_runs = 100
        benchmark_sort("insertion sort (sorted data)", insertion_sort, number_of_runs)
        benchmark_sort("quick sort middle (sorted data)", quick_sort_middle, number_of_runs)
        number_of_runs = 1
        benchmark_sort("quick sort last (sorted data)", quick_sort_last, number_of_runs)

        ## Sekcja 3
        f.write("003:\n")
        f.write(", ".join([str(i) for i in data_steps]) + "\n")
        print("Rozkład danych a) [1, 100*n]")
        res = []
        for n in data_steps:
            data = list(range(1, 100*n))
            random.shuffle(data)
            number_of_runs = 10
            time_taken = Timer(lambda: quick_sort_middle(data[:n - 1].copy())).timeit(number=number_of_runs)
            print(f"quick sort middle: ({n} elementów): {time_taken / number_of_runs}s")
            res.append(time_taken/number_of_runs)
        f.write(f"quick sort middle (a): " + ", ".join([str(i) for i in res])+",\n")

        res = []
        for n in data_steps:
            data = list(range(1, 100 * n))
            random.shuffle(data)
            number_of_runs = 10
            time_taken = Timer(lambda: count_sort(data[:n - 1].copy())).timeit(number=number_of_runs)
            print(f"counting sort: ({n} elementów): {time_taken / number_of_runs}s")
            res.append(time_taken / number_of_runs)
        f.write(f"counting sort (a): " + ", ".join([str(i) for i in res])+",\n")

        res = []
        print("Rozkład danych b) [1, 0.01*n]")
        for n in data_steps:
            data = list(range(1, int(0.01*n)))
            random.shuffle(data)
            number_of_runs = 10
            time_taken = Timer(lambda: quick_sort_middle(data[:n - 1].copy())).timeit(number=number_of_runs)
            print(f"quick sort middle: ({n} elementów): {time_taken / number_of_runs}s")
            res.append(time_taken / number_of_runs)
        f.write(f"quick sort middle (b): " + ", ".join([str(i) for i in res])+",\n")

        res = []
        for n in data_steps:
            data = list(range(1, int(0.01 * n)))
            random.shuffle(data)
            number_of_runs = 10
            time_taken = Timer(lambda: count_sort(data[:n - 1].copy())).timeit(number=number_of_runs)
            print(f"counting sort: ({n} elementów): {time_taken / number_of_runs}s")
            res.append(time_taken / number_of_runs)
        f.write(f"counting sort (b): " + ", ".join([str(i) for i in res])+",\n")


if __name__ == "__main__":
    benchmark()
