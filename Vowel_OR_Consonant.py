def Vowel_OR_Consonant():
    str=input("Enter the String")
    STR1="aeiouAEIOU"
    if len(str)!=1 or not str.isalpha():
        print("enter the Single Letter only!!")
    elif  str in STR1:
        print(f"the {str} is vowele")
    else:
        print(f'the {str} is consonant ')
Vowel_OR_Consonant()




