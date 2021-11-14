#ได้ 100 คะแนน
inputs = [int(x) for x in input().split()]

N = inputs[0]
K = inputs[1]
T = inputs[2]

round = 0
z = 0
c = 1

while z != 1:
    c += K
    if c > N:
        c-=N
    round += 1
    if c == T:
        round += 1
        break 
    if c == 1:
        z=1
print(round)
