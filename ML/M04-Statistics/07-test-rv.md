# Probability and Mathematical Statistics
## Chapter 2: Random Variables and Their Distributions

**Name:** ____________________　 **Class:** ____________________　 **Student ID:** ____________________

## Part I. Multiple-Choice Questions

1. Suppose the probability mass function of the random variable \(X\) is
   \[
   P(X=k)=\frac{\lambda^k}{a\,k!},\qquad k=1,2,\ldots
   \]
   Then \(a=\underline{\qquad}\).

   - (A) \(e^{-\lambda}\)
   - (B) \(e^\lambda\)
   - (C) \(e^{-\lambda}-1\)
   - (D) \(e^\lambda-1\)

2. Let \(F(x)\) be the cumulative distribution function (CDF) of a discrete random variable \(X\). And \(x_1 < x_2 < x_3 ....\) are the possible values of X. Then \(P(X=x_k)=\underline{\qquad}\). (Racall that CDF is defined as \(F(x)=P(X \le x)\))

   - (A) \(P(x_{k-1}\le X\le x_k)\)
   - (B) \(F(x_k)-F(x_{k-1})\)
   - (C) \(P(x_{k-1}<X\le x_{k+1})\)
   - (D) \(F(x_{k+1})-F(x_{k-1})\)

3. If \(F(x)\) is the CDF of a random variable \(X\), which statement is **not necessarily true**?

   - (A) \(F(-\infty)=0\)
   - (B) \(F(+\infty)=1\)
   - (C) \(0\le F(x)\le 1\)
   - (D) \(F(x)\) is continuous on \((-\infty,+\infty)\)

4. If \(F(x)\) is the CDF of a random variable \(X\), then \(P(a\le X\le b)=\underline{\qquad}\).

   - (A) \(F(b)-F(a)\)
   - (B) \(F(b)-F(a)+P(X=a)\)
   - (C) \(F(b)-F(a)-P(X=a)\)
   - (D) \(F(b)-F(a)+P(X=b)\)

5. Which of the following functions can be the CDF of a random variable?

   - (A) \(F(x)=\dfrac{1}{1+x^2}\)
   - (B) \(F(x)=\dfrac34+\dfrac{1}{2\pi}\arctan x\)
   - (C) \(F(x)=\begin{cases}0,&x<0,\\\\ \dfrac{x}{1+x},&x\ge0\end{cases}\)
   - (D) \(F(x)=1+\dfrac{2}{\pi}\arctan x\)

6. Which of the following functions can be the CDF of a random variable?

   - (A) \(F(x)=1+\dfrac{1}{x^2}\)
   - (B) \(F(x)=\dfrac12+\dfrac{1}{\pi}\arctan x\)
   - (C) \(F(x)=\begin{cases}0,&x\le0,\\\\ \dfrac12(1-e^{-x}),&x>0\end{cases}\)
   - (D) \(F(x)=\displaystyle\int_{-\infty}^{x} f(t)\,dt\), where \(\displaystyle\int_{-\infty}^{+\infty}f(t)\,dt=1\)

7. Let \(F_1(x)\) and \(F_2(x)\) be two CDFs, with corresponding probability density functions \(f_1(x)\) and \(f_2(x)\). Which of the following is a probability density function?

   - (A) \(f_1(x)f_2(x)\)
   - (B) \(2f_2(x)F_1(x)\)
   - (C) \(f_1(x)F_2(x)\)
   - (D) \(f_1(x)F_2(x)+f_2(x)F_1(x)\)

8. Let \(f(x)\) be the probability density function of a random variable \(X\). Which statement must be true?

   - (A) The domain of \(f(x)\) is \([0,1]\)
   - (B) \(f(x)\ge0\)
   - (C) The range of \(f(x)\) is \([0,1]\)
   - (D) \(f(x)\) is continuous

9. The probability density function of \(X\) is
   \[
   f(x)=\begin{cases}8x,&x\in[0,A],\\0,&x\notin[0,A].\end{cases}
   \]
   Then \(A=\underline{\qquad}\).

   - (A) \(\frac14\)
   - (B) \(\frac12\)
   - (C) \(1\)
   - (D) \(2\)

10. The probability density function of \(X\) is
    \[
    f(x)=\begin{cases}
    x,&0\le x<1,\\
    2-x,&1\le x<2,\\
    0,&\text{otherwise}.
    \end{cases}
    \]
    Then \(P(X\le2)=\underline{\qquad}\).

    - (A) \(\displaystyle\int_{-\infty}^{2}(2-x)\,dx\)
    - (B) \(\displaystyle\int_0^2 f(x)\,dx\)
    - (C) \(\displaystyle\int_0^1 x\,dx\)
    - (D) \(\displaystyle\int_1^2(2-x)\,dx\)

