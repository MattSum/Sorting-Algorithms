#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Implementation of insertion sort in Python3
Reference: https://en.wikipedia.org/wiki/Insertion_sort
"""


def insertion_sort(A: list) -> None:
    i = 1
    while i < len(A):
        j = i
        while j > 0 and A[j-1] > A[j]:
            A[j], A[j-1] = A[j-1], A[j]
            j = j - 1
        i = i + 1
    return None


def insertion_sort_with_one_assignment(A: list) -> None:
    i = 1
    while i < len(A):
        x = A[i]
        j = i - 1
        while j >= 0 and A[j] > x:
            A[j+1] = A[j]
            j = j - 1
        A[j+1] = x
        i = i + 1
    return None


def insertion_sort_recursive(A: list, n: int) -> None:
    if n > 0:
        insertion_sort_recursive(A, n-1)
        x = A[n]
        j = n-1
        while j >= 0 and A[j] > x:
            A[j+1] = A[j]
            j = j-1
        A[j+1] = x
    return None


if __name__ == "__main__":
    arr = [51, 23, 56, 19, 4]
    print(f'not sorted: {arr}')
    insertion_sort_recursive(arr, len(arr)-1)
    print(f'sorted: {arr}')
