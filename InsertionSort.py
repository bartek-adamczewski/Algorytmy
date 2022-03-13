from typing import List


def insertion_sort(data: List[int]) -> List[int]:
	for i in range(1, len(data)):
		for j in range(i, 0, -1):
			if data[j] < data[j-1]:
				data[j], data[j-1] = data[j-1], data[j]
			else:
				break

	return data