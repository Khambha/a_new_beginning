import math
def mean(arr1):
    n=len(arr1)
    meanVal=sum(arr1)/n    
    return meanVal    

def median(arr1):
    n=len(arr1)
    mid=int(n/2)
    if(n%2==0):
        val=(arr1[mid]+arr1[mid+1])/2
    else:  
        val= arr1[mid]
    return val    

def mode(arr1):
    n=len(arr1)
    hc=0
    max_hc=0
    finalVal=0
    for i in range(0,n):
        val=arr1[i]
        hc+=1
        for j in range(0,n):
            if (arr1[j]==val):
                hc+=1
            else:
                 continue    
        if max_hc<=hc:
            finalVal=arr1[i]
            max_hc=hc
    return finalVal        

def stddev(arr1):
    n=len(arr1)
    print(arr1)
    sum1=0
    val=0
    me=int(mean(arr1))
    for i in arr1:
     sum1 +=(i-me)**2
    val=math.sqrt(sum1/n-1) 
    return math.sqrt(val) 
def vari(arr1):
    return stddev(arr1)**2


arr=[]
n = int(input("Enter number of elements : "))
for i in range(0, n):
    print("Enter value number ",(i+1), ": ")
    arr.append(int(input()))
val=mean(arr)
print("the mean is : ",val)      
med=median(arr)
print('The median of the array is : ', med)
mod=mode(arr)
print("The mode value in the array is : ", mod)
std=stddev(arr)
print("The standard deiation value of the array is : ", std)
va=vari(arr)
print("the variance of the array list is : ",va)
