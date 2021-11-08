#ได้ 100 คะแนน
inputs = [int(x) for x in input().split()]

num = inputs[0]
energymin = inputs[1]
energymax = inputs[1]

H=[]
for i in range(num):
    H.append(int(input()))
energy_lose = []

for i in H:
    if i % 3 == 0 and i % 4 == 0:
        energy_lose.append([int(10*(i/3)), int(10*(i/4))])
    elif i % 3 == 0:
        energy_lose.append(int(10*(i/3)))
    elif i % 4 == 0:
        energy_lose.append(int(10*(i/4)))


for i in energy_lose:
    if type(i) == list:
        energymin-=max(i)
        energymax-=min(i)
    else:
        energymin-=i
        energymax-=i
print(f'{energymin} {energymax}')