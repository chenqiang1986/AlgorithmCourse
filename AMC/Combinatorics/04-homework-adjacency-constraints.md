# Homework: Adjacency Constraints
*AMC / Combinatorics*

This homework accompanies [Lesson 4](./04-adjacency-constraints.md). In every
counting problem, the people or objects are distinct. State the method you use:
**bundling**, **gaps**, or **complement**.  For a circular arrangement, rotations
are considered the same unless the problem says otherwise.

## Part A: One Restriction at a Time

### Problem 1

Six students, including Ana and Bo, stand in a row. How many lineups have Ana
and Bo next to each other?

<details>
<summary>Solution</summary>

Bundle Ana and Bo. There are $5$ objects to arrange, and the pair has $2$ internal
orders:

$$5!\cdot2!=120\cdot2=\boxed{240}. $$

</details>

### Problem 2

Eight different books are placed on a shelf. Two particular books, $M$ and $N$,
must be together. How many arrangements are possible?

<details>
<summary>Solution</summary>

Treat $M$ and $N$ as one block. This gives $7!$ arrangements of the resulting
objects and $2!$ orders within the block:

$$7!\cdot2!=\boxed{10{,}080}. $$

</details>

### Problem 3

Seven people sit in a row. Lena and Omar refuse to sit next to each other. How
many valid seatings are there?

<details>
<summary>Solution</summary>

Use the complement. There are $7!$ total seatings. If Lena and Omar are bundled,
there are $6!\cdot2!$ forbidden seatings. Thus

$$7!-6!\cdot2!=5{,}040-1{,}440=\boxed{3{,}600}. $$

</details>

### Problem 4

Nine different flags are hung in a row. Three specified flags must form one
consecutive group, in any order. How many displays are possible?

<details>
<summary>Solution</summary>

Bundle the three flags. The block and the other six flags make $7$ objects, and
the block has $3!$ internal orders:

$$7!\cdot3!=\boxed{30{,}240}. $$

</details>

### Problem 5

Seven distinct books include three novels by the same author. In how many orders
can the books be shelved if no two of those three novels are adjacent?

<details>
<summary>Solution</summary>

First arrange the other four books: $4!$ ways. They create $5$ gaps. Place the
three novels in three distinct gaps, in order, giving $P_5^3$ choices:

$$4!\cdot P_5^3=24\cdot(5\cdot4\cdot3)=\boxed{1{,}440}. $$

</details>

### Problem 6

Eight students include five members of a quiz team. Can all five team members be
seated in a row with no two team members adjacent? If so, how many ways are there?

<details>
<summary>Solution</summary>

Arrange the other three students first. They create only $3+1=4$ gaps, but five
team members would need five distinct gaps. Therefore the condition is impossible:

$$\boxed{0}. $$

</details>

## Part B: Combining Restrictions

### Problem 7

Eight people stand in a row. Ava and Ben must be together, and Cy and Dia must
also be together. How many lineups are possible?

<details>
<summary>Solution</summary>

Make an AB block and a CD block. Together with the other four people, there are
$6$ objects to arrange. Each block has two internal orders:

$$6!\cdot2!\cdot2!=\boxed{2{,}880}. $$

</details>

### Problem 8

Eight people stand in a row. Cy and Dia must be together, but Ava and Ben must
not be together. How many lineups are possible?

<details>
<summary>Solution</summary>

First make the CD block. There are then $6$ effective objects. Of their $6!$
arrangements, $5!\cdot2!$ have Ava and Ben adjacent. Account for the two orders
inside the CD block:

$$\left(6!-5!\cdot2!\right)\cdot2!
=\left(720-240\right)\cdot2
=\boxed{960}. $$

</details>

### Problem 9

Eight people include three siblings. How many row seatings have no two siblings
sitting next to each other?

<details>
<summary>Solution</summary>

Arrange the five non-siblings first: $5!$ ways. Their arrangement creates $6$
gaps. Insert the three siblings into distinct gaps:

$$5!\cdot P_6^3=120\cdot(6\cdot5\cdot4)=\boxed{14{,}400}. $$

</details>

### Problem 10

