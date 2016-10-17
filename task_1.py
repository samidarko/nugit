
def solution(A):
    # def fn(arr, pos, counter):
    #     if arr[pos] == -1:
    #         return counter + 1
    #     else:
    #         return fn(arr, arr[pos], counter + 1)
    #
    # return fn(A, 0, 0)
    pos = 0
    counter = 0
    while A[pos] != -1:
        counter += 1
        pos = A[pos]

    return counter + 1

print(solution([1, 4, -1, 3, 2]))

assert solution([1, 4, -1, 3, 2]) == 4

