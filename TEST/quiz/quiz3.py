# for i in range(1,21):
#     if i%2!=0:
#         print("A"+str(i),end= " ")

for i in range(1,21)[::2]:
    print("A" + str(i),end=" ")
print()
for j in range(1,21):
    print("B"+ str(j),end=" ")