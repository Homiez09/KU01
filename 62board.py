#ได้ 100 คะแนน
NMS = [int(x) for x in input().split()]

row = []
for i in range(NMS[0]):
    row.append([int(x) for x in input().split()])

notseen = 0
for i in range(1, NMS[0]): #row  
    for j in range(NMS[1]): #column    
       for k in range(1,i+1):
           if row[i][j] + (NMS[2]*k) <= row[i-k][j]:
               notseen += 1
               break

print((NMS[0]*NMS[1])-notseen)