list=[48,96,7,1,3,15,6,7,10]

def sort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j]>list[j+1]:
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp
    
    



sort(list)

print(list)