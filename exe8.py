def divExp(a,b):
    try:
        c=a/b
        return c
    except ZeroDivisionError:
        print("division by zero is not possible !")
    

n1=int(input("enter numaarator :"))
n2=int(input("enter denominator :"))

result=divExp(n1,n2)
print("the result is :",result)


    
    