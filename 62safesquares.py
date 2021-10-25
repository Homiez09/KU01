#ได้ 20 คะแนน
mode = [int(x) for x in input().split()]

N = mode[0]%25621
M = mode[1]%25621
K = mode[-1]

enemys = []
for i in range(K):
    inputEnemys = [int(x) for x in input().split()]  
    enemys.append(inputEnemys)

field = []
[field.append((i+1,j+1)) for j in range(M) for i in range(N)]

redzone = []
for i in range(len(enemys)):
    [redzone.append((j+1,enemys[i][1])) for j in range(N)]
    [redzone.append((enemys[i][0],j+1)) for j in range(M)]

greenzone = list(set(field)-set(redzone))
print(len(greenzone))