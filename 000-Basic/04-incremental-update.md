# Incremental Update Strategy

In previous lesson, we learned the conception **index** using partial result maintenance as example.
From time to time, we might need to update the index for reasons like 

1. The data isn't static, there is update to the data.
2. We are not able to store the whole index, but only a portion of it, and we need to update the portion based on different uses.

# Practice
1. 2026 Bronze First 3rd https://usaco.org/index.php?page=viewproblem2&cpid=1541
   - Q1: What index we can build so that we can get the sum of KxK square without taking addition of every number again and again?
   - Q2: If $attactive[i,j]$ changes, how many entries in the index need to be updated?
   - Q3: How should we update the max beauty value?
2. 2025 Jan Bronze 2nd https://usaco.org/index.php?page=viewproblem2&cpid=1468
   - Q1: What index we can build so that if I take $a[i]$ as the first letter, I can quickly calculate the number of "moo"s with $a[i]$ being the "m"?
   - Q2: Can we persist such index in the memory for all $a[i]$ simultaneously? Do we need that?
   - Q3: If we have the index for $a[i]$, can we quickly build it for $a[i-1]$ or $a[i+1]$?
3. 2025 Jan Bronze 3rd https://usaco.org/index.php?page=viewproblem2&cpid=1469
   - Q1: If we enumerate all $l, r$ possibilities and do flipping and counting, what's the time complexity?
   - Q2: It seems the brute force method was re-doing the same counting again and again. Can you identify two pairs of $l, r$,
        such that the counting between $flip(a, l1, r1)$ with $b$ and $flip(a, l2, r2)$ with $b$ is almost the same, with slightly difference.
   - Q3: Can you figure out a method to reuse the same counting, and thus improve performance?
