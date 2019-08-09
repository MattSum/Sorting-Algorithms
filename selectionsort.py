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


if __name__ == "__main__":
    arr = [51, 23, 56, 19, 4]
    print(arr)
    selection_sort(arr)
    print(arr)