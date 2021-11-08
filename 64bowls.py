#ได้ 100 คะแนน
num = int(input())

bowls = []
for i in range(num):
    bowls.append(int(input()))

bowls.sort()

#find = set([x for x in bowls if bowls.count(x) > 1])

def most_frequent(List):
    return max(set(List), key = List.count)

key = most_frequent(bowls)


x=0
for i in bowls:
    if key == i:
        x +=1

print(x)



""" for i in range(num-1):
    if bowls[i+1] != bowls[i] """
