# Homework: Bézout's Identity and Linear Congruences
*AMC / Number Theory*

This homework accompanies [Lesson 5](./05-bezouts-identity-and-linear-congruences.md).
When using the extended Euclidean algorithm, show the division equations and enough
back-substitution to justify each inverse or Bézout identity. Report residues in their
least nonnegative form unless the problem asks for all solution classes.

## Part A: Bézout's Identity and Integer Equations

### Problem 1

Use the extended Euclidean algorithm to write $1$ as an integer combination of $43$
and $17$.

<details>
<summary>Solution</summary>

$$43=17\cdot2+9,\qquad17=9\cdot1+8,\qquad9=8\cdot1+1.$$

Working backward,

$$1=9-8=9-(17-9)=2(43-2\cdot17)-17.$$

Thus

$$\boxed{1=2\cdot43-5\cdot17.}$$

</details>

### Problem 2

Use the extended Euclidean algorithm to write $1$ as a linear combination of $84$
and $31$. Hence find $31^{-1}\pmod {84}$.

<details>
<summary>Solution</summary>

$$84=31\cdot2+22,\quad31=22+9,\quad22=9\cdot2+4,\quad9=4\cdot2+1.$$

Back-substitution gives

$$\begin{aligned}
1&=9-2\cdot4\\
 &=5\cdot9-2\cdot22\\
 &=5\cdot31-7\cdot22\\
 &=19\cdot31-7\cdot84.
\end{aligned}$$

Therefore $19\cdot31\equiv1\pmod {84}$, so

$$\boxed{31^{-1}\equiv19\pmod {84}.}$$

</details>

### Problem 3

Find one integer solution to $35x+22y=1$.

<details>
<summary>Solution</summary>

$$35=22+13,\quad22=13+9,\quad13=9+4,\quad9=2\cdot4+1.$$

Back-substitution gives

$$1=8\cdot22-5\cdot35.$$

Thus one solution is

$$\boxed{(x,y)=(-5,8).}$$

</details>

### Problem 4

Does $18x+30y=7$ have an integer solution? Justify your answer.

<details>
<summary>Solution</summary>

$$\gcd(18,30)=6.$$

An integer solution exists only if $6\mid7$, which is false. Therefore

$$\boxed{\text{there is no integer solution}.}$$

</details>

## Part B: Inverses and Linear Congruences

### Problem 5

Find $11^{-1}\pmod {37}$ using the extended Euclidean algorithm.

<details>
<summary>Solution</summary>

$$37=11\cdot3+4,\qquad11=4\cdot2+3,\qquad4=3+1.$$

Thus

$$1=4-3=3\cdot37-10\cdot11.$$

So $-10$ is an inverse of $11$ modulo $37$. Its least nonnegative representative is

$$\boxed{11^{-1}\equiv27\pmod {37}.}$$

</details>

### Problem 6

Solve $13x\equiv7\pmod {31}$.

<details>
<summary>Solution</summary>

The Euclidean algorithm and back-substitution give

$$1=12\cdot13-5\cdot31.$$

Thus $13^{-1}\equiv12\pmod {31}$. Multiply both sides of the congruence by $12$:

$$x\equiv12\cdot7=84\equiv\boxed{22}\pmod {31}. $$

</details>

### Problem 7

Solve $8x\equiv14\pmod {30}$, giving all solutions modulo $30$.

<details>
<summary>Solution</summary>

Since $\gcd(8,30)=2$ and $2\mid14$, solutions exist. Divide the congruence and
modulus by $2$:

$$4x\equiv7\pmod {15}.$$

Because $4^{-1}\equiv4\pmod {15}$,

$$x\equiv4\cdot7=28\equiv13\pmod {15}.$$

There are two solutions modulo $30$:

$$\boxed{x\equiv13\text{ or }28\pmod {30}.}$$

</details>

### Problem 8

Does $12x\equiv9\pmod {18}$ have a solution? Explain.

<details>
<summary>Solution</summary>

$$\gcd(12,18)=6,$$

but $6\nmid9$. Hence

$$\boxed{\text{the congruence has no solution}.}$$

</details>

### Problem 9

Solve $21x\equiv14\pmod {35}$, listing every solution modulo $35$.

<details>
<summary>Solution</summary>

Here $\gcd(21,35)=7$, and $7\mid14$. Divide by $7$:

$$3x\equiv2\pmod5.$$

Since $3^{-1}\equiv2\pmod5$, we get $x\equiv4\pmod5$. The seven solutions modulo
$35$ are

$$\boxed{x\equiv4,9,14,19,24,29,34\pmod {35}.}$$

</details>

### Problem 10

A student cancels the $6$ in $6x\equiv6\pmod {15}$ and concludes that
$x\equiv1\pmod {15}$. Explain the error and find every solution modulo $15$.

<details>
<summary>Solution</summary>

The number $6$ has no inverse modulo $15$, since $\gcd(6,15)=3$, so it cannot be
cancelled while keeping modulus $15$. Divide the entire congruence and modulus by $3$:

$$2x\equiv2\pmod5.$$

This gives $x\equiv1\pmod5$. Therefore the solutions modulo $15$ are

$$\boxed{x\equiv1,6,11\pmod {15}.}$$

</details>

## Part C: Structure and Applications

### Problem 11

Find the least nonnegative residue of $x$ satisfying $23x\equiv1\pmod {101}$.

<details>
<summary>Solution</summary>

$$101=23\cdot4+9,\quad23=9\cdot2+5,\quad9=5+4,\quad5=4+1.$$

Back-substitution gives

$$1=22\cdot23-5\cdot101.$$

Thus

$$\boxed{x=22.}$$

</details>

### Problem 12

Suppose $d=\gcd(a,n)$ and $d\mid b$. Explain why every solution to
$ax\equiv b\pmod n$ remains a solution after adding $n/d$ to $x$.

<details>
<summary>Solution</summary>

If $x$ is a solution, then

$$a\left(x+\frac nd\right)=ax+\frac{an}{d}.$$

Because $d\mid a$, write $a=da'$. Then $an/d=a'n$, which is divisible by $n$.
So adding $n/d$ to $x$ does not change $ax$ modulo $n$. Hence the new value is also
a solution.

</details>

## Part D: Challenge

### Problem 13

Find all integer solutions to $26x+39y=13$.

<details>
<summary>Solution</summary>

One solution is $x=2$, $y=-1$, since $26(2)+39(-1)=13$. Divide the equation by $13$:

$$2x+3y=1.$$

All integer solutions are

$$\boxed{x=2+3t,\qquad y=-1-2t\qquad(t\in\mathbb Z).}$$

Indeed, substituting gives $2(2+3t)+3(-1-2t)=1$.

</details>

### Problem 14

Prove that if $\gcd(a,n)=1$, then the modular inverse of $a$ modulo $n$ is unique
modulo $n$.

<details>
<summary>Solution</summary>

Suppose $u$ and $v$ are both inverses. Then

$$au\equiv1\pmod n\qquad\text{and}\qquad av\equiv1\pmod n.$$

Subtracting gives $a(u-v)\equiv0\pmod n$. Since $a$ has an inverse modulo $n$,
multiply by it to obtain $u-v\equiv0\pmod n$. Therefore

$$\boxed{u\equiv v\pmod n,}$$

so there is only one inverse class modulo $n$.

</details>
