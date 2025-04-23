import math


def fact(f):
    if f == 0:
        return 1
    else:
        return f * fact(f - 1)


def comb(n, r):
    # nCr
    if n == r:
        return 1
    elif n < r:
        return "INVALID VALUE OF -R-"
    elif r == 0:
        return 1
    else:
        c = fact(n) / (fact(r) * fact(n - r))
        return c


a = int(input("ENTER THE VALUE OF A : "))
b = int(input("ENTER THE VALUE OF B : "))
n = int(input("ENTER THE EXPONENT VALUE : "))
ans1 = 0
ans2 = 0
for r in range(0, n + 1):
    ans1 = comb(n, r) * (a ** (n - r)) * ((b**r))
    ans2 += ans1
print(ans2)
