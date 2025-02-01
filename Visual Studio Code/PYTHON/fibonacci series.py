n = int(input("ENTER THE LIMIT : "))
a = 0
b = 1
print(a)
print(b)
for i in range(0, n + 1):
    s = a + b
    print(s)
    a = b
    b = s