Seven people sit around a circular table. Eve and Finn must sit next to each
other. How many seatings are possible?

<details>
<summary>Solution</summary>

Bundle Eve and Finn, leaving $6$ objects around the circle. Their circular
arrangements number $(6-1)!$, and the pair has two internal orders:

$$5!\cdot2!=\boxed{240}. $$

</details>

### Problem 11

Eight people sit around a circular table. Priya and Quinn must not sit next to
each other. How many seatings are possible?

<details>
<summary>Solution</summary>

There are $(8-1)!=7!$ circular seatings in total. Bundling Priya and Quinn gives
$7$ circular objects, so the forbidden count is $(7-1)!\cdot2!=6!\cdot2!$.

$$7!-6!\cdot2!=5{,}040-1{,}440=\boxed{3{,}600}. $$

</details>

### Problem 12

Eight people, including Ana, Bo, and Cy, sit in a row. Ana, Bo, and Cy are not
allowed to form one consecutive group of three. (Two of them may still be next to
each other.) How many valid seatings are there?

<details>
<summary>Solution</summary>

Use the complement of the fully bundled group. There are $8!$ total seatings. If
all three form a single block, there are $6!\cdot3!$ seatings. Hence

$$8!-6!\cdot3!=40{,}320-4{,}320=\boxed{36{,}000}. $$

</details>

## Part C: Choose the Model Carefully

### Problem 13

Five people $A,B,C,D,E$ stand in a row. Person $A$ must stand next to $B$, but
$B$ must not stand next to $C$. How many lineups are possible?

<details>
<summary>Solution</summary>

There are $4!\cdot2!=48$ lineups with $A$ adjacent to $B$. Among these, the
forbidden lineups have $B$ adjacent to both $A$ and $C$, so the three-person run
must be $ABC$ or $CBA$. Treat that run as a block with $D,E$:

$$3!\cdot2=12. $$

Therefore the desired count is

$$48-12=\boxed{36}. $$

</details>

### Problem 14

Nine people, including $P,Q,R$, stand in a row. Persons $P$ and $Q$ must be
adjacent, but $P,Q,R$ must not all form one consecutive group. How many lineups
are possible?

<details>
<summary>Solution</summary>

Start with the required $PQ$ adjacency:

$$8!\cdot2!=80{,}640. $$

Now subtract the cases where $P,Q,R$ form one run. Within such a three-person
block, $P$ and $Q$ must be adjacent. Bundle $P,Q$ within the block: its possible
internal orders are $PQR, QPR, RPQ, RQP$, for $4$ orders. The three-person block
and the other six people make $7$ objects, so the forbidden count is

$$7!\cdot4=20{,}160. $$

Thus the answer is

$$80{,}640-20{,}160=\boxed{60{,}480}. $$

</details>

### Problem 15

Six people, including three friends, sit around a circular table. How many
seatings have no two of the three friends adjacent?

<details>
<summary>Solution</summary>

Arrange the three non-friends around the circle in $(3-1)!=2$ ways. They create
three circular gaps. To separate all three friends, put one friend into each gap,
in $3!$ orders:

$$2!\cdot3!=\boxed{12}. $$

</details>

### Problem 16

Explain why the two formulas below count the same thing: the number of lineups of
$n$ distinct people in which two specified people are not adjacent.

$$ (n-2)!\cdot P_{n-1}^{2} \qquad\text{and}\qquad n!-2(n-1)! $$

<details>
<summary>Solution</summary>

Algebraically,

$$
(n-2)!\cdot P_{n-1}^{2}
=(n-2)!\cdot(n-1)(n-2)
=n!-2(n-1)!.
$$

Conceptually, the first formula is the gap method: arrange the other $n-2$
people, then put the two specified people into distinct gaps. The second is the
complement method: subtract the $2(n-1)!$ lineups in which the two people form a
block from all $n!$ lineups.

</details>

## Self-Check

- A required consecutive group calls for a block and its internal arrangements.
- To keep several people mutually separated, first arrange everyone else and use
  distinct gaps.
- “Not all together” permits partial adjacency, so subtract the fully bundled case
  rather than using the gap method.
- For circular arrangements, glue first; then use the circular-arrangement count.
