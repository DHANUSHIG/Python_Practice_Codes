class C:
    def rvr_String(self):
        strs=input("Enter the new String:")
        strs=strs.upper()
        strss=""
        for char in strs:
            strss=char+strss
        print(f"the reversed string {strss}")
obj=C()
obj.rvr_String()

