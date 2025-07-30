class Input:
    def __init__(self):
        self.n1=int(input("Enter value of number1 :"))
        self.n2=int(input("Enter value of number2 :"))
class operate(Input):
    def __init__(self):
        super().__init__()
    def add(self):
        return self.n1+self.n2
    def mul(self):
        return self.n1*self.n2
class result(operate):
    def __init__(self):
         super().__init__()
    def display(self):
        print("Addition of two numbers is : ",self.add())
        print("Multiplication of two numbers is : ",self.mul())
r=result()
r.display()

