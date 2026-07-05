import numpy as np  
lst = [] 
# number of elements as input  
n = int(input("Enters number of elements : "))  
print("Enter the elements of the list:")  
# iterating till the range  
for i in range(0, n):  
    ele = int(input())  
    lst.append(ele) # adding the element  
print(lst) 
# Calculating average using average()  
print("Mean=", np.average(lst))  
# Calculating variance using var()  
print("Variance=", np.var(lst))  
# Calculating standard deviation  
print("Standard Deviation=", np.std(lst))