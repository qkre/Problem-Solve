# 개 그지 같은 문제.

from sys import stdin
input = stdin.readline

N = int(input())

def binary_search(num, right):
    lo, hi = 0, right

    while lo < hi:
        mid = (lo + hi) // 2

        if sorted_wire[mid][1] < num:
            lo = mid + 1
        else:
            hi = mid

    return hi

wire = []
for _ in range(N):
    s, e = map(int, input().split())
    wire.append((s, e))

wire.sort(key=lambda x:x[0])

sorted_wire = []
record = []

sorted_wire.append(wire[0])
record.append(0)
count = 1

for i in range(1, N):
    if sorted_wire[-1][1] < wire[i][1]:
        sorted_wire.append(wire[i])
        record.append(count)
        count +=1
    else:
        idx = binary_search(wire[i][1], count)
        sorted_wire[idx] = wire[i]
        record.append(idx)

print(sorted_wire)
print(record)

print(N-count)
link_set = set()
find_idx = count - 1
for idx, inserted_idx in enumerate(record[::-1]):
    if inserted_idx == find_idx:
        link_set.add(N - idx - 1)
        find_idx -= 1
    if find_idx < 0:
        break

for i in range(N):
    if i not in link_set:
        print(wire[i][0])

