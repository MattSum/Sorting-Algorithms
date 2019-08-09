#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 18:55:40 2019

@author: mateusz
"""


def bubble_sort(A: list) -> None:
    n = len(A)
    while n > 1:
        for i in range(0, n-1):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
            n = n-1


def bidirectional_bubble_sort(A: list) -> None:
    """ Also known as Cocktail shaker sort"""
    swapped = True
    while swapped:
        swapped = False
        for i in range(0, len(A)-2):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                swapped = True

        if not swapped:
            break
        swapped = False

        for i in range(len(A)-2, 0, -1):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                swapped = True


if __name__ == "__main__":
    arr = [51, 23, 56, 19, 4]
    print(arr)
    bidirectional_bubble_sort(arr)
    print(arr)
