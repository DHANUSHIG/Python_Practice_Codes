class A:
    def Tuple(self):
        inp=list(map(int,input('enter the list').split()))
        Tuple=tuple(inp)
        if len(inp)!=5:
            print("enter only five elements")
        else:
            print(f"the Tuple {Tuple[::-1]}")
obj = A()
obj.Tuple()