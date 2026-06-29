# Partial Result Maintenance - Linear Based
## Questions
From time to time we may need to answer the following questions repeatedly:
1. Given array $a$, what is the sum of $a[i..j]$
2. Given array $a$, what is the min/max of $a[0..i]$ or $a[i:]$
   - For generic question on $a[i..j]$, we need tree based optimization. Will cover later.
3. Given an array of points $a={(x_i, y_i)}$ and X, what is the y min/max value for $x_i > X$.
4. Given an array of points $a={(x_i, y_i)}$ and $X_1$, $X_2$, what is the sum of y values for $x_i \in [X_1, X_2]$. 
