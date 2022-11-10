import numpy as np
import scipy as stats

list1=[]
n=int(input("enter the value of n :"))
print("enter the numbers :")
for i in range(n):
    list1.append(int(input()))
print("numbers are : ", list1)
list2=[]
print("enter the numbers :")
for i in range(n):
    list2.append(int(input()))
print("numbers are : ", list2)
kpcoeff = np.corrcoef(list1, list2)
print("karl pearson coefficient of correlation is :", kpcoeff)
rankcorr=stats.spearmanr(list1,list2)[0]
print("rank correlation is :", rankcorr)
