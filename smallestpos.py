# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
A = [-10, -100, 12, 231, 414124, 2]


def solution(A):
    # write your code in Python 3.8.10
    b = []
    f = []
    diff = []
    b = sorted(A, reverse=True)

    for i in range(min(b), max(b)+1):
        f.append(i)
    f = sorted(f, reverse=True)

    s = set(f)
    diff = [x for x in s if x not in b]
    diff = sorted(diff, reverse=True)

    if len(diff) != 0:
        if diff[0] < 0:
            return 1
    else:
        return max(b)+1

    return max(diff)


print(solution(A))
