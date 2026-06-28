#include <iostream>
#include <map>
#include <vector>
#include <set>

// We will calculate the # of operations
// to move all A[i] to A[l] if interpreting 
// the modulo M by [base, base + M - 1]
struct Param {
    int l;
    int base;

    // Stores the # of A[i] less than A[l]
    // in [base, base + M - 1]
    int le_count;

    // Stores the # of A[i] bigger than A[l]
    // in [base, base + M - 1]
    int gt_count;

    int operations;
};

std::vector<int> make_3_cover(std::vector<int> a, int m) {    
    for (int i = 0; i< a.size(); i++) {
        a[i] = a[i]%m;        
    }

    std::sort(a.begin(), a.end());
    std::vector<int> a_expand (a.size() * 3, 0);

    for (int i = 0; i< a.size(); i++) {
        a_expand[i] = a[i] - m;
        a_expand[i+a.size()] = a[i];
        a_expand[i+a.size()*2] = a[i] +m;
    }
    return a_expand;
}


Param move_param_rebase(const Param& input, const std::vector<int>& a_expand, int m, int n, int new_base) {
    Param result {
        .l = input.l,
        .base = new_base,

        .le_count = input.le_count, // TBD
        .gt_count = input.gt_count, // TBD
        .operations = input.operations // TBD
    };

    for (
        int i = input.l - input.le_count;
        a_expand[i] < result.base; 
        i++) {
            result.le_count --;
            result.gt_count ++;
            result.operations -= a_expand[result.l] - a_expand[i];
            result.operations += a_expand[i+n] - a_expand[result.l];
    }
    return result;    
}

Param move_param_l_by_1(Param input, const std::vector<int>& a_expand, int m, int n) {
    if (input.gt_count == 0) {
        input = move_param_rebase(input, a_expand, m, n, a_expand[input.l+1]-m+1);
    }

    Param result {
        .l = input.l + 1,
        .base = input.base,

        .le_count = input.le_count + 1, 
        .gt_count = input.gt_count - 1, 
        .operations = input.operations + (a_expand[input.l + 1] - a_expand[input.l]) * (input.le_count + 1 - input.gt_count)
    };
    return result;
}

std::vector<Param> calculate_operations(
    const std::vector<int>& a_expand,
    int m,
    int n
) {
    Param init_param{
        .l = n-1,
        .base = -m,
        .le_count =n-1,
        .gt_count =0,
        .operations =0 // TBD
    };

    for (int i = 0; i < n; i++) {
        init_param.operations += a_expand[init_param.l] - a_expand[i];
    }

    std::vector<Param> result;
    result.push_back(init_param);

    for (int i = n; i< n+n; i++) {
        result.push_back(move_param_l_by_1(result.back(), a_expand, m, n));       

        result.push_back(move_param_rebase(result.back(), a_expand, m, n, a_expand[result.back().l]-m/2));
    }

    return result;
}


int main() {
    int m = 20;
    std::vector<int> a({5,10,15,1});

    std::vector<int> a_expand = make_3_cover(a, m);

    std::vector<Param> param_to_steps = calculate_operations(
        a_expand,
        m,
        a.size()
    );

    for (int v: a_expand) {
        std::cout << v << " ";
    }
    std::cout << std::endl;

    for (const Param& p : param_to_steps) {
        std::cout << a_expand[p.l] << " [" << p.base << "," <<(p.base+m-1) << "] le_count=" 
           << p.le_count << " gt_count=" << p.gt_count << " op=" << p.operations << std::endl;
    }

}