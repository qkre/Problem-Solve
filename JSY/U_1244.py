import sys
from collections import deque, Counter

sys.stdin = open("input/1244_input.txt")

t = int(input())

for i in range(t):
    money, change = input().split()
    cnt = 0
    temp = ""
    money = deque(money)

    while cnt < int(change):
        # 가장 큰 값이 처음있을때
        if max(money) == money[0]:
            temp += money[0]
            money.popleft()

        else:
            reversed_lst = list(money)[::-1]
            index_from_end = reversed_lst.index(money[money.index(max(money))])
            act_index = len(money) - 1 - index_from_end
            a = money[act_index]
            if len(money) >= 2 and money[0] < money[1]:
                money[act_index] = money[0]
                money[0] = a
                temp += money[0]
                money.popleft()
            else:
                w = money[act_index]
                money.remove(money[act_index])
                money.appendleft(w)
            cnt += 1

        if len(money) == 0 and cnt < int(change):
            count = Counter(temp).most_common(1)
            if count[0][1] > 1:  # 같은 요소가 2개면 break
                break
            # else: 아니면 맨 뒤에 2개 씩 바꾸면서 cnt += 1 cnt랑 change 같으면 break
            else:
                temp_list = list(temp)
                temp_list[-2], temp_list[-1] = temp_list[-1], temp_list[-2]
                cnt += 1
                temp = "".join(temp_list)

        if cnt == int(change) and len(money) > 0:
            for i in money:
                temp += i

        if len(money) == 0:
            break

    print(temp)
