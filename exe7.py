# where the keys are the lengths of the words and the values are lists of words that have that length.
# * The list inside the dictionary is used to store multiple words of the same length, 
# * allowing for efficient grouping and retrieval of words based on their lengths.

word_list=[]
word_dict={}

N=int(input("Enter the number of words :"))

for i in range (N):
    word=input(f"Enter the word {i+1} :")
    word_list.append(word)

for w in word_list:
    length=len(w)
    if length in word_dict:
        word_dict[length].append(w)
        # Here we are appending the word to the list inside the dictionary corresponding to its length

    else:
         word_dict[length]=[w] 
        # this is a string instead of a list, so we need to put it in a list

print("the words grouped with length are :")

print(word_dict)
