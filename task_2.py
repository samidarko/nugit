arr = [5, 5, 1, 7, 2, 3, 5]
# arr = [5, 5, 1, 7, 5, 3, 5]


def solution(X, A):
    k = 0
    # init = 0
    # len_a = len(A)
    # def fn(arr, pos, k):
    #     if pos == len_a:
    #         return k+1
    #     elif arr[pos] == X:
    #         arr[k], arr[pos] = arr[pos], arr[k]
    #         return fn(arr, pos+1, k+1)
    #     else:
    #         return fn(arr, pos+1, k)
    for i, item in enumerate(A):
        if item == X:
            A[k], A[i] = A[i], A[k]
            k += 1

    # return fn(A, init, k)
    return k+1

# assert solution(5, arr) == 4

big_list = list(range(0, 1000))
big_list[500] = 5
# print(solution(5, arr))
print(solution(5, big_list))
