arr = [4,3,2,7,8,2,3,1]
set1 = set()
set2 = set()

for i in arr:
    if i in set1:
        set2.add(i)
    else:
        set1.add(i)

lst = list(set2)
print(lst)