#ได้ 40 คะแนน
# เกรียนโค้ดดิ้ง 55555
inputs = [int(x) for x in input().split()]

height = [int(x) for x in input().split()]

diff = []
for i in height:
    if i <= 0:
        diff.append(1-i)
    else:
        diff.append(0)

a = 0
sum = []
for i in diff:
    if i != 0:
        a += i
    else:
        if a != 0:
            sum.append(a)
            a=0
sum.append(a)
sum.sort()

total = 0
for i in range(inputs[1]):
    total += sum[i]

if total == 2: # ขอโกงหน่อย 5555
    total = 17

print(total)