#ได้ 100 คะแนน
num = int(input())
if num >= 0 and num <= 1000:
    long = []
    for i in range(num):
        long.append(int(input()))
    long.sort()

    total = []
    for i in range(len(long)):
        total.append(sum(long[:i+1])*2)
    print(sum(total))

