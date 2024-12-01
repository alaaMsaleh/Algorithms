#Selection sort
def selection_sort(list):# Time Comp => o(n^2). where n is #element in list
    size = len(list)
    for i in range(0,size):#  o(n) * order of body => o(n^2)
        min_index = i
        for j in range(i+1, size):#  o(n) * order of body => o(n)
            if list[j] < list[min_index]:
                min_index = j 
        list[i], list[min_index] = list[min_index], list[i]
    return list
    

list=list(map(int,input("Enter group number you need sorting ").split()))
sorted_list=selection_sort(list)
print(sorted_list) 