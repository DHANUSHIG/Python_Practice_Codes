class B:
    def Largest_Smallest_element(self):
        arr=list(map(int, input().split()))
        max_element=min_element=arr[0]

        for num in arr[1:]:
            if num>max_element:
                max_element=num
            elif num<min_element:
                min_element=num
        print(f"The largest is {max_element} and the smallest element is {min_element}")
obj =B()
obj.Largest_Smallest_element()