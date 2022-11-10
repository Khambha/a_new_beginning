def merge(L1,low,high,mid):
    size1=mid-low+1
    size2=high-mid
    L=[0]*(size1)
    R=[0]*(size2)
    for x in range(0,size1):
        L[x]=L1[low+x]
    for y in range(0,size2):
        R[y]=L1[mid+1+y]    
     
    i=low     
    j=0
    k=0      
    while(j<size1 and k<size2):
        if L[j]<=R[k]:
            L1[i]=L[j]
            j=j+1
        else:
            L1[i]=R[k]    
            k=k+1
        i=i+1    
    print(L,"",R)    
    while(j<size1):
        L1[i]=L[j]
        i=i+1
        j=j+1 
  
    while(k<size2):
        L1[i]=R[k] 
        i=i+1
        k=k+1 

def spliter(L1,low,high):
    if low<high:
        mid=low+(high-low)//2
        spliter(L1,low,mid)
        spliter(L1,mid+1,high)
        merge(L1,low,high,mid)

L1=list(input("Enter a set of values"))
print(L1)
n=len(L1)
spliter(L1,0, n-1)
print("The final set of strings after arrangement is :")
print(L1)



   
'''
L1=list(input("Enter a set of nummber you want to sort : "))
print(L1)
n=len(L1)
for x in range(0,n-1):
    for y in range(0,n-x-1):
        if (L1[y]>L1[y+1]):
                temp=L1[y+1]
                L1[y+1]=L1[y]
                L1[y]=temp
    print(L1)
print("The final sorted list is as follows: ")
print(L1)

''''''
L1=list(input("Enter a set of nummber you want to sort : "))
print(L1)
n=len(L1)
for x in range(0,n-1):
   
    for y in range(x+1,n):
        if (L1[y]<L1[x]):
               key=L1[y]
               L1[y]=L1[x]
               L1[x]=key  
    print(L1)  
print("The final sorted list is as follows: ")
print(L1)

'''