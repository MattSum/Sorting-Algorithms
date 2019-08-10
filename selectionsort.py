#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Implementation of selection sorting algotithm in Python
Reference: https://en.wikipedia.org/wiki/Selection_sort
"""

def selection_sort(A: list) -> None:
    for i in range(len(A)):
        minimal = i

        for j in range(i+1, len(A)):
            if A[j] < A[minimal]:
                minimal = j
    
        if minimal != i:
            A[i], A[minimal] = A[minimal], A[i]
    
    return None


def bidirectional_selection_sort(A: list) -> None:
    """Known as Coctail sort"""
    k = len(A)-1
    for i in range(len(A)):
        minimal = i
        maximal = k
        for j in range(i+1, k+1):
            if A[j] < A[minimal]:
                minimal = j

        if minimal != i:
            A[i], A[minimal] = A[minimal], A[i]

        for j in range(k, i, -1):
            if A[j] > A[maximal]:
                maximal = j

        if maximal != k+1-i:
            A[k], A[maximal] = A[maximal], A[k]

        k -= 1
        if k < len(A) / 2:
            break

    return None


if __name__ == "__main__":
    arr = [51, 23, 0, 1, 56, 19, 4]
    print(arr)
    bidirectional_selection_sort(arr)
    print(arr)