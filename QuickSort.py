def partition(arr, iStart, jEnd):
    i = iStart
    j = jEnd
    pivLoc = i

    while i < j:
        while pivLoc != j:
            if arr[pivLoc] > arr[j]:
                arr[j], arr[pivLoc] = arr[pivLoc], arr[j]
                pivLoc = j
            else:
                j -= 1
                if pivLoc == j:
                    break

        while pivLoc != i:
            if arr[pivLoc] < arr[i]:
                arr[i], arr[pivLoc] = arr[pivLoc], arr[i]
                pivLoc = i
            else:
                i += 1
                if pivLoc == i:
                    break

    return pivLoc


def Quick_sort(arr, I, J):
    if I < J:
        Pivot = partition(arr, I, J)
        Quick_sort(arr, I, Pivot - 1)
        Quick_sort(arr, Pivot + 1, J)

        
        
List = list(map(int, input("Enter group number you need sorting: ").split()))
Quick_sort(List, 0, len(List) - 1)
print("Sorted list:", List)