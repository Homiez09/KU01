#ได้ 30 คะแนน
inputs = [int(x) for x in input().split()]

min_row = []
max_row = []
table = []
for i in range(inputs[0]):
    inputnum = [int(x) for x in input().split()]
    min_row.append(min(inputnum))
    max_row.append(max(inputnum))

""" print(min_row)
print(max_row)
print(min(min_row))
print(max(max_row)) """

for i in range(inputs[0]):
    if min_row[i] == min(min_row) and max_row[i] == max(max_row):      
        a = min_row.sort() 
        c = []
        for j in range(1, inputs[0]):
            if min_row[j] - inputs[1] < min(min_row):
                c.append(min_row[j])
        if c == []:
            ans=max(max_row) - min(min_row)
            print(ans)
            break
        else:
            ans=(max(max_row)+inputs[1]) - (min(c)-inputs[1])
            print(ans)
            break
    else:
        ans = (max(max_row)+inputs[1])-(min(min_row)-inputs[1])
        print(ans)
        break

