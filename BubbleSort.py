from typing import List


def bubble_sort(data: List[int]) -> List[int]:
	for _ in data:
		for i in range(1, len(data)):
			if data[i-1] > data[i]:
				data[i-1], data[i] = data[i], data[i-1]

	return data