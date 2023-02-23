import cv2
import numpy as np
import copy

def PeripheralHoleBoundaryTracking(mode,memImage,cr,cc,pixel,label):
    pdir = 0 #이전탐색방향
    ndir = 0 #다음탐색방향
    r = cr  # row좌표
    c = cc #column좌표
    d = [0]*8
    flag = False

    while True:
        d[0] = memImage[r][c + 1];
        d[1] = memImage[r + 1][c + 1];
        d[2] = memImage[r + 1][c];
        d[3] = memImage[r + 1][c - 1];
        d[4] = memImage[r][c - 1];
        d[5] = memImage[r - 1][c - 1];
        d[6] = memImage[r - 1][c];
        d[7] = memImage[r - 1][c + 1];
 
        if(d[0]==0 and d[1]==0 and d[2]==0 and d[3]==0 and d[4]==0 and d[5]==0 and d[6]==0 and d[7]==0):
            break

        #마스크내의 탐색시장 방향 설정
        ndir = pdir - 3
        if (ndir == -1):
            ndir = 7
        elif (ndir == -2):
            ndir = 6
        elif (ndir == -3):
            ndir = 5

        #마스크내의 탐색을 시계방향으로 수행
        while True:
            if((d[ndir] == pixel) or (d[ndir] == label)):
                flag = False
                if(pdir == 1):
                    if(ndir==5):
                        flag = True
                elif(pdir == 2):
                    if(ndir==5 or ndir == 6):
                        flag = True
                elif (pdir == 3):
                    if (ndir == 5 or ndir == 6 or ndir == 7):
                        flag = True
                elif (pdir == 4):
                    if (ndir == 0 or ndir == 5 or ndir == 6 or ndir == 7):
                        flag = True
                elif (pdir == 5):
                    if (ndir != 2 and ndir != 3 and ndir !=4):
                        flag = True
                elif (pdir == 6):
                    if (ndir != 3 and ndir != 4):
                        flag = True
                elif (pdir == 7):
                    if (ndir != 4):
                        flag = True

                if(flag):
                    memImage[r][c] = label
                pdir = ndir
                break
 
            else: #다음 탐색방향 설정
                ndir = ndir+1
                if(ndir>7):
                    ndir = 0

         #위치이동
        if(ndir == 0):
            c+=1
        elif(ndir==1):
            r+=1
            c+=1
        elif(ndir==2):
            r+=1
        elif(ndir==3):
            r+=1
            c-=1
        elif(ndir==4):
            c-=1
        elif(ndir==5):
            r-=1
            c-=1
        elif(ndir==6):
            r-=1
        elif(ndir==7):
            r-=1
            c+=1
 
        if((r == cr) and (c == cc)):
            break
 
    return memImage

img = cv2.imread('/Users/leeminsik/Desktop/Images (1)/bolt.bmp',1)
img2 = cv2.imread('/Users/leeminsik/Desktop/Images (1)/bolt.bmp', 0)
ret, thresh1 = cv2.threshold(img2, 127, 255, cv2.THRESH_BINARY) #이미지 이진화
cv2.imshow('original', thresh1)    


maxX = thresh1.shape[1]
maxY = thresh1.shape[0]
 
 
memImage = np.zeros((maxY,maxX))
 
dd = [[0]*3 for i in range(3)]
 
 
print(thresh1[50])


for y in range(0, maxY, 1):
    for x in range(0, maxX, 1):
        c = 0
        if(x == 0 or y == 0 or x == (maxX-1) or y == (maxY-1)):
            c = 0
        else:
            c = thresh1[y][x]
            if(c==0):
                c = 0
            else:
                c = -255
        print(x,y)
        memImage[y][x] = c
 
pixValue = 0
label = 0



for y in range(1, maxY - 1, 1):
    for x in range(1, maxX -1 , 1):
        pixValue = memImage[y][x]
        if(memImage[y][x] < 0):
            if ((memImage[y][x - 1] <= 0) and (memImage[y - 1][x - 1] <= 0)):
                label+=1
                print("라벨",label, ' ', pixValue,x,y)
                memImage[y][x] = label
                memImage = PeripheralHoleBoundaryTracking(1, memImage, y, x, pixValue, label)
            elif (memImage[y][x-1] > 0) :
                memImage[y][x] = memImage[y][x-1]
            elif ((memImage[y][x-1] <= 0) and (memImage[y-1][x-1] > 0)) :
                memImage[y][x] = memImage[y-1][x-1]
                memImage = PeripheralHoleBoundaryTracking(2, memImage, y, x, pixValue, memImage[y-1][x-1])
 
for y in range(0, maxY,1):
    for x in range(0, maxX, 1):
        c = int(memImage[y][x] * (255 / (label+1))) # 레이블의 수에 따라 밝기값을 균등분할
        if (c == 0):
            c = 255
        img[y][x] = [c,c,c]
 
cv2.imshow('fast region labeling', img)
cv2.waitKey(0)
cv2.destroyAllWindows()