11. The probability density function of \(X\) is
    \[
    f(x)=\begin{cases}Bx^{-2},&x>1,\\0,&x\le1.\end{cases}
    \]
    Then \(B=\underline{\qquad}\).

    - (A) \(\frac32\)
    - (B) \(1\)
    - (C) \(-1\)
    - (D) \(\frac12\)

12. If \(X\sim N(3,2)\), which transformation \(Y=\underline{\qquad}\) has distribution \(N(0,1)\)?

    - (A) \(\frac{X-3}{2}\)
    - (B) \(\frac{X+3}{2}\)
    - (C) \(\frac{X-3}{\sqrt2}\)
    - (D) \(\frac{X+3}{\sqrt2}\)

13. Let \(P_1=P(X\le\mu-4)\) and \(P_2=P(Y\ge\mu-5)\), where \(X\sim N(\mu,4^2)\) and \(Y\sim N(\mu,5^2)\). Then:

    - (A) \(P_1<P_2\)
    - (B) \(P_1>P_2\)
    - (C) \(P_1=P_2\)
    - (D) The relationship between \(P_1\) and \(P_2\) cannot be determined.

14. Let \(X\sim N(\mu_1,\sigma_1^2)\) and \(Y\sim N(\mu_2,\sigma_2^2)\). If
    \[
    P(X-\mu_1<1)>P(Y-\mu_2<1),
    \]
    then:

    - (A) \(\sigma_1<\sigma_2\)
    - (B) \(\sigma_1>\sigma_2\)
    - (C) \(\mu_1<\mu_2\)
    - (D) \(\mu_1>\mu_2\)

15. If \(X\sim N(\mu,\sigma^2)\), then \(P(X\le1+\mu)=\underline{\qquad}\).

    - (A) Increases as \(\mu\) increases
    - (B) Decreases as \(\mu\) increases
    - (C) Increases as \(\sigma\) increases
    - (D) Decreases as \(\sigma\) increases

16. If \(X\sim N(5,\sigma^2)\), what happens to \(P(|X-5|<\sigma)\) as \(\sigma\) decreases?

    - (A) It decreases
    - (B) It increases
    - (C) It stays the same
    - (D) It depends on the circumstances

17. Let \(X\sim N(0,1)\), and let \(\Phi(x)\) be its CDF. Then:

    - (A) \(\Phi(-x)=-\Phi(x)\)
    - (B) \(\Phi(-x)=1-\Phi(x)\)
    - (C) \(\Phi(-x)=\Phi(x)-1\)
    - (D) \(\Phi(-x)=\Phi(x)\)

## Part II. Problems (Show your work in detail)

1. The probability distribution of \(X\) is given by
   \[
   \begin{array}{c|ccc}
   X & -1 & 1 & 3\\\hline
   P & 0.3 & 0.3 & 0.4
   \end{array}
   \]
   Find the cumulative distribution function \(F(x)\) of \(X\).

2. The CDF of a discrete random variable \(X\) is
   \[
   F(x)=\begin{cases}
   0,&x<-1,\\
   0.4,&-1\le x<1,\\
   0.8,&1\le x<3,\\
   1,&x\ge3.
   \end{cases}
   \]
   Find \(P(X<2\mid X\ne1)\).

3. Let \(X\sim\operatorname{Poisson}(\lambda)\), and suppose \(P(X=0)=\frac12\). Find \(P(X>1)\).

4. Let \(X\sim\operatorname{Poisson}(\lambda)\), and suppose \(P(X=1)=P(X=2)\). Find \(P(X=4)\).

5. Let \(X\sim\operatorname{Poisson}(1)\), so that
   \[
   P(X=k)=\frac{e^{-1}}{k!},\qquad k=0,1,2,\ldots
   \]
   Define events \(A=\{X\ge2\}\) and \(B=\{X<1\}\). Find:
   (1) \(P(A\cup B)\); (2) \(P(A\setminus B)\); (3) \(P(B\setminus A)\).

6. Let \(X\sim\operatorname{Binomial}(2,p)\) and \(Y\sim\operatorname{Binomial}(3,p)\). If \(P(X\ge1)=\frac59\), find \(P(Y\ge1)\).

7. The probability density function of \(X\) is
   \[
   f(x)=\begin{cases}2x,&0<x<1,\\0,&\text{otherwise}.\end{cases}
   \]
   In three independent observations of \(X\), let \(Y\) be the number of times the event \(\{X\le\frac12\}\) occurs. Find \(P(Y=1)\).

