#ได้ 100 คะแนน
inputs = [int(x) for x in input().split()]

z = []

for i in range(inputs[0]):
    distance = [int(x) for x in input().split()]
    diff = []
    for j in range(inputs[1]):
        if j == 0:
            diff.append(distance[0])
        else:
            diff_find = distance[j] - distance[j-1]
            diff.append(diff_find)
    diff.sort()
    z.append(diff[-1])

z.sort()
print(z[0])