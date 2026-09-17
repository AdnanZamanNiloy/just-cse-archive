#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n, m;
    cin >> n >> m;

    vector<pair<int, pair<int, int>>> p;

    for (int i = 0; i < m; i++)
    {
        int u, v, w;
        cin >> u >> v >> w;
        p.push_back({w, {u, v}});
    }

    sort(p.begin(), p.end()); // sort edges based on weight

    for (auto &edge : p)
    {
        cout << "Node1: " << edge.second.first << ", Node2: " << edge.second.second << ", Weight: " << edge.first << "\n";
    }

    return 0;
}
