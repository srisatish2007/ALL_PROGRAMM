yr = int(input("ENTER THE YEAR : "))
if abs((yr - 2024)) % 4 == 0:
    print("THE YEAR ", yr, "IS A LEAP YEAR")
else:
    print("THE GIVEN YEAR IS NOT A LEAP YEAR ")
