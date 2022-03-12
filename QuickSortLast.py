
def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    else:
        pivot = lst.pop()

    lower = []
    greater = []

    for number in lst:
        if number > pivot:
            greater.append(number)
        else:
            lower.append(number)
    return quick_sort(lower) + [pivot] + quick_sort(greater)