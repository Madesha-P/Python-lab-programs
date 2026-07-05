class stud:
    def display(self):
        print("Enter the number of subjects:")
        n=int (input())
        for i in range (n):
            sub=input("enter subject name:")
            marks=int(input ("enter the marks in the subject:"))
            if marks < 40:
                print("result",sub,": Fail")
            else:
                print("result",sub,": Pass")
        return self
        
s=stud()
print(s.display())
    
    