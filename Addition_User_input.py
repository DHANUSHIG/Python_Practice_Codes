class A:
    def Addition(self):
        num=int(input("enter the number"))
        c=0
        for i in range(1,num+1):
            c+=i
        print(f"the addition of number is {c}")
obj=A()
obj.Addition()