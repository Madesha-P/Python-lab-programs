n = int(input('Enter the number of elements: '))
a = []

for i in range(n):
    m = int(input('Enter the element: '))   # convert to int
    a.append(m)

print('The list is:', a)

file = open("even.txt", "w")   # open file in write mode

for num in a:
    if num % 2 == 0:
        file.write(str(num) + "\n")

file.close()

print('The file saved successfully!')