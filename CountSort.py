def count_sort(lst):
    values = [0 for i in range(max(lst) + 1)]

    for number in lst:
        values[number] += 1

    for index in range(1, len(values)):
        values[index] = values[index - 1] + values[index]

    answer = [0 for loop in range(len(lst))]
    for value in lst:
        index = values[value] - 1
        answer[index] = value
        values[value] -= 1

    return answer






