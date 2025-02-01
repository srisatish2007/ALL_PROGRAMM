l = int(input("ENTER NUMBER OF LINES : "))
n_l = l + 1
for i in range(0, n_l):
    for j in range(0, i):
        print("*", end="\t")
    print("\n")

    #          3 ,2                           |   3,2,1,0-2,
for k in range(l, 0, -1):
    for m in range(k, 1, -1):  #
        print("*", end="\t")
    print("\n")
