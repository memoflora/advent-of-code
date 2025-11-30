#include <bits/stdc++.h>
using namespace std;

int main() {
    string line, s = "";
    while (getline(cin, line)) s += line;

    int n = s.length(); 
    vector<int> v;
    for (int i = 0; i < n; i++) {
        if (i + 7 < n and s.substr(i, 4) == "mul(") {
            v.push_back(i + 4); 
        }
    }

    int ans = 0;
    for (auto pos : v) {
        bool com = 0, par = 0;
        int x = -1, y = -1;
        for (int i = pos; i < n; i++) {
            if (s[i] == ')') {
                par = 1;
                break;
            }
            if (s[i] == ',') {
                if (!com && x != -1) {
                    com = 1;
                    continue;
                } else {
                    break;
                }
            }
            if (!isdigit(s[i])) break;

            if (!com) {
                x = (x == -1 ? 0 : x);
                x = x * 10 + (s[i] - '0');
            } else {
                y = (y == -1 ? 0 : y); 
                y = y * 10 + (s[i] - '0');
            }
        }

        ans += (!par || x == -1 || y == -1 || x > 999 || y > 999 ? 0 : x * y);
    }

    cout << ans << '\n';
}
