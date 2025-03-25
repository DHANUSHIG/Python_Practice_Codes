class B:
    def palindrome(self):
        while True:
                strss = input("Input the String:")
                strss = strss.lower()
                if strss.isalpha():
                    break
                else:
                    print("Enter only Alphabet Try again")

        if strss==strss [::-1] :
            print(f"The  String {strss} is palindrome")
        else:
            print(f"The  string {strss} is Not A palindrome")
obj = B()
obj.palindrome()