# program to calculate the sum of series up to n term. For example, if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690
num = int(input("ENTER NUMBER THAT YOU WANT TO USE OF THE SERIES : "))
tim = int(input("ENTER HOW MANY TIMES : "))
num1 = 0
num2 = num / 10
new = 0
k = 10
num3 = num
for i in range(2, tim + 2):  #
    num1 = num1 + (num2 * k)  #
    new += num1
    k = pow(10, i)  #
print(int(new))
