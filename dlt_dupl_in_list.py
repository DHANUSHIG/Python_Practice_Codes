class Q:
    def duplicate(self):
        arr = list(map(int, input().split()))
        unique_list = []
        for num in arr:
            if num not in unique_list:
                unique_list.append(num)
        print(f"undated List {unique_list}")
obj =Q()
obj.duplicate()