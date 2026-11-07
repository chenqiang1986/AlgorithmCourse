# Lesson 15: Final Price After Tax and Discount
*Fundamental Math / Course 2*

Lesson 14 found one piece of a transaction: a tax amount, a discount amount, a rate,
or an original price. In a purchase, there is usually one more question: **What is the
final price?** This lesson connects the percent calculation to that final amount and
also works backward when the final price is known.

## 1. Name Each Price

Keep the prices distinct.

| Name | Meaning |
| --- | --- |
| original price | price before a tax or discount |
| discount amount | money removed from the original price |
| sale price | price after the discount, before tax |
| tax amount | money added to the taxable price |
| final price | amount paid after all discounts and taxes |

> **Always state what price the percent is based on.** A discount is usually based on
> the original price. If tax is charged after a discount, the tax is based on the sale
> price, not the original price.

## 2. One Step: Add Tax to Find the Final Price

With tax only, first find the tax amount. Then add it to the original price:

$$\text{final price}=\text{original price}+\text{tax amount}.$$

The same relationship can be written as one multiplication. Write the tax rate as a
decimal first:

$$\boxed{\text{final price}=\text{original price}\times(1+\text{tax rate})}.$$

For example, a $7.5\%$ tax rate is $0.075$, so the multiplier is
$1+0.075=1.075$. The multiplier $1.075$ means $107.5\%$ of the original price.

**Example (Tax only).** A backpack costs $\$48.00$ before tax. The tax rate is
$7.5\%$. Find the final price.

**Solution:** Find the tax first:

$$\frac{t}{48}=\frac{7.5}{100}$$

$$100t=48(7.5)=360,$$

so $t=3.60$. Add the tax:

$$48.00+3.60=51.60.$$

The final price is **$\$51.60$**.

$\square$

## 3. One Step: Subtract a Discount to Find the Sale Price

With a discount only, first find the discount amount. Then subtract it from the
original price:

$$\text{sale price}=\text{original price}-\text{discount amount}.$$

This can also be written as one multiplication. Write the discount rate as a decimal:

$$\boxed{\text{sale price}=\text{original price}\times(1-\text{discount rate})}.$$

For example, a $15\%$ discount rate is $0.15$, so the multiplier is
$1-0.15=0.85$. The multiplier $0.85$ means $85\%$ of the original price remains.

**Example (Discount only).** A $\$84.00$ jacket is on sale for $15\%$ off. Find the
sale price.

**Solution:** Let $d$ be the discount amount.

$$\frac{d}{84}=\frac{15}{100}$$

$$100d=84(15)=1260,$$

so $d=12.60$. Subtract the discount:

$$84.00-12.60=71.40.$$

The sale price is **$\$71.40$**.

$\square$

## 4. Tax After a Discount: Follow the Order

When an item is discounted and then taxed, do these steps in order:

1. Find and subtract the discount to get the sale price.
2. Find the tax using the sale price as the whole.
3. Add that tax to get the final price.

**Example (Discount, then tax).** A pair of shoes has an original price of $\$80.00$.
It is discounted $25\%$, and then $8\%$ tax is charged. Find the final price.

**Solution:** First find the discount:

$$\frac{d}{80}=\frac{25}{100}.$$

Thus $100d=80(25)=2000$, so $d=20.00$. The sale price is

$$80.00-20.00=60.00.$$

Now tax the **sale price**, $\$60.00$:

$$\frac{t}{60}=\frac{8}{100}.$$

Then $100t=60(8)=480$, so $t=4.80$. Add the tax:

$$60.00+4.80=64.80.$$

The final price is **$\$64.80$**.

$\square$

### A Common Incorrect Setup

In the example above, $8\%$ of the original $\$80.00$ is $\$6.40$. But the tax is
charged after the discount, so $\$6.40$ is not the tax amount. The tax must be $8\%$
of $\$60.00$, the sale price.

