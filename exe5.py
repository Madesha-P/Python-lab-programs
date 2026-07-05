# empty dictionary 
my_dict = {} 
# number of elements 
n = int(input("Enter number of elements: ")) 
# taking input from user 
for i in range(n): 
    key = input("Enter key: ") 
    value = input("Enter value: ") 
    my_dict[key] = value 
# sorting dictionary based on keys 
sorted_dict = dict(sorted(my_dict.items())) 
# displaying results 
print("Original Dictionary:", my_dict) 
print("Dictionary sorted by keys:", sorted_dict)