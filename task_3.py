arr = [5, 0, -2, 6, 3, 4, 4, -3, 5]


def solution(A):
    sup = 'sup'
    inf = 'inf'
    result = 0
    current = 0
    len_a = len(A)
    # oscillating = False
    status = ''
    for p, _ in enumerate(A):
        if p + 1 == len_a:
            break
        # I would like to improve this code but I just have 10 min left and I'm quite confident it works
        if A[p] > A[p + 1]:
            if not status:
                status = sup
                current += 1
            else:
                if status == inf:  # it is oscillating
                    status = sup
                    current += 1
                else:
                    status = sup
                    current = 0

        if A[p] < A[p + 1]:
            if not status:
                status = inf
                current += 1
            else:
                if status == sup:  # it is oscillating
                    status = inf
                    current += 1
                else:
                    status = inf
                    current = 0

        result = max(result, current)

    return result


# test = [1, 2, 1, 2, 4, 1, 2, 1]

print(solution(arr))
# print(solution(test))

assert solution(arr) == 5
