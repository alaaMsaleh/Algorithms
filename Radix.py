"""def radix_sort(arr):
    # find max nmber
    max_num = arr[0]
    for num in arr:
        if num > max_num:
            max_num = num

    # calc digit
    num_digits = 0
    temp = max_num
    while temp > 0:
        temp //= 10
        num_digits += 1

    place = 1 #to determin any digit and updata by *10 to move to next digit

    while num_digits > 0:
        buckets = [[] for _ in range(10)]
        
        for num in arr:
            digit = (num // place) % 10
            buckets[digit].append(num)
        
        arr = []
        for bucket in buckets:
            for item in bucket:
                arr.append(item)
        
        place *= 10
        num_digits -= 1

    return arr


arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
sorted_arr = radix_sort(arr)
print("Sorted Array:", sorted_arr)

buckets[0] = [170, 90]  
buckets[1] = []     
buckets[2] = [2]       
buckets[3] = []         
buckets[4] = [24]      
buckets[5] = [75]     
buckets[6] = [66]      
buckets[7] = []         
buckets[8] = []         
buckets[9] = [45]       

"""
def radix_sort(List): # Time Comp => o(n*k). where n is #element in list



    max_length = max(len(num) for num in List)#     o(n)



    List_with_zeros = [str(num).zfill(max_length) for num in List] #    o(n)



    for digit_pos in range(max_length-1, -1, -1): # o(k*n)

        Result = [[] for _ in range(10)] #  o(1)



        for num in List_with_zeros: #   o(n)

            digit = int(num[digit_pos])

            Result[digit].append(num)



        List_with_zeros = []

        for R in Result: #  o(n)

            List_with_zeros.extend(R)



        print(f"List after sorting by digit {max_length - digit_pos}: {List_with_zeros}")

    List_final = [num.lstrip('0') for num in List_with_zeros] # o(n)

    print(f"Sorted List (with leading zeros): {List_with_zeros}")

    print(f"Sorted List (without leading zeros): {List_final}")

    return List_final





List = input("Enter numbers separated by spaces: ").split()





sorted_list = radix_sort(List)