class B:
    def Vowel_consonant_count(self):
        String=input("Enter the Strings:")
        String=String.lower()

        Voweles="aeiou"
        Voweles_count=0
        Consonant_count=0

        for char in String:
            if char.isalpha():
                if char in Voweles:
                   Voweles_count+=1
                else:
                   Consonant_count+=1
        print(f"the Voweles count:{Voweles_count}")
        print(f"the Consonant count:{Consonant_count}")
obj=B()
obj.Vowel_consonant_count()
