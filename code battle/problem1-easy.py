# given a square matrix, sum of primary and secondary diagonal elements
# lst = [[1,2,3,4],
#        [4,5,6,7],
#        [7,8,9,10],
#        [12,3,14,15]]

lst = [[1,2,3],
       [4,5,6],
       [7,8,9]]

n = len(lst)

sum = 0
if(n % 2 == 0):
    for i in range(n):
            for j in range(len(lst[i])):
                if(i == j):
                    sum = sum + lst[i][j]
                    sum = sum + lst[i][n-i-1]
else:
    for i in range(n):
            for j in range(len(lst[i])):
                if(i == j):
                    sum = sum + lst[i][j]
                    sum = sum + lst[i][n-i-1]
    sum -= lst[n//2][n//2]
    
    

print(sum)
            
