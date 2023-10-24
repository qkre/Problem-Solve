import sys

sys.stdin = open("input/1206_input.txt")

for i in range(10):
    n = int(input())
    arr = list(map(int, input().split()))
    ret = 0
    
    if arr[0] > arr[1] and arr[0] > arr[2]:
        ret += arr[0] - max(arr[1], arr[2])
        
    if arr[1] > arr[0] and arr[1] > arr[2] and arr[1] > arr[3]:
        ret += arr[1] - max(arr[0], arr[2], arr[3])
        
    if arr[len(arr) - 1] > arr[len(arr) - 2] and arr[len(arr) - 1] > arr[len(arr) - 3]:
        ret += arr[len(arr) - 1] - max(arr[len(arr) - 2],arr[len(arr) - 3])
        
    if arr[len(arr) - 2] > arr[len(arr) - 3] and arr[len(arr) - 2] > arr[len(arr) - 4] and arr[len(arr) - 2] > arr[len(arr) - 1]:
        ret += arr[len(arr) - 2] - max(arr[len(arr) - 1], arr[len(arr) - 3], arr[len(arr) - 4])
        
    for j in range(2, len(arr)-2):
        if arr[j] > arr[j-2] and arr[j] > arr[j-1] and arr[j] > arr[j+1] and arr[j]> arr[j+2]:
            ret += arr[j] - max(arr[j-2], arr[j-1], arr[j+1], arr[j+2])
            
    print(f"#{i+1} {ret}")