"""Sort a list of numbers from lowest to highest"""

numList = [5, 2, 8, 3, 9]

"""double for loop"""


def insertion_sort_for(A):
    for i in range(1, len(A)):
        for j in range(i - 1, 0, -1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
            else:
                break


"""while loop"""


def insertion_sort_while(A):
    for i in range(1, len(A)):
        j = i - 1
        while A[j] > A[j + 1] and j >= 0:
            A[j], A[j + 1] = A[j + 1], A[j]
            j -= 1


"""optimized method"""


def insertion_sort_optimized(A):
    for i in range(1, len(A)):
        cur_num = A[i]
        for j in range(i-1, 0, -1):
            if A[j] > cur_num:
                A[j+1] = A[j]
            else:
                A[j+1] = cur_num
                break
