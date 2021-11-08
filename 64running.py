#ได้ 87 คะแนน
inputs = [int(x) for x in input().split()]
race = []
o = inputs[1]
p = inputs[0]
for i in range(p):
    race.append(int(input()))
race.sort()
t = min(race)
z = 0
point = t*o
for i in race:
    if i*(o)-t <= point:
        z+=1

print(z)
