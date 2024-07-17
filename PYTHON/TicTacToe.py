import random
import time

print("                          WELCOME TO TIC-TAC-TOE GAME                       ")
print("============================================================================")
n = input("\n\tENTER YOUR OPTION X OR O : ")
if n == "x" or "X" or "o" or "O":
    n = n.upper()
else:
    print("\tINVALID ENTRY! OF CHARACTER ")
if n == "X":
    comp = "O"
else:
    comp = "X"
print()
print("\tYOUR OPTION : " + n)
print()
print("\tCOMPUTER OPTION : " + comp)
print(
    """\t
           ::          ::
           ::          ::
     A     ::    B     ::    C
           ::          ::
           ::          ::
::::::::::::::::::::::::::::::::::::
           ::          ::
           ::          ::
     D     ::    E     ::    F
           ::          ::
           ::          ::
::::::::::::::::::::::::::::::::::::
           ::          ::
           ::          ::
     G     ::    H     ::    I
           ::          ::
           ::          ::
"""
)
lst = []
A = "A"
B = "B"
C = "C"
D = "D"
E = "E"
F = "F"
G = "G"
H = "H"
I = "I"
i = 0
result = "0"


def main_cal():
    global i, result

    while i <= 4:

        def cal():
            global lst, n, comp, A, B, C, D, E, F, G, H, I, i, result
            print("\tIT'S YOUR TURN!")
            opt = input("\tENTER YOUR OPTION TO PLACE " + n + " : ")
            opt = opt.upper()
            if ord(opt) <= 73:
                pass
                if opt == "A":
                    if opt not in lst:
                        A = n
                        lst.append(opt)
                    else:
                        print(n + " IS ALREADY EXIST IN " + opt)
                        cal()
                elif opt == "B":
                    if opt not in lst:
                        B = n
                        lst.append(opt)
                    else:
                        print(n + " IS ALREADY EXIST IN " + opt)
                        cal()
                elif opt == "C":
                    if opt not in lst:
                        C = n
                        lst.append(opt)
                    else:
                        print(n + " IS ALREADY EXIST IN " + opt)
                        cal()
                elif opt == "D":
                    if opt not in lst:
                        D = n
                        lst.append(opt)
                    else:
                        print(n + " IS ALREADY EXIST IN " + opt)
                        cal()
                elif opt == "E":
                    if opt not in lst:
                        E = n
                        lst.append(opt)
                    else:
                        print(n + " IS ALREADY EXIST IN " + opt)
                        cal()
                elif opt == "F":
                    if opt not in lst:
                        F = n
                        lst.append(opt)
                    else:
                        print(n + " IS ALREADY EXIST IN " + opt)
                        cal()
                elif opt == "G":
                    if opt not in lst:
                        G = n
                        lst.append(opt)
                    else:
                        print(n + " IS ALREADY EXIST IN " + opt)
                        cal()
                elif opt == "H":
                    if opt not in lst:
                        H = n
                        lst.append(opt)
                    else:
                        print(n + " IS ALREADY EXIST IN " + opt)
                        cal()
                elif opt == "I":
                    if opt not in lst:
                        I = n
                        lst.append(opt)
                    else:
                        print(n + " IS ALREADY EXIST IN " + opt)
                        cal()
                else:
                    print("INVALID ENTRY! ")
            print(lst)
            print(
                f"""\t
           ::          ::
           ::          ::
     {A}     ::    {B}     ::    {C}
           ::          ::
           ::          ::
::::::::::::::::::::::::::::::::::::
           ::          ::
           ::          ::
     {D}     ::    {E}     ::    {F}
           ::          ::
           ::          ::
::::::::::::::::::::::::::::::::::::
           ::          ::
           ::          ::
     {G}     ::    {H}     ::    {I}
           ::          ::
           ::          ::
"""
            )

            if len(lst) >= 5:
                if (
                    A == B == C == n
                    or D == E == F == n
                    or G == H == I == n
                    or A == D == G == n
                    or B == E == H == n
                    or C == F == I == n
                    or A == E == I == n
                    or C == E == G == n
                ):
                    result = "YOU WON THE MATCH !"
                    print(result)
                    i = 10
                    main_cal()

                elif (
                    A == B == C == comp
                    or D == E == F == comp
                    or G == H == I == comp
                    or A == D == G == comp
                    or B == E == H == comp
                    or C == F == I == comp
                    or A == E == I == comp
                    or C == E == G == comp
                ):
                    result = "COMPUTER WON THE MATCH !"
                    print(result)
                    i = 10
                    main_cal()

            else:
                pass
            if i != 4 and result == "0":
                print("\tIT'S COMPUTER TURN")
                time.sleep(2)

                def COMP_OPT():
                    global lst
                    comp_opt = random.randint(65, 73)
                    comp_opt = chr(comp_opt)
                    if comp_opt not in lst:
                        globals()[comp_opt] = comp
                        lst.append(comp_opt)
                    else:
                        COMP_OPT()

                COMP_OPT()
                print(lst)

                print(
                    f"""\t
           ::          ::
           ::          ::
     {A}     ::    {B}     ::    {C}
           ::          ::
           ::          ::
::::::::::::::::::::::::::::::::::::
           ::          ::
           ::          ::
     {D}     ::    {E}     ::    {F}
           ::          ::
           ::          ::
::::::::::::::::::::::::::::::::::::
           ::          ::
           ::          ::
     {G}     ::    {H}     ::    {I}
           ::          ::
           ::          ::
"""
                )
            elif len(lst) == 9 and result == "0":
                print("MATCH DRAW!")
            else:
                pass
            result2 = "0"
            if len(lst) >= 5 and result == "0":
                if (
                    A == B == C == n
                    or D == E == F == n
                    or G == H == I == n
                    or A == D == G == n
                    or B == E == H == n
                    or C == F == I == n
                    or A == E == I == n
                    or C == E == G == n
                ):
                    result2 = "YOU WON THE MATCH !"
                    print(result2)
                    i = 10
                    main_cal()
                elif (
                    A == B == C == comp
                    or D == E == F == comp
                    or G == H == I == comp
                    or A == D == G == comp
                    or B == E == H == comp
                    or C == F == I == comp
                    or A == E == I == comp
                    or C == E == G == comp
                ):
                    result2 = "COMPUTER WON THE MATCH !"
                    print(result2)
                    i = 10
                    main_cal()
            else:
                pass

        cal()
        i = i + 1


main_cal()
print("THE PROGRAM EXECUTED ! ")
