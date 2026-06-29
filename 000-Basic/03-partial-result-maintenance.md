# Partial Result Maintenance - Linear Based
## Questions
From time to time we may need to answer the following questions repeatedly:
1. Given array $a$, what is the sum of $a[i..j]$
2. Given array $a$, what is the min/max of $a[0..i]$ or $a[i:]$
   - For generic question on $a[i..j]$, we need tree based optimization. Will cover later.
3. Given an array of points $a={(x_i, y_i)}$ and X, what is the y min/max value for $x_i > X$.
4. Given an array of points $a={(x_i, y_i)}$ and $X_1$, $X_2$, what is the sum of y values for $x_i \in [X_1, X_2]$. 

Typically in a problem, the array is given and fixed, but it may have tons of queries for you to process. 
If we use brute force method to scan all the data we need for each query, the efficiency is not good enough.

## Basic Principle
The basic principle for these kind of problem is to
1. Preprocess the data and store the partial result in some data structure. (We call such data as **index**.)
2. Use **index** to quickly get the answer to the query.

## Solution
1. Given array $a$, what is the sum of $a[i..j]$
   - Define vector $A[i]=\sum_{k=0}^{i}{a[k]}$
   - Easy to see $A[i] = A[i-1]+a[i]$
   - Then $\sum_{k=i}^{j}{a[k]} = A[j] - A[i-1]$
2. Given array $a$, what is the min/max of $a[0..i]$ or $a[i:]$
   - Take max of $a[i:]$ as example.
   - Define vector $A[i] = max_{k=i}^{n-1}(a[k])$
   - Easy to see $A[i] = max(A[i+1], a[i])$
3. Given an array of points $a={(x_i, y_i)}$ and X, what is the y min/max value for $x_i \ge X$.
   - Take max for example.
   - Sort $a$ based on $x_i$ as primary key,  $y_i$ as secondary key.
   - Define map $A[x_i] = max_{k=i}^{n-1}(y_i)$
   - Easy to see $A[x_i] = max(y_i, A[x_{i+1}])$ (Check if $x_i==x_{i-1}$, there is no problem.)
   - For given $X$ that may not appear as a x coordinate of some point in $a$: $A.lower\\_bound(X).second$ gives us the solution.
4. Given an array of points $a={(x_i, y_i)}$ and $X_1$, $X_2$, what is the sum of y values for $x_i \in [X_1, X_2]$.
   - Sort $a$ based on $(x_i, y_i)$ in lexicographic order.
   - Define map $A[x_i] = \sum_{k=0}^{i}y_i$
   - Easy to see $A[x_i] = A[x_{i-1}] + y_i$ (Check if $x_i==x_{i-1}$, there is no problem.)
   - For given $X_1$ $X_2$, result is $$(A.upper\\_bound(X_2) -1).second - (A.lower\\_bound(X_1)-1).second$$
