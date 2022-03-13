from typing import List


def quick_sort(dane: List[int], low: int = 0, high: int = None) -> List[int]:
    if high is None:
        high = len(dane) - 1

    if low >= high or low < 0:
        return dane

    new_pivot = partition(dane, low, high)

    quick_sort(dane, low, new_pivot - 1)
    quick_sort(dane, new_pivot + 1, high)

    return dane


def partition(dane: List[int], low: int, high: int) -> int:
    pivot = dane[high]  # ostatni element jako pivot
    i = low - 1

    for j in range(low, high):
        if dane[j] <= pivot:
            i += 1
            dane[i], dane[j] = dane[j], dane[i]
    i += 1
    dane[i], dane[high] = dane[high], dane[i]
    return i
