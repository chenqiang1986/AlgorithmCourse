#include <iostream>
#include <vector>

int main() {
    long long n, q;
    std::cin >>n >> q;

    std::vector<long long> a(n,0);
    for(long long i = 0; i < n; i++) {
        std::cin >> a[i];
    }

    std::vector<long long> prefix_sum(n,0);
    prefix_sum[0] =a[0];
    for(long long i = 1; i < n; i++) {
        prefix_sum[i] = prefix_sum[i-1] + a[i];
    }

    for (long long i = 0; i < q; i++) {
        long long start, stop;
        std::cin >> start >> stop;
        start--;
        stop--;

        long long sum = (start == 0) ? prefix_sum[stop] : prefix_sum[stop] - prefix_sum[start -1]; 
        std::cout << sum << std::endl;
    }
}