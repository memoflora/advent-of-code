#include <bits/stdc++.h>
using namespace std;

int main() {
    map<int, int> mp[2];
    int x, y;
    while (cin >> x >> y) {
        mp[0][x]++;
        mp[1][y]++;
    }

    long long ans = 0;
    for (auto [x, y] : mp[0]) {
        ans += (long long) x * y * mp[1][x];
    }
    
    cout << ans << '\n';
}
