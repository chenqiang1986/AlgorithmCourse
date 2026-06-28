# C++ `std::map` and `std::set` Basics

`std::set` and `std::map` are **ordered** containers in C++.

- `set<T>` stores unique values of type `T`
- `map<Key, Value>` stores `(key, value)` pairs with unique keys
- both containers keep elements in **sorted order**
- most common operations take `O(log n)` time

This makes them very useful when we want:

- fast insertion
- fast deletion
- fast search
- automatic sorted order
- `lower_bound` / `upper_bound`

## 1. How to insert element

### `set`

```cpp
set<int> s;

s.insert(10);
s.insert(4);
s.insert(10);  // duplicate, ignored
```

### `map`

```cpp
map<string, int> score;

score["alice"] = 95;      // insert or update
score["bob"] = 88;
score["alice"] = 99;      // updates existing key

score.insert({"cindy", 91});   // also works
```

Important:

- `set` does not allow duplicates
- `map` does not allow duplicate keys
- `mp[key]` will create the key if it does not already exist

## 2. How to query element

### `set`

```cpp
if (s.count(10)) {
    cout << "10 exists\n";
}

auto it = s.find(4);
if (it != s.end()) {
    cout << "found " << *it << "\n";
}
```

### `map`

```cpp
if (score.count("bob")) {
    cout << score["bob"] << "\n";
}

auto it = score.find("cindy");
if (it != score.end()) {
    cout << it->first << " " << it->second << "\n";
}
```

Important:

- use `count(key)` to check whether a key exists
- use `find(key)` when you want an iterator
- avoid writing `mp[key]` just to check existence, because it may insert a new key

## 3. How to delete element

### `set`

```cpp
s.erase(10);   // erase by value
```

### `map`

```cpp
score.erase("bob");   // erase by key
```

You can also erase by iterator.

```cpp
auto it = s.find(4);
if (it != s.end()) {
    s.erase(it);
}
```

## 4. How to enumerate all entries

### `set`

```cpp
for (int x : s) {
    cout << x << " ";
}
cout << "\n";
```

### `map`

```cpp
for (auto [name, value] : score) {
    cout << name << " -> " << value << "\n";
}
```

Because these are ordered containers, the loop visits entries in sorted order.

## 5. How to find the smallest entry bigger than some given key

This is where `lower_bound` and `upper_bound` are very important.

- `lower_bound(x)` = first element that is `>= x`
- `upper_bound(x)` = first element that is `> x`

### `set` example

```cpp
set<int> s = {2, 5, 8, 12};

auto it1 = s.lower_bound(6);   // points to 8
auto it2 = s.upper_bound(8);   // points to 12
```

### `map` example

For a `map`, the comparison is based on the **key**.

```cpp
map<int, string> mp;
mp[2] = "two";
mp[5] = "five";
mp[8] = "eight";

auto it = mp.lower_bound(6);   // points to key 8
```

Always check whether the iterator is `end()`.

```cpp
if (it != mp.end()) {
    cout << it->first << " " << it->second << "\n";
} else {
    cout << "no such key\n";
}
```

## Demo Code

Students can copy, paste, compile, and play with this file directly.

```cpp
#include <iostream>
#include <map>
#include <set>
#include <string>
using namespace std;

int main() {
    cout << "=== set demo ===\n";
    set<int> s;

    // 1. insert
    s.insert(10);
    s.insert(4);
    s.insert(7);
    s.insert(10);  // duplicate, ignored

    // 2. query
    cout << "Does 7 exist? " << (s.count(7) ? "yes" : "no") << "\n";
    cout << "Does 9 exist? " << (s.count(9) ? "yes" : "no") << "\n";

    auto find_it = s.find(4);
    if (find_it != s.end()) {
        cout << "Found value: " << *find_it << "\n";
    }

    // 4. enumerate
    cout << "All values in set: ";
    for (int x : s) {
        cout << x << " ";
    }
    cout << "\n";

    // 5. lower_bound / upper_bound
    int target = 6;
    auto lb = s.lower_bound(target);  // first value >= 6
    auto ub = s.upper_bound(target);  // first value > 6

    if (lb != s.end()) {
        cout << "lower_bound(" << target << ") = " << *lb << "\n";
    } else {
        cout << "lower_bound(" << target << ") = end()\n";
    }

    if (ub != s.end()) {
        cout << "upper_bound(" << target << ") = " << *ub << "\n";
    } else {
        cout << "upper_bound(" << target << ") = end()\n";
    }

    // 3. delete
    s.erase(7);
    cout << "After erasing 7: ";
    for (int x : s) {
        cout << x << " ";
    }
    cout << "\n\n";

    cout << "=== map demo ===\n";
    map<string, int> score;

    // 1. insert
    score["alice"] = 95;
    score["bob"] = 88;
    score["cindy"] = 91;
    score["alice"] = 99;  // update existing key

    // 2. query
    if (score.count("bob")) {
        cout << "bob's score = " << score["bob"] << "\n";
    }

    auto map_it = score.find("david");
    if (map_it == score.end()) {
        cout << "david is not in the map\n";
    }

    // 4. enumerate
    cout << "All entries in map:\n";
    for (auto [name, value] : score) {
        cout << name << " -> " << value << "\n";
    }

    // 5. lower_bound / upper_bound on keys
    auto lb_map = score.lower_bound("b");
    auto ub_map = score.upper_bound("bob");

    if (lb_map != score.end()) {
        cout << "lower_bound(\"b\") = " << lb_map->first
             << " -> " << lb_map->second << "\n";
    } else {
        cout << "lower_bound(\"b\") = end()\n";
    }

    if (ub_map != score.end()) {
        cout << "upper_bound(\"bob\") = " << ub_map->first
             << " -> " << ub_map->second << "\n";
    } else {
        cout << "upper_bound(\"bob\") = end()\n";
    }

    // 3. delete
    score.erase("bob");
    cout << "After erasing bob:\n";
    for (auto [name, value] : score) {
        cout << name << " -> " << value << "\n";
    }

    return 0;
}
```

## Suggested Exercises

1. Change the `set<int>` demo into `set<string>`.
2. Add more names and scores to the `map`.
3. Try `lower_bound` and `upper_bound` with different keys.
4. Print the largest value smaller than a target by moving one step left from `lower_bound`.

## Common Mistakes

- using `mp[key]` when you only want to check existence
- forgetting that `set` removes duplicates automatically
- forgetting to check `it != end()` before using `*it`
- confusing:
  - `lower_bound(x)` with first value `>= x`
  - `upper_bound(x)` with first value `> x`
