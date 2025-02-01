a = input("ENTER A NMUBER TO CHECK WHETHER THE NUMBER IS PALIDROME : ")
b = list(a)
l = len(b)
p = []
for i in range(0, l):
    # 4-0-1=3
    # 4-1-1=2
    # 4-2-1=1
    # 4-3-1=0
    p.append(b[l - (i + 1)])
print("THE GIVEN NUMBER : ", b)
print("THE REVERSED NUMBER : ", p)
if p == b:
    print("YES!, THE GIVEN NUMBER IS PALINDROME ")
else:
    print("NO, THE GIVEN NUMBER IS NOT PALINDROME ")
