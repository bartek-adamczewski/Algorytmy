def merge_sort(lst):
    if len(lst) > 1:
        left, right = lst[:len(lst)//2], lst[len(lst)//2:]     # Dzielenie głównej listy na dwie

        merge_sort(left)                                       # Rekurencja
        merge_sort(right)

        l_ind = 0
        r_ind = 0
        main_ind = 0

        while l_ind < len(left) and r_ind < len(right):        # dodawanie mniejszej wartości do głównej listy
            if left[l_ind] < right[r_ind]:
                lst[main_ind] = left[l_ind]
                l_ind += 1
            else:
                lst[main_ind] = right[r_ind]
                r_ind += 1
            main_ind += 1

        while l_ind < len(left):                               # gdy dodano wszystkie elementy z jednej z dwóch list
            lst[main_ind] = left[l_ind]
            l_ind += 1
            main_ind += 1

        while r_ind < len(right):
            lst[main_ind] = right[r_ind]
            r_ind += 1
            main_ind += 1
