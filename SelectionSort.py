from typing import List


def selection_sort(data: List[int])-> List[int]:
	for i in range(len(data)):
		minimum_index = find_min(data[i:]) + i
		data[i], data[minimum_index] = data[minimum_index], data[i]

	return data

def find_min(data: List[int]) -> int:
	min_val, min_index = data[0], 0
	for i, val in enumerate(data):
		if val < min_val:
			min_val, min_index = val, i
	return min_index