'''L1=list(input("Enter a set of nummber you want to search from : "))
print("The values present are as follows : ", L1)
val=input("Enter the value you want to search :")
n=len(L1)
check=0
for x in range(n):
    if L1[x] == val:
        check=1
        ind= L1.index(val)+1
        print("The value ",val," is found at position number : ",ind," and was found in ",x+1," moves...")

    else:
        continue       
if (check != 1):
    print("Sorry element not found")    
print("Process done")    
'''


L1=list(input("Enter a set of nummber you want to search from : "))
print("The values present are as follows : ", L1)
val=input("Enter the value you want to search :")
n=len(L1)
check=0
low=0
high=n
i=1

for x in range(0,n-1):
    for y in range(0,n-x-1):
        if (L1[y]>L1[y+1]):
                temp=L1[y+1]
                L1[y+1]=L1[y]
                L1[y]=temp
print(L1)                
while low!= n+1 and high != -1:
    mid = (low+ high)//2
    if(L1[mid]==val):
        ind =L1.index(val)+1
        print("The value ",val," is found at position number : ",ind," and was found in ",i," moves...")
        check=1
        break
    elif L1[mid]>val :
        high=mid-1 
        i+=1
        continue
    else :
        low=mid+1 
        i+=1
        continue
if(check!=1):
    print("Sorry value not found")
print("Process completed")            
