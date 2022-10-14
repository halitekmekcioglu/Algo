"""

"""

A = [1, 1, 3, 3]

b = []


def sol(b, A):

    b = sorted(A, reverse=True)

    if b[0] % 2 == 1:
        for i in b:
            if i % 2 == 0:
                return i+b[0]
        return b[0]

    elif b[0] % 2 == 0:
        for i in b:
            if i % 2 == 1:
                return i+b[0]
        return b[0]


print(sol(b, A))
