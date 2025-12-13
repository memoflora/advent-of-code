def get(sz, l, r):
    cnt, ret = {}, 0
    for seq in range(1, sz // 2 + 1):
        if sz % seq != 0: continue

        rep, fac = sz // seq, 1
        for i in range(rep - 1):
            fac = fac * (10 ** seq) + 1
        
        lf = (l + fac - 1) // fac
        rg = r // fac
        tmp = fac * (lf + rg) * (rg - lf + 1) // 2

        for k, v in cnt.items():
            if seq % k == 0:
                ret -= v

        cnt[seq] = tmp
        ret += cnt[seq]

    return ret

def main():
    s = input()
    v = s.split(',')

    ans = 0
    for p in v:
        l, r = p.split('-')
        lenl, lenr = len(l), len(r) 
        l, r = int(l), int(r)

        if lenl == lenr:
            ans += get(lenl, l, r)     
            continue

        ans += get(lenl, l, 10 ** lenl - 1)
        for sz in range(lenl + 1, lenr):
            ans += get(sz, 10 ** (sz - 1), 10 ** sz - 1)
        
        ans += get(lenr, 10 ** (lenr - 1), r)
           
    print(ans)

if __name__ == '__main__':
    main()
