def lst_input():
    Lst = []
    print("ENTER THE ELEMENTS OF THE LIST ONCE YOU ARE DONE ENTER `!` ")
    for i in range(0, 1000):
        j = input()
        if j == chr(33):
            break
        else:
            Lst.append(j)
    return Lst
