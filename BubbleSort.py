def buble_sort(List):# Time Comp => Big-oh(n^2). where n is #element in list
    size = len(List)
    for i in range(0, size):#  o(n) * order of body => Big-oh(n^2)
        for j in range(0, size - i - 1):#   Big-oh(n) * order of body => Big-oh(n)
            if List[j+1] < List[j]:
                List[j], List[j+1] = List[j+1], List[j]

    return List
 
List=list(map(int,input("Enter group number you need sorting ").split()))

sorted_list=buble_sort(List)
print(sorted_list)                