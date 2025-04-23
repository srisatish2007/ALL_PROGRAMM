print("PROGRAM FOR PRIME NUMBERS")
Lim = int(input("ENTER THE LIMIT : "))
prime = []
factor = 0
for i in range(2,Lim+1):
    for j in range(2,Lim+1):
        if (i/j == i) and (i/j == 1):

            prime.append(i)
print(prime)
