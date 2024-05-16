N = int(input())
channels = list(input() for _ in range(N))

kbs1_idx, kbs2_idx = channels.index("KBS1"), channels.index("KBS2")

if kbs2_idx < kbs1_idx:
    kbs2_idx += 1

ans = ""
ans += kbs1_idx * "1" + kbs1_idx * "4"
ans += kbs2_idx * "1" + (kbs2_idx - 1) * "4"

print(ans)