8. Let \(X\sim\operatorname{Uniform}[0,7]\). Find the probability that the equation
   \[
   x^2+2Xx+5X-4=0
   \]
   has real roots.

9. Let \(K\sim\operatorname{Uniform}[-1,5]\). Find the probability that the equation
   \[
   4x^2+4Kx+K+2=0
   \]
   has real roots.

10. Let \(X\sim\operatorname{Uniform}[-5,7]\). Find the probability that the equation
    \[
    x^2+2Xx+9=0
    \]
    has real roots.

11. Let \(X\sim N(\mu,\sigma^2)\). If the probability that the quadratic equation
    \[
    y^2+4y+X=0
    \]
    has no real roots is \(0.5\), find \(\mu\).

12. The foreign-language exam scores of candidates in a certain region are approximately normally distributed, with a mean score of \(72\). The proportion scoring \(96\) or higher is \(2.3\%\). (Use \(\Phi(1)=0.8413\) and \(\Phi(2)=0.977\).) If the third-highest score is \(96\), estimate the number of candidates who failed the exam.

13. The height of bus doors in a certain region is designed so that the probability of a man hitting his head on a door is below \(0.01\). Suppose men's heights in the region follow \(X\sim N(170,6^2)\), with heights measured in centimeters. How high should the door be? (Use \(\Phi(2.33)=0.99\).)

14. A temperature controller is placed in a container holding a certain liquid and set to \(d\,^\circ\mathrm C\). The liquid temperature \(X\), measured in degrees Celsius, is a random variable with \(X\sim N(d,0.5^2)\). To ensure that the probability of the liquid temperature being at least \(80^\circ\mathrm C\) is no less than \(0.99\), find the minimum value of \(d\). (Use \(\Phi(2)=0.977\) and \(\Phi(2.33)=0.99\).)

15. The probability density function of \(X\) is
    \[
    f(x)=\begin{cases}
    \dfrac{A}{\sqrt{1-x^2}},&|x|<1,\\
    0,&|x|\ge1.
    \end{cases}
    \]
    (1) Find the constant \(A\). (2) Find \(P(-0.5<X\le0.5)\).

For all the questions below, we assume \(X\) to be a random variable with continuous distribution:

16. The probability density function of \(X\) is
    \[
    f(x)=\begin{cases}
    a\cos x,&x<\frac{\pi}{2},\\
    0,&x\ge\frac{\pi}{2}.
    \end{cases}
    \]
    Find: (1) the constant \(a\); (2) \(P(-\frac{\pi}{4}<X<\pi)\).

17. The probability density function of \(X\) is
    \[
    f(x)=\begin{cases}
    Ax^2,&0<x<1,\\
    0,&\text{otherwise}.
    \end{cases}
    \]
    Find: (1) the constant \(A\); (2) \(P(-\frac12<X<\frac14)\).

18. The CDF of \(X\) is
    \[
    F(x)=\begin{cases}
    A+B e^{-x^2/2},&x>0,\\
    0,&x\le0.
    \end{cases}
    \]
    Find: (1) the constants \(A\) and \(B\); (2) \(P(\sqrt{\ln4}<X<\sqrt{\ln9})\); (3) the probability density function \(f(x)\).

19. The CDF of \(X\) is
    \[
    F(x)=\begin{cases}
    0,&x\le0,\\
    Ax^2,&0<x\le1,\\
    1,&x>1.
    \end{cases}
    \]
    Find: (1) \(A\); (2) \(P(0.3<X<0.7)\); (3) the probability density function \(f(x)\).

20. The CDF of \(X\) is
    \[
    F(x)=\begin{cases}
    0,&x\le-a,\\
    A+B\arcsin\left(\frac{x}{a}\right),&-a<x\le a,\\
    1,&x>a.
    \end{cases}
    \]
    Find: (1) \(A\) and \(B\); (2) \(P(-\frac a2<X<\frac a2)\); (3) the probability density function \(f(x)\).

21. The CDF of \(X\) is
    \[
    F(x)=\begin{cases}
    0,&x\le-a,\\
    A+B\arctan\left(\frac{x}{a}\right),&-a<x\le a,\\
    1,&x>a.
    \end{cases}
    \]
    Find: (1) \(A\) and \(B\); (2) \(P(0<X<\frac{\sqrt3\,a}{3})\); (3) the probability density function \(f(x)\).

---

**Notation:** \(N(\mu,\sigma^2)\) denotes a normal distribution with mean \(\mu\) and variance \(\sigma^2\); \(\operatorname{Uniform}[a,b]\) denotes a continuous uniform distribution; \(\operatorname{Binomial}(n,p)\) denotes a binomial distribution.
