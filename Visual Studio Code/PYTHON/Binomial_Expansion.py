print("WELCOME TO BINOMIAL EXPANSION!")
x = int(input("ENTER A VALUE FOR HTE SEREIS : "))
n = int(input("ENTER THE EXPONENT VALUE : "))


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
print("THE ANSWER OF " + "(  1  + ", x, " )  ^ ", n, "IS : ", a2)
