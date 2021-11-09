#ได้ 100 คะแนน
inputs = [int(x) for x in input().split()]
N = inputs[0]
H = inputs[1]

robotH = []
for i in range(N):
    robotH.append(int(input()))
 
robotH.sort()

result = list(filter(lambda x : x <= H, robotH))
print(result[-1])