#ได้ 100 คะแนน
inputs = [int(i) for i in input().split()]
l = inputs[0]
w = inputs[1]
n = inputs[2]

test = []

for i in range(w):
    test.append([])
    for j in range(l):
        test[i].append(0)
            
for i in range(n):
    abcd = [int(i) for i in input().split()]
    a = abcd[0]
    c = abcd[2]
    d = abcd[3]
        
    for j in range(c-a):
        b = abcd[1]
        a+=1    
        for k in range(d-b):
            b+=1
            
            test[b-1][a-1]=1

ans = 0            
for i in range(w-2):
    for j in range(l-2):
        if test[i][j] + test[i][j+1] + test[i][j+2] == 0:
            if test[i+1][j] + test[i+1][j+1] + test[i+1][j+2] == 0:          
                if test[i+2][j] + test[i+2][j+1] + test[i+2][j+2] == 0:       
                    ans += 1    
    
print(ans)
