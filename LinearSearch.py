



pos=0

def search(list,n):
    
    for e in list:
        globals()['pos']+=1
        if e==n:
            return True
    
    return False

list=[5,6,8,3,8,2,7]

n=8


if search(list,n):
    print("Found at ",pos)

else:
    print("Not Found")