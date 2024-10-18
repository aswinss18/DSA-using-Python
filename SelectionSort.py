list=[48,96,7,1,3,15,6,7,10]

def sort(list):
    for i in range(len(list)-1):
        minpos=i
        for j in range(i,len(list)):
            if list[j]<list[minpos]:
                minpos=j

        temp=list[i]
        list[i]=list[minpos]
        list[minpos]=temp
        
        
   
    
    



sort(list)

print(list)