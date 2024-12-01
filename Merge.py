def merge_sort(A,P,R):
   if P < R :

      Q = ( P + R ) // 2  #O(1)
   
      merge_sort (A,P,Q)  #T(N/2)
      merge_sort (A,Q+1,R)  #T(N/2)
      merge(A,P,Q,R)  #O(N)
   
def merge(A,P,Q,R):
    
   left_part = A[P:Q +1] 
   right_part = A[Q+1:R+1] 
    
   left_part.append(float('inf'))  #O(1)
   right_part.append(float('inf')) #O(1)
    
   i = j = 0   #O(1)
   
   for K in range(P,R+1): 
       if left_part[i] <= right_part[j]: #O(1)
           A[K] = left_part[i]  #O(1)
           i += 1
         
           
       else:
            A[K] = right_part[j] #O(1)
            j += 1   #O(1)
            
A = list(map(int, input("Enter numbers separaed by spaces:").split()))

merge_sort(A,0,len(A)-1)

print("Array after sorting:",A)