## 5. Work Backward From a Final Price

If a final price includes tax, subtracting a percent is not the right reverse step.
Instead, use the fact that a $r\%$ tax makes the final price $100+r\%$ of the
pre-tax price:

$$\frac{\text{final price}}{\text{pre-tax price}}=\frac{100+r}{100}.$$

**Example (Find the pre-tax price).** The final price of an item is $\$53.50$ after a
$7\%$ tax. Find the pre-tax price.

**Solution:** The final price is $107\%$ of the pre-tax price. Let $p$ be the pre-tax
price.

$$\frac{53.50}{p}=\frac{107}{100}.$$

Cross-multiply:

$$107p=53.50(100)=5350$$

$$p=50.00.$$

The pre-tax price is **$\$50.00$**. The tax is $\$53.50-\$50.00=\$3.50$.

$\square$

## 6. Work Backward From a Sale Price

If an item is discounted $r\%$, the sale price is $100-r\%$ of the original price:

$$\frac{\text{sale price}}{\text{original price}}=\frac{100-r}{100}.$$

**Example (Find the original price).** After a $20\%$ discount, a game costs
$\$36.00$. Find its original price.

**Solution:** A $20\%$ discount leaves $80\%$ of the original price. Let $p$ be the
original price.

$$\frac{36}{p}=\frac{80}{100}.$$

Cross-multiply:

$$80p=36(100)=3600$$

$$p=45.00.$$

The original price is **$\$45.00$**.

$\square$

> Do not subtract $20\%$ of $\$36.00$ to work backward. The $\$36.00$ is already the
> discounted price; it represents $80\%$ of the original price.

## 7. A Final-Price Checklist

Before giving an answer, check:

- Did I find the percentage amount from the correct whole?
- Did I subtract a discount and add a tax?
- If both occur, did I calculate the discount before the tax?
- Is my final price reasonable? It should be greater than the original price with only
  tax, and less than the original price with only a discount.
- Did I round a money answer to the nearest cent?

## 8. Class Practice

Try each problem before opening its solution.

### Practice 1: Tax Only

**Problem.** A $\$35.00$ item has $6\%$ tax. Find the final price.

<details>
<summary>Solution</summary>

The tax is $0.06(35)=2.10$. Add it: $35.00+2.10=37.10$. The final price is
**$\$37.10$**.

</details>

### Practice 2: Discount Only

**Problem.** A $\$120.00$ item is discounted $30\%$. Find the sale price.

<details>
<summary>Solution</summary>

The discount is $0.30(120)=36.00$. Subtract it: $120.00-36.00=84.00$. The sale price
is **$\$84.00$**.

</details>

### Practice 3: Discount Then Tax

**Problem.** A $\$50.00$ item is discounted $10\%$, then taxed $8\%$. Find the final
price.

<details>
<summary>Solution</summary>

The discount is $0.10(50)=5.00$, so the sale price is $50.00-5.00=45.00$. The tax is
$0.08(45)=3.60$. The final price is $45.00+3.60=\mathbf{\$48.60}$.

</details>

### Practice 4: Work Backward From Tax

**Problem.** A final price of $\$86.40$ includes $8\%$ tax. Find the pre-tax price.

<details>
<summary>Solution</summary>

The final price is $108\%$ of the pre-tax price. Let $p$ be the pre-tax price:

$$\frac{86.40}{p}=\frac{108}{100}.$$

So $108p=8640$, and $p=80.00$. The pre-tax price is **$\$80.00$**.

</details>

### Practice 5: Work Backward From a Discount

**Problem.** A $25\%$ discount leaves a sale price of $\$54.00$. Find the original
price.

<details>
<summary>Solution</summary>

A $25\%$ discount leaves $75\%$. Let $p$ be the original price:

$$\frac{54}{p}=\frac{75}{100}.$$

Then $75p=5400$, so $p=72.00$. The original price is **$\$72.00$**.

</details>
