import sys

def main():
    ans = 0
    for s in sys.stdin:
        a = list(map(int, s.split()))
        if all(1 <= a[i + 1] - a[i] <= 3 for i in range(len(a) - 1)):
            ans += 1
            continue

        if all(1 <= a[i] - a[i + 1] <= 3 for i in range(len(a) - 1)):
            ans += 1
            continue

    print(ans)

if __name__ == '__main__':
    main()
