# programm to find the value of the binomial expansion ( 1 + x)^n
def exp(x, n):
    x = x - 1

    def fact(f):
        if f == 0:
            return 1
        else:
            return f * fact(f - 1)

    a1 = 1
    a2 = 1
    for i in range(0, n):  # 0
        if i == 0:
            a1 = (n) * x  #
            pass  #
        else:  #
            a1 = a1 * fact(i)
            a1 = (a1 * ((n - i) * x)) / fact(i + 1)  #
        a2 += a1  #
    return a2


print(exp(4, 4))
