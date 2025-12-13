s = input()
v = s.split(',')

ans = 0
for p in v:
    l, r = p.split('-')
    lenl, lenr = len(l), len(r) 
    l, r = int(l), int(r)

    if lenl == lenr and lenl % 2 == 0:
        fac = 10 ** (lenl // 2) + 1
        lf = (l + fac - 1) // fac
        rg = r // fac
        ans += fac * (lf + rg) * (rg - lf + 1) // 2

        continue

    for i in range(lenl + 1, lenr):
        if i & 1: continue

        fac = 10 ** (i // 2) + 1
        lf = 10 ** (i // 2 - 1)
        rg = 10 ** (i // 2) - 1
        ans += fac * (lf + rg) * (rg - lf + 1) // 2
    
    if lenl % 2 == 0:
        fac = 10 ** (lenl // 2) + 1
        lf = (l + fac - 1) // fac
        rg = 10 ** (lenl // 2) - 1
        ans += fac * (lf + rg) * (rg - lf + 1) // 2

    if lenr % 2 == 0:
        fac = 10 ** (lenr // 2) + 1
        lf = 10 ** (lenr // 2 - 1)
        rg = r // fac
        ans += fac * (lf + rg) * (rg - lf + 1) // 2

print(ans)
