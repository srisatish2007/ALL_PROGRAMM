class calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b


a = int(input("ENETR FIRST NUMBER : "))
b = int(input("ENTER SECOND NUMBER : "))
choise = int(
    input(
        """ENTER YOUR CHOISE : 
                   
                ENTER 1 FOR ADDITION 
                ENTER 2 FOR SUBTRATION
                ENTER 3 FOR MULTIPLICATION
                ENTER 4 FOR DIVISION """
    )
)
o = calculator(a, b)
if choise == 1:
    print("THE ANSWER IS : ", o.add())
elif choise == 2:
    print("THE ANSWER IS : ", o.sub())
elif choise == 3:
    print("THE ANSWER IS : ", o.mul())
elif choise == 4:
    print("THE ANSWER IS : ", o.div())
else:
    print("INVALID CHOISE!")
