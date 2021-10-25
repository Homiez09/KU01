#ได้ 100 คะแนน
tree = int(input())
height = [int(x) for x in input().split()]

bird = 0

for i in range(tree):
    if i == 0:
        if height[i] > height[i+1]:
            bird += 1
    elif i == tree -1:
        if height[i] > height[i-1]:
            bird += 1
    elif height[i] > height[i-1] and height[i] > height[i+1]:
        bird += 1
        
print(bird)