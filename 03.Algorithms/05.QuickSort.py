"""Sort a list from lowest to highest"""


def quick_sort(A):
    quick_sort2(A, 0, len(A)-1)


def quick_sort2(A, low, hi):
    if low < hi:
        p = partition(A, low, hi)
        quick_sort2(A, low, hi)
        quick_sort2(A, p+1, hi)


def get_pivot(A, low, hi):
    mid = (hi + low) // 2
    pivot = hi
    if A[low] < A[mid]:
        if A[mid] < A[hi]:
            pivot = mid
    elif A[low] < A[hi]:
        pivot = low
    return pivot


def partition(A, low, hi):
    pivot_index = get_pivot(A, low, hi)
    pivot_value = A[pivot_index]
    A[pivot_index], A[low] = A[low], A[pivot_index]
    border = low

    for i in range(low, hi+1):
        if A[i] < pivot_value:
            border += 1
            A[i], A[border] = A[border], A[i]
    A[low], A[border] = A[border], A[low]

    return border
