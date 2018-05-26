n = int(input())

datalist = [int(x) for x in input().split()]

# index = datalist[0]
# j = n - 1
# i = 0
# while i < j:
#     if datalist[i] <= index:
#         i = i + 1
#     else:
#         j = j - 1
#         datalist[i],datalist[j] = datalist[j],datalist[i]

i = 1
k = n
while i < k:
    if datalist[i] > datalist[0]:
        datalist.remove(datalist[i])
        k = k - 1
    else:
        i = i + 1
    
        

res = len(datalist)

k = 0
while k <= 20:
    if 2**k < res:
        k = k + 1
    else:
        break

print(k)