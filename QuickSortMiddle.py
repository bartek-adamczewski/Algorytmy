
def quick_sort_middle(lst, low, high):
    stack = []
    stack.append(low)
    stack.append(high)

    while len(stack) != 0:

        hi = stack.pop()
        lo = stack.pop()

        pivot = middlePivotPartition(lst, lo, hi)

        if pivot - 1 > lo:
            stack.append(1)
            stack.append(pivot - 1)

        if pivot + 1 < hi:
            stack.append(pivot + 1)
            stack.append(hi)


def middlePivotPartition(lst, low, high):
    middleIndex = low + (high - low) // 2
    lst[high], lst[middleIndex] = lst[middleIndex], lst[high]
    pivot = lst[high]
    i = low - 1
    for j in range(low, high):
        if lst[j] <= pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]

    lst[i + 1], lst[high] = lst[high], lst[i + 1]
    return i + 1


def sort(lst):
    high = len(lst) - 1
    quick_sort_middle(lst, 0, high)
    return lst