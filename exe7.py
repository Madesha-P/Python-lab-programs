w=[]
n=int(input("Enter the number of words:"))

for i in range (n):
    word=input("Enter the word:")
    w.append(word)

word_dict={}

for i in w:
    length=len(i)
    if length in word_dict:
        word_dict[length].append(i)

    else:
        word_dict[length]=[i]
        

print("Words grouped by length:-")

print(word_dict)
