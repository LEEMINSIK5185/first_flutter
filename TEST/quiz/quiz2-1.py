from random import *
words = ["apple","banana","kiwii"]
word = choice(words)
print("answer : " + word)

letters = ""

while True:
    succeed=True
    for w in word:
        if w in letters:
            print(w,end=" ")
        else:
            print("_",end=" ")
            succeed=False
    
    print()
    if succeed:
        print("SUCCESS")
        break
    letter = input("input letters : ")
    if letter not in letters:
        letters += letter
    
    if letter in word:
        print("Correct")
    else:
        print("Wrong")