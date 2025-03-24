class M:
    def DivisibleBy(self):
        Num1 = int(input("enter the number"))
        if Num1%11==0 and Num1%5==0:
            print("the number is divisible by 11 and 5")
        else:
            print('the number is not divisible by 11 and 5')
obj =M()
obj.DivisibleBy()

