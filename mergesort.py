# -*- coding: utf-8 -*-
"""
Merge sort algorithm implemented in Python3
Reference pseudo code: https://en.wikipedia.org/wiki/Merge_sort
"""


def bottom_up_merge(left: list, right: list) -> list:
    result = []
    while left != [] and right != []:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]

    while left != []:
        result.append(left[0])
        left = left[1:]
    while right != []:
        result.append(right[0])
        right = right[1:]
    return result


def bottom_up_merge_sort(mer: list) -> list:
    if len(mer) <= 1:
        return mer
    left = []
    right = []
    for i, x in enumerate(mer):
        if i < len(mer) / 2: 
            left.append(x)
        else:
            right.append(x)
    left = bottom_up_merge_sort(left)
    right = bottom_up_merge_sort(right)
    return bottom_up_merge(left, right)


if __name__ == "__main__":
    arr = [51, 23, 56, 19, 4]
    print(f'not sorted: {arr}')
    print(f'sorted: {bottom_up_merge_sort(arr)}')
