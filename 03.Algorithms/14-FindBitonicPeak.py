"""
Given an array that is bitonically sorted, an array that starts off with increasing terms
and then concludes with decreasing terms. In any such sequence, there is a "peak" element,
that is, the element in the sequence that is the largest element.

We will be writing a problem to help us in finding the peak element of a bitonic sequence.
"""


def find_highest_number(A):
    low = 0
    high = len(A) - 1

    # Require at least 3 elements fora valid bitonic seg
    if len(A) < 3:
        return None

    while low <= high:
        mid = (low + high) // 2

        mid_left = A[mid - 1] if mid - 1 > 0 else float("-inf")
        mid_right = A[mid + 1] if mid + 1 < len(A) else float("inf")

        if mid_left < A[mid] < mid_right:
            low = mid + 1

        elif mid_left > A[mid] > mid_right:
            high = mid - 1

        elif mid_left < A[mid] > mid_right:
            return A[mid]


# Peak element is "5".
A = [1, 2, 3, 4, 5, 4, 3, 2, 1]

# Peak element is "4".
B = [1, 2, 3, 4, 1]

# Peak element is "6".
C = [1, 6, 5, 4, 3, 2, 1]

x = find_highest_number(A)
print(x)
