import sys

cur = 50
ans = 0
for s in sys.stdin:
    rot = int(s[1:]) % 100
    if s[0] == 'L':
        cur = cur - rot + 100
        cur %= 100
    else:
        cur += rot
        cur %= 100

    if cur == 0: ans += 1

print(ans)
