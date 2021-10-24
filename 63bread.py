#ได้ 100 คะแนน
mode = [int(x) for x in input().split()]

W = mode[0]
H = mode[1]
M = mode[2]
N = mode[3]

position_cutX = [int(x) for x in input().split()]
position_cutY = [int(y) for y in input().split()]

position_cutX.append(W)
position_cutX.append(0)
position_cutY.append(H)
position_cutY.append(0)

position_cutX.sort()
position_cutY.sort()

height = []
width = []
for i in range(M+1):
    height.append(position_cutX[i+1]-position_cutX[i])
for i in range(N+1):
    width.append(position_cutY[i+1]-position_cutY[i])
total=[]
for i in width:
    for j in height:
        total.append(i*j)

total.sort()
print(f'{total[-1]} {total[-2]}')
