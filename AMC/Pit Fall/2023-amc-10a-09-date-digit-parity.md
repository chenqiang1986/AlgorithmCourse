# AMC 10 2023 A, Problem 9 — Date Digits and Exhaustive Casework

> A digital display shows the current date as an 8-digit integer: a 4-digit year, then a 2-digit month, then a 2-digit day. For how many dates in 2023 does every digit occur an even number of times?

## Key observation

Write the display as

$$2023\,MM\,DD.$$

Before considering `MMDD`, the year contributes two `2`s, one `0`, and one `3`.

- The two `2`s are already paired.
- The `0` and `3` each currently occur an odd number of times.

Therefore, in the four unknown positions `MMDD`, digits `0` and `3` must each occur an **odd** number of times, and every other digit must occur an even number of times. This is the condition we maintain in every case below.

## Exhaustive casework by enumerate month first

The two month digits are the first two of the four unknown positions. Thus, looking through the possible months tells us whether `0` and/or `3` has already appeared before the day digits. This prevents missed cases.

| Month(s) | What the month has done to the parity | Forced day digits | Valid dates |
|---|---|---|---|
| `01` | `0` is now paired; `1` occurs once; `3` still occurs once | one `1` and one `3` | `01/13`, `01/31` |
| `02` | `0` is paired; `2` now occurs three times; `3` still occurs once | one `2` and one `3` | `02/23` (`32` is not a day) |
| `03` | both `0` and `3` are paired | two equal digits | `03/11`, `03/22` |
| `04,05,06,07,08,09` | `0` is paired; the nonzero month digit occurs once; `3` still occurs once | that month digit and a `3` | none: the only orders are at least `34` or `43` |
| `10` | same parity situation as `01` | one `1` and one `3` | `10/13`, `10/31` |
| `11` | the two `1`s are paired; neither `0` nor `3` has appeared in the month | one `0` and one `3` | `11/03`, `11/30` |
| `12` | `1` and `2` each occur oddly, and `0` and `3` are also odd | would need `0,1,2,3` in only two day positions | none |

For the `03` row, a day must have matching digits. Among actual days, only `11` and `22` work: `00` is not a day, `33` is not a valid day, and larger repeated pairs exceed 31.

## Count

The complete list is

$$
\begin{aligned}
&\text{January }13,31;\\
&\text{February }23;\\
&\text{March }11,22;\\
&\text{October }13,31;\\
&\text{November }03,30.
\end{aligned}
$$

Hence the answer is

$$\boxed{9}.$$

## Solution 2: Place `0` and `3` first

Here is a second exhaustive organization of the same parity condition. After placing one needed `0` and one needed `3`, the two remaining positions must contain the same digit. (That repeated digit is allowed to be `0` or `3`; then one of those digits occurs three times in `MMDD`, which is still odd.)

First place `0` before `3` in the four positions of `MMDD`:

```text
202303__
20230_3_
20230__3
2023_03_
2023_0_3
2023__03
```

Then place `3` before `0`:

```text
20233___
2023_30_
2023_3_0
2023__30
```

In a template with two blanks, both blanks are the same digit. In the first template of the second block, the month would begin with `3`, so it is immediately impossible; the other templates in that block either reduce to a previous `0`-first case or fail the month restriction, except the final one.

Checking the templates against valid months and days gives:

| Template | Dates that survive |
|---|---|
| `202303__` | `20230311`, `20230322` |
| `20230_3_` | `20230131` |
| `20230__3` | `20230113`, `20230223` |
| `2023_03_` | `20231031` |
| `2023_0_3` | `20231013` |
| `2023__03` | `20231103` |
| `20233___`, `2023_30_`, `2023_3_0` | none new |
| `2023__30` | `20231130` |

This produces the same nine displays as Solution 1.

## Pitfall

Use an enumeration pattern that is defined in advance and reliably exhaustive: for example, split by the month (Solution 1), or list the possible positions of `0` and `3` (Solution 2).

Do not observe a month restriction to obtain a few solutions, then switch to observing a day restriction to obtain a few others. That mixed, improvised process makes it very easy to miss a case or count the same date twice.
