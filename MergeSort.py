def merge_sort(lst):
    left, right = lst[:len(lst)//2], lst[len(lst)//2:]     # Dzielenie głównej listy na dwie

    merge_sort(right)
    merge_sort(left)

    l_ind, r_ind, main_ind = 0, 0, 0
