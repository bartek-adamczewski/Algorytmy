from typing import List
from unittest import TestCase
import random

from BubbleSort import bubble_sort
from CountSort import count_sort
from HeapSort import heap_sort
from InsertionSort import insertion_sort
from MergeSort import merge_sort
from QuickSortLast import quick_sort
from QuickSortMiddle import quick_sort as quick_sort_middle
from SelectionSort import selection_sort


def get_test_data(n: int) -> List[int]:
    data = list(range(1, n))
    random.shuffle(data)
    return data


def get_sorted(data: List[int]) -> List[int]:
    sorted = data.copy()
    sorted.sort()
    return sorted


class TestRandomData(TestCase):
    data = get_test_data(100)
    sorted = get_sorted(data)

    def test_bubble_sort(self):
        res = bubble_sort(self.data.copy())
        self.assertEqual(self.sorted, res)

    def test_insertion_sort(self):
        res = insertion_sort(self.data.copy())
        self.assertEqual(self.sorted, res)

    def test_selection_sort(self):
        res = selection_sort(self.data.copy())
        self.assertEqual(self.sorted, res)

    def test_count_sort(self):
        res = count_sort(self.data.copy())
        self.assertEqual(self.sorted, res)

    def test_merge_sort(self):
        copy = self.data.copy()
        merge_sort(copy)
        self.assertEqual(self.sorted, copy)

    def test_quick_sort_last(self):
        res = quick_sort(self.data.copy())
        self.assertEqual(self.sorted, res)

    def test_quick_sort_middle(self):
        res = quick_sort_middle(self.data.copy())
        self.assertEqual(self.sorted, res)

    def test_heap_sort(self):
        copy = self.data.copy()
        heap_sort(copy, len(copy))
        self.assertEqual(self.sorted, copy)

class TestSingleElement(TestCase):
    data = get_test_data(1)
    sorted = get_sorted(data)

    def test_bubble_sort(self):
        res = bubble_sort(self.data.copy())
        self.assertEqual(self.sorted, res)

    def test_insertion_sort(self):
        res = insertion_sort(self.data.copy())
        self.assertEqual(self.sorted, res)

    def test_selection_sort(self):
        res = selection_sort(self.data.copy())
        self.assertEqual(self.sorted, res)

    def test_count_sort(self):
        res = count_sort(self.data.copy())
        self.assertEqual(self.sorted, res)

    def test_merge_sort(self):
        copy = self.data.copy()
        merge_sort(copy)
        self.assertEqual(self.sorted, copy)

    def test_quick_sort_last(self):
        res = quick_sort(self.data.copy())
        self.assertEqual(self.sorted, res)

    def test_quick_sort_middle(self):
        res = quick_sort_middle(self.data.copy())
        self.assertEqual(self.sorted, res)

    def test_heap_sort(self):
        copy = self.data.copy()
        heap_sort(copy, len(copy))
        self.assertEqual(self.sorted, copy)

class TestEmptyList(TestCase):
    data = []
    sorted = []

    def test_bubble_sort(self):
        res = bubble_sort(self.data.copy())
        self.assertEqual(self.sorted, res)

    def test_insertion_sort(self):
        res = insertion_sort(self.data.copy())
        self.assertEqual(self.sorted, res)

    def test_selection_sort(self):
        res = selection_sort(self.data.copy())
        self.assertEqual(self.sorted, res)

    def test_count_sort(self):
        res = count_sort(self.data.copy())
        self.assertEqual(self.sorted, res)

    def test_merge_sort(self):
        copy = self.data.copy()
        merge_sort(copy)
        self.assertEqual(self.sorted, copy)

    def test_quick_sort_last(self):
        res = quick_sort(self.data.copy())
        self.assertEqual(self.sorted, res)

    def test_quick_sort_middle(self):
        res = quick_sort_middle(self.data.copy())
        self.assertEqual(self.sorted, res)

    def test_heap_sort(self):
        copy = self.data.copy()
        heap_sort(copy, len(copy))
