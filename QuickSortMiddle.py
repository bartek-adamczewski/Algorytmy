from typing import List


def quick_sort(dane: List[int], low: int = 0, high: int = None) -> List[int]:
    if high is None:
        high = len(dane) - 1

    if low >= 0 and high >= 0 and low < high:
        new_pivot = partition(dane, low, high)
        quick_sort(dane, low, new_pivot)
        quick_sort(dane, new_pivot + 1, high)

    return dane


def partition(dane: List[int], low: int, high: int) -> int:
    pivot = dane[(high+low)//2]  # środkowy element jako pivot
    left_index = low
    right_index = high

    while True:
        while dane[left_index] < pivot:
            left_index += 1
        while dane[right_index] > pivot:
            right_index -= 1
        if left_index >= right_index:
            return right_index
        dane[left_index], dane[right_index] = dane[right_index], dane[left_index]