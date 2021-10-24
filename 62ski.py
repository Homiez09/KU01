#ได้ 100 คะแนน
mode = [int(x) for x in input().split()]

L = int(mode[0])
M = int(mode[1])
N = int(mode[-1])

if L>=1 and L<=20 and M>=1 and M<=20 and N>=0 and N<=100:
    control = []
    for i in range(N):
        inputControl = [int(x) for x in input().split()]  
        control.append(inputControl)
    for i in range(N):
        start = [L,0]

        for j in control[i]:
            if j == 0:
                start[0] = start[0] - 1
            if j == 1:
                start[0]= start[0] + 1
            if start[0] < 0 or start[0] > L*2:
                break
        
        if start[0] < 0 or start[0] > L*2:
            print(0)
        else:
            print(1)
