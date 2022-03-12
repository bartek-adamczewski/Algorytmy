
def swap_in_heap(lst, n, i):
    largest = i                 # indeks rodzica
    lchild = i*2 + 1            # indeks lewego dziecka
    rchild = i*2 + 2            # indeks prawego dziecka

    if lchild < n and lst[lchild] > lst[largest]:       # czy lewe dziecko należy do listy i czy jest większe od rodzica
        largest = lchild
    if rchild < n and lst[rchild] > lst[largest]:       # czy lewe dziecko należy do listy i czy jest większe od rodzica
        largest = rchild
    if largest != i:                                    # zamiana dziecka z rodzicem jeśli ma większą wartość
        lst[largest], lst[i] = lst[i], lst[largest]
        swap_in_heap(lst, n, largest)

def heap_sort(lst, n):
    for i in range(n//2 - 1, -1, -1):        # znajduje największą wartość listy
        swap_in_heap(lst, n, i)

    for i in range(n-1, 0, -1):              # znajduje największy element i przenosi go do części posortowanej
        lst[i], lst[0] = lst[0], lst[i]
        swap_in_heap(lst, i, 0)




