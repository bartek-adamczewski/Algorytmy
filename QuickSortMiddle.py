
def quick_sort(lst, start, end):
    if start < end:
        pivot = partition(lst, start, end)
        quick_sort(lst, start, pivot - 1)
        quick_sort(lst, pivot + 1, end)
    return lst


def partition(lst, start, end):
    pivot = lst[start]
    left = start + 1
    right = end
    done = False
    while not done:
        while left <= right and lst[left] <= pivot:
            left = left + 1
        while lst[right] >= pivot and right >= left:
            right = right - 1
        if right < left:
            done = True
        else:
            temp = lst[left]
            lst[left] = lst[right]
            lst[right] = temp
    temp = lst[start]
    lst[start] = lst[right]
    lst[right] = temp
    return right


def sort(lst):
    return quick_sort(lst, 0, len(lst) - 1)

