"""
This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
"""


# O(N) or O(N * log(N))
def solution(A):
    length = len(A) + 1
    if A[-1] == len(A):
        length = len(A) + 2
    M = set(range(1, length))
    for i in A:
        if i in M:
            M.remove(i)
    return M.pop()

# O(N) or O(N * log(N))
def others_solution(A):
    n = len(A)
    counter = [0] * n
    print(counter)
    for i in range(0, n):
        if (A[i] > 0) and (A[i] <= n):
            counter[A[i] - 1] += 1
            print(i,A[i], counter)

    for i in range(0, len(counter)):
        if (counter[i] == 0):
            return i + 1
    return n + 1
