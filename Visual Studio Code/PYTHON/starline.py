l = int(input("ENTER NUMBER OF LINES : "))
n_l = l + 1
for i in range(0, n_l):
    for j in range(0, i):
        print("*", end=" ")
    print("\n")
