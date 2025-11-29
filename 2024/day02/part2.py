import sys

def main():
    ans = 0
    for s in sys.stdin:
        a = list(map(int, s.split()))
        
        ok = False
        for i in range(len(a)):
            b = a[:i] + a[i + 1:]
            if all(1 <= b[i + 1] - b[i] <= 3 for i in range(len(b) - 1)):
                ok = True
                break

            if all(1 <= b[i] - b[i + 1] <= 3 for i in range(len(b) - 1)):
                ok = True
                break

        if ok: ans += 1

    print(ans)

if __name__ == '__main__':
    main()
