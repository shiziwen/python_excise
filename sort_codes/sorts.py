# !/user/bin/python

def bubble_sort(array):
    n = len(n)
    for i in range(n):
        for j in range(1, n-i):
            if array[j-1] > array[j]:
                array[j-1], array[j] = array[j], array[j-1]
    return array


def select_sort(array):
    n = len(array)
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if array[j] < array[j-1]:
                min = j
        array[min], array[i] = array[i], array[min]
    return array


def insert_sort(ary):
    n = len(ary)
    for i in range(1, n):
        if ary[i] < ary[i-1]:
            temp = ary[i]
            index = i
            for j in range(i-1, -1, -1):
                if ary[j] > temp:
                    ary[j+1] = ary[j]
                    index = j
                else:
                    break
        ary[index] = temp
    return ary


def quick_sort(ary):
    qsort(ary, 0, len(ary) - 1)

def qsort(ary, left, right):
    if left >= right:
        return ary
    key = ary[left]
    lp = left
    rp = right
    while lp < rp:
        while ary[rp] >= key and lp < rp:
            rp -= 1
        while ary[lp] <= key and lp < rp:
            lp += 1
        ary[lp], ary[rp] = ary[rp], ary[lp]
    ary[left], ary[lp] = ary[lp], ary[rp]
    qsort(ary, left, lp - 1)
    qsort(ary, rp + 1, right)
    return ary

