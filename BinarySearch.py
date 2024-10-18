list=[5,16,28,33,48,52,67]
pos=0
n=52


def search(list,n):
    l=0
    u=len(list)-1
    print(range(l,u))
    for e in range(l,u):
        
        mid=(l+u)//2
        if list[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if list[mid]<n:
                l=mid+1
            else:
                u=mid-1



if search(list,n):
    print("Found at ",pos)

else:
    print("Not Found")