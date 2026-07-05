file=open("new.txt","r")
data=file.read()
file.close
freq={}
for ch in data:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
print("character Frequncies :")

for ch in freq:
    print(ch,":",freq[ch])
