from collections import Counter

t = int(input())
for i in range(t):
    idx =int(input())
    
    score = sorted(list(map(int, input().split())), reverse=True)
    print(f"#{idx} {Counter(score).most_common(1)[0][0]}")