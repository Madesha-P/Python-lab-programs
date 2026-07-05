
N=int(input('Enter the number of elements:'))

def fib(n):

    if n<=1:
         return n

    else:
         return fib(n-1)+fib(n-2)
    
if N<=0:
     print("Enter the positive number !")

else:
     

     print("The fibbonaci sereies is :")

     for i in range(N):
          print(fib(i))
