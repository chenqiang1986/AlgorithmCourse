# Binary Number

## Base Change Formula
In computer, all the numbers are really represented in base 2.
Conversion between different bases.

For a number whose base2 digit represented by a list $a_i$, the value is essentially

$$
(a_{n-1}a_{n-2}...a_0)_2=\sum_{k=0}^{n-1}a_k2^k
$$

Here is the code to convert a string of base 2 representation into an integer,
but slightly different from the above formula, from time to time we have the 
leading digit persisted at the beginning of the string:

```
int get_number_base2(std::string a) {
    int result = 0;
    for (int i = 0; i < a.size(); i++) {
        result = result * 2 + (a[i] - '0');
    }
    return result;
}
```

Here is the code to convert an integer into a list of digits base2.
```
std::vector<int> to_base2(int a) {
  std::vector<int> result;
  while (a > 0) {
     result.push_back(a%2);
     a/=2;
  }
  return result;
}
```

## Bitwise Operation

Bitwise operation is just like boolean operation, but we treat each bit independently.

Example for bitwise and (&), or (1):
1. $3\\&5 = (011)_2 \\& (101)_2 = (001)_2 =1$
2. $3|5 = (011)_2 | (101)_2 = (111)_2 =7$

Example for bitwise xor (^):
xor is essentially addition with overflow neglected.
1. $3$ ^ $5 = (011)_2$ ^ $(101)_2 = (110)_2 =6$

## Practice
2026 Third Bronze 3rd: https://usaco.org/index.php?page=viewproblem2&cpid=1588
- Q: Can you figure out the pattern on the chain $f(x), f(f(x)), f(f(f(x)))....$ if we only collect the number that contains 0 or 1.
2026 Second Bronze 3rd: https://usaco.org/index.php?page=viewproblem2&cpid=1565
