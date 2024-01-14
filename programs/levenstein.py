#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, inv_left = merge_sort(arr[:mid])
    right, inv_right = merge_sort(arr[mid:])
    merged, inv_merge = merge(left, right)

    return merged, (inv_left + inv_right + inv_merge)


def merge(left, right):
    i, j = 0, 0
    inversions = 0
    merged = []

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            inversions += len(left) - i

    merged += left[i:]
    merged += right[j:]

    return merged, inversions


if __name__ == "__main__":
    arr = [1, 3, 5, 2, 4, 6, 100, 99, 33, 29, 35]
    print(f"Массив: {arr}")

    sorted_arr, inversions = merge_sort(arr)
    print(f"Отсортированный массив: {sorted_arr}")
    print(f"Количество инверсий: {inversions}")









