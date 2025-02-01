# program to count the number of even and odd number in the give list!
from Lst_Input import lst_input as ls

lst1 = ls()
lst2 = []
for i in range(0, len(lst1)):
    lst2.append(int(lst1[i]))
num_E = 0
num_O = 0
for i in lst2:
    if i % 2 == 0:
        num_E += 1
    else:
        num_O += 1
print("THE NUMBER OF EVEN NUMBER IS : ", num_E)
print("THE NUMBER OF ODD NUMBER IS : ", num_O)
