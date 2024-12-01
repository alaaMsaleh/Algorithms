#Insertion 

#[32 , 1 ,10 , 5 ,2]


def insertion(List):
 for i in range(1,len(List)): 
      key=List[i]#i=1
      j=i-1  #j=06
      while j>=0 and key<List[j]:
        List[j + 1] = List[j] 
        j -= 1 
        List[j + 1] = key  
        
 return List  
       
if __name__ == "__main__":    
 List=list(map(int,input("Enter group number you need sorting ").split()))

 sorted_list=insertion(List)
print(sorted_list)
  
