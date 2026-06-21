#include <iostream>
#include <vector>
#include <map>

int main() {
    int n, q;

    std::cin >> n >> q;

    std::vector<int> a (n,0);
    for (int i = 0; i < n; i++) {
        std::cin >> a[i];
    }

    std::sort(a.begin(), a.end());

    // value_to_precount[v] stores the number of elements smaller than or equal to v.
    std::map<int, int> value_to_precount;
    for (int i = 0; i< n; i++) {
        value_to_precount[a[i]] = i+1;
    }

    for (int i = 0; i < q; i++) {
        int t;
        std::cin >> t;

        auto it = value_to_precount.upper_bound(t);
        if (it == value_to_precount.begin()) {
            std::cout << 0 << std::endl;
            continue;
        }

        it--;
        std::cout << it->second << std::endl;
    }
}
