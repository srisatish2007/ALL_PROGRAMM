print("Binomial expansion")


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


def comb(n, r):
    sum = 0
    sum = fact(n) / (fact(r) * fact(n - r))
    return sum


x = float(input("Enter your value:"))
n = int(input("Enter he exponents value:"))
t = float(0)
for i in range(0, n + 1):
    t += (1 ** (n - 1)) * (x**i) * comb(n, i)
    print("The the binomial expansion is:", t)
