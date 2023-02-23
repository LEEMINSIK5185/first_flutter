from random import *
words = ["apple","banana","orange"]
word = choice(words)
print("answer : "+word)
letters = "" 

while True:
    succeed = True
    for w in word:
        if w in letters:
            print(w,end=" ")
        else:
            print("_",end=" ")
            succeed=False
    print()
    if succeed:
        print("success")
        break
    letter = input("\nInput letter > ") # 사용자 입력 받기
    if letter not in letters : 
        letters += letter
    
    if letter in word:
        print("correct")

    else:
        print("Wrong")
