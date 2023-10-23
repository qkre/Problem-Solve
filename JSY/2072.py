n = int(input())

for i in range(n):
    arr = list(map(int, input().split()))
    sum = 0
    for j in arr:
        if j % 2 == 1:
            sum += j
            
    
    print(f"#{i+1} {sum}")