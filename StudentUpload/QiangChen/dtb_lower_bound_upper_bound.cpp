#include<iostream>
#include<set>

std::string smallest_greater_than_or_equal_to(
    const std::set<int> a,
    int t
) {
    auto it = a.lower_bound(t);
    if (it == a.end()) {
        return "N";
    }
    return std::to_string(*it);
}


std::string smallest_greater_than(
    const std::set<int> a,
    int t
) {
    auto it = a.upper_bound(t);
    if (it == a.end()) {
        return "N";
    }
    return std::to_string(*it);
}

std::string biggest_less_than_or_equal_to(
    const std::set<int> a,
    int t
) {
    auto it = a.upper_bound(t);
    if (it == a.begin()) {
        return "N";
    }
    it--;
    return std::to_string(*it);
}


std::string biggest_less_than(
    const std::set<int> a,
    int t
) {
    auto it = a.lower_bound(t);
    if (it == a.begin()) {
        return "N";
    }
    it--;
    return std::to_string(*it);
}

int main() {
    int n, q;
    std::cin >> n >> q;

    std::set<int> a;
    for (int i = 0; i < n ;i++) {
        int num;
        std::cin >> num;
        a.insert(num);
    }

    for (int i = 0; i < q; i++) {
        int t;
        std::cin >> t;

        std::cout << smallest_greater_than_or_equal_to(a, t) << " ";
        std::cout << smallest_greater_than(a, t) << " ";
        std::cout << biggest_less_than_or_equal_to(a, t) << " ";
        std::cout << biggest_less_than(a, t) << std::endl;
    }
}
