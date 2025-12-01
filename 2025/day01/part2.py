import sys

cur = 50
ans = 0
for s in sys.stdin:
    rot = int(s[1:])
    if s[0] == 'L':
        if cur > 0 and cur - rot % 100 <= 0: ans += 1
        cur -= rot % 100
        cur = (cur + 100) % 100
        
        ans += rot // 100 
    else:
        cur += rot % 100
        if cur >= 100: ans += 1
        cur %= 100
        
        ans += rot // 100

print(ans)
