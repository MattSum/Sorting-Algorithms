# -*- coding: utf-8 -*-
"""
Quick sort algorithm implemented in Python3
Reference: https://en.wikipedia.org/wiki/Quicksort
"""


def quick_sort(data: list, beg: int, end: int) -> None:
    if beg < end:
        p = partition(data, beg, end)
        quick_sort(data, beg, p-1)
        quick_sort(data, p+1, end)


def partition(data: list, beg: int, end: int) -> int:
    pivot = data[end]
    i = beg
    for j in range(beg, end):
        if data[j] < pivot:
            data[i], data[j] = data[j], data[i]
            i = i + 1
    data[i], data[end] = data[end], data[i]
    return i


if __name__ == "__main__":
    arr = [51, 23, 56, 19, 4]
    quick_sort(arr, 0, len(arr)-1)
    print(arr)