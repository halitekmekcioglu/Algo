
A = "OXOOXOXOXOXOOOOX"
x = []
o = []


def sol(x, o, A):

    a = [*A]
    z = 0
    w = 0
    for i in range(0, (len(a))):
        for k in range(1, (len(a))):

            if a[i] == a[k] and abs(i-k) <= 2:
                z = z+1
                w = w+1
                #print("z", z, "i", i, "k", k)
                if z >= 3:
                    if a[k] == "X":
                        x.append(a[k])

                if w >= 3:
                    if a[k] == "O":
                        o.append(a[k])

            else:
                z = 0
                w = 0
                #print("x", x, "o:", o)
                pass

    if len(x) >= 3 and len(o) < 3:
        return "X is winner", x, o
    elif len(x) < 3 and len(o) > 3:
        return "O is winner", x, o
    elif len(x) >= 3 and len(o) >= 3 or len(x) < 3 and len(o) < 3:
        return "its tie", x, o


print(sol(x, o, A))
