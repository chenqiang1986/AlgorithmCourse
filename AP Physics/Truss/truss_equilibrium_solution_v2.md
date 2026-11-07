# Truss Equilibrium: A Systematic Method

## Given problem

A planar truss has four rectangular bays. Each bay is $9\,\mathrm{m}$ wide and $6\,\mathrm{m}$ high. Two downward loads of $15\,\mathrm{N}$ act at joints $D$ and $G$.

- Support $A$: reaction components $A_x$ and $A_y$, applied at the bottom of the long left support leg.
- Support $L$: vertical reaction $L_y$, applied at the bottom of the long right support leg.
- Required member forces: $DF$, $EF$, and $DE$.

The truss itself has four $9\,\mathrm{m}$-wide bays and is $6\,\mathrm{m}$ high. The support legs extend downward from the truss; the reaction forces are applied at their bottom endpoints, $A$ and $L$.

## Geometry diagram

<svg xmlns="http://www.w3.org/2000/svg" width="900" height="390" viewBox="0 0 900 390" role="img" aria-label="Truss with four bays, long support legs down to A and L, loads at D and G, and support reactions">
  <defs>
    <marker id="arr" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#222"/></marker>
  </defs>
  <g stroke="#333" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round">
    <path d="M100 90 H700 M100 210 H700"/>
    <path d="M100 90 V210 M250 90 V210 M400 90 V210 M550 90 V210 M700 90 V210"/>
    <path d="M100 90 L250 210 M250 90 L400 210 M400 210 L550 90 M550 210 L700 90"/>
    <path d="M100 210 V335 M700 210 V335"/>
  </g>
  <g stroke="#222" stroke-width="2.8" fill="none" marker-end="url(#arr)">
    <path d="M250 15 V78"/><path d="M400 15 V78"/>
    <path d="M30 335 H90"/><path d="M100 380 V345"/><path d="M700 380 V345"/>
  </g>
  <g font-family="Arial, sans-serif" font-size="18" fill="#111">
    <text x="264" y="25">15 N</text><text x="414" y="25">15 N</text>
    <text x="76" y="357">A</text><text x="711" y="357">L</text>
    <text x="85" y="82">C</text><text x="239" y="82">D</text><text x="390" y="82">G</text><text x="540" y="82">H</text><text x="690" y="82">I</text>
    <text x="84" y="235">B</text><text x="239" y="235">E</text><text x="390" y="235">F</text><text x="540" y="235">J</text><text x="690" y="235">K</text>
    <text x="18" y="322">Aₓ</text><text x="112" y="380">Aᵧ</text><text x="712" y="380">Lᵧ</text>
    <text x="165" y="265">9 m</text><text x="315" y="265">9 m</text><text x="465" y="265">9 m</text><text x="615" y="265">9 m</text><text x="735" y="155">6 m</text>
    <text x="120" y="320" font-size="14">support leg</text><text x="720" y="320" font-size="14">support leg</text>
  </g>
</svg>

*The diagram is schematic. The truss bay dimensions are $9\,\mathrm{m}\times6\,\mathrm{m}$. The support legs are drawn longer to make clear that the reactions act at A and L, not at joints B and K.*

---

## General strategy

1. **Find the external forces.** Treat the entire supported structure as one rigid body. Use $\sum F_x=0$, $\sum F_y=0$, and $\sum\tau=0$ to determine the support reactions.
2. **Identify obvious zero-force members.** Apply the standard joint rules only at joints with no external force applied directly to that joint. There are two standard cases:
   - If a no-external-force joint has exactly two members that are **not collinear**, both members are zero-force members.
   - If a no-external-force joint has exactly three members, with two **collinear** members and one non-collinear member, the non-collinear member is a zero-force member.
3. **Find selected internal member forces with sections.**
   - Cut through the target member—the member whose force you want to calculate.
   - Cut additional neighboring members as needed to separate the truss into two sections.
   - In general, cut through **at most three members with unknown forces**.

   Isolate one section and apply the same three equilibrium equations. Choose a pivot that eliminates as many unknown cut forces as possible.

A pivot can be chosen anywhere. A force whose line of action passes through the pivot has zero torque about that pivot. Choosing such a pivot is a convenient way to eliminate an unknown from the torque equation.

## Step 0. Identify obvious zero-force members

At joint $B$, $BC$ and $BA$ are in the same direction, but $BE$ is not. So :

$$
\boxed{F_{BE}=0.}
$$

Similarly

$$
\boxed{F_{JK}=0.}
$$

These are the obvious zero-force members for the diagram.

---

## Part 1. Solve the external support reactions

Treat the whole structure as one free body. Internal member forces cancel in pairs and do not appear in the overall equilibrium equations.

Unknown reactions are $A_x$, $A_y$, and $L_y$. The known loads are $15\,\mathrm{N}$ downward at $x=9\,\mathrm{m}$ and $x=18\,\mathrm{m}$.

### Option 1. Choose pivot point A

Take counterclockwise torque as positive. The three equilibrium equations are

$$
\left\{
\begin{aligned}
\sum F_x=0:&\qquad A_x=0,\\
\sum F_y=0:&\qquad A_y+L_y-15-15=0,\\
\sum\tau_A=0:&\qquad 36L_y-9(15)-18(15)=0.
\end{aligned}
\right.
$$

Solving the system gives

$$
\boxed{A_x=0,\qquad A_y=18.75\,\mathrm{N},\qquad L_y=11.25\,\mathrm{N}.}
$$

### Option 2. Choose pivot point E

Using a different pivot produces a different, but equally valid, torque equation. Let $s$ be the vertical distance from $A$ to the horizontal level through $E$. The $sA_x$ term is included for completeness; the horizontal-force equation will give $A_x=0$.

$$
\left\{
\begin{aligned}
\sum F_x=0:&\qquad A_x=0,\\
\sum F_y=0:&\qquad A_y+L_y-15-15=0,\\
\sum\tau_E=0:&\qquad sA_x-9A_y-9(15)+27L_y=0.
\end{aligned}
\right.
$$

Solving this system again gives

$$
\boxed{A_x=0,\qquad A_y=18.75\,\mathrm{N},\qquad L_y=11.25\,\mathrm{N}.}
$$

Pivot $A$ is convenient because both reaction forces at $A$ have zero moment there. Pivot $E$ is still valid and leads to the same support reactions.

---

## Part 2. Solve member forces DF, and EF using a section

In order to find the force on $DF$ and $EF$, we have to cut $DF$ and $EF$. To fully separate the system into two parts, we have to cut $DG$ as well.

<svg xmlns="http://www.w3.org/2000/svg" width="900" height="390" viewBox="0 0 900 390" role="img" aria-label="Original truss diagram with DF and EF highlighted in red and DG highlighted in green">
  <defs>
    <marker id="section-arr" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#222"/></marker>
  </defs>
  <g stroke="#333" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round">
    <path d="M100 90 H700 M100 210 H700"/>
    <path d="M100 90 V210 M250 90 V210 M400 90 V210 M550 90 V210 M700 90 V210"/>
    <path d="M100 90 L250 210 M250 90 L400 210 M400 210 L550 90 M550 210 L700 90"/>
    <path d="M100 210 V335 M700 210 V335"/>
  </g>
  <g fill="none" stroke-linecap="round">
    <path d="M250 90 L400 210 M250 210 H400" stroke="#d62828" stroke-width="7"/>
    <path d="M250 90 H400" stroke="#2a9d4b" stroke-width="7"/>
  </g>
  <g stroke="#222" stroke-width="2.8" fill="none" marker-end="url(#section-arr)">
    <path d="M250 15 V78"/><path d="M400 15 V78"/>
    <path d="M30 335 H90"/><path d="M100 380 V345"/><path d="M700 380 V345"/>
  </g>
  <g font-family="Arial, sans-serif" font-size="18" fill="#111">
    <text x="264" y="25">15 N</text><text x="414" y="25">15 N</text>
    <text x="76" y="357">A</text><text x="711" y="357">L</text>
    <text x="85" y="82">C</text><text x="239" y="82">D</text><text x="390" y="82">G</text><text x="540" y="82">H</text><text x="690" y="82">I</text>
    <text x="84" y="235">B</text><text x="239" y="235">E</text><text x="390" y="235">F</text><text x="540" y="235">J</text><text x="690" y="235">K</text>
    <text x="18" y="322">Aₓ</text><text x="112" y="380">Aᵧ</text><text x="712" y="380">Lᵧ</text>
    <text x="165" y="265">9 m</text><text x="315" y="265">9 m</text><text x="465" y="265">9 m</text><text x="615" y="265">9 m</text><text x="735" y="155">6 m</text>
    <text x="120" y="320" font-size="14">support leg</text><text x="720" y="320" font-size="14">support leg</text>
  </g>
</svg>

*The two red members are the requested member forces. The green member is the additional cut required to create two separate free bodies.*

Cut through members $DG$, $DF$, and $EF$, and isolate the **left-hand portion** of the truss. The section crosses exactly the three target members; the left-hand free body contains the known reactions at $A$ and the known $15\,\mathrm{N}$ load at $D$.

Assume initially that all cut-member forces are tensile: they pull away from the isolated section. A negative answer means the actual member is in compression.

### Left section after the cut

<svg xmlns="http://www.w3.org/2000/svg" width="760" height="300" viewBox="0 0 760 300" role="img" aria-label="Left section of the truss after a cut through DG, DF, and EF">
  <g stroke="#333" stroke-width="4" fill="none" stroke-linecap="round">
    <path d="M90 80 H195 M90 80 V200 M90 200 H195 M90 80 L195 200 M195 80 V200 M90 200 V260"/>
    <path d="M195 80 H315 M195 80 L315 200 M195 200 H315" stroke-dasharray="7 6"/>
  </g>
  <g font-family="Arial, sans-serif" font-size="17" fill="#111">
    <text x="78" y="70">C</text><text x="184" y="70">D</text><text x="78" y="225">B</text><text x="183" y="225">E</text><text x="77" y="282">A</text>
    <text x="325" y="70">DG</text><text x="286" y="145">DF</text><text x="325" y="220">EF</text>
  </g>
</svg>

After the cut, the left section consists of joints $A$, $B$, $C$, $D$, and $E$, and members $AB$, $BE$, $BC$, $CD$, $DE$, and $CE$. However, $DG$, $DF$, and $EF$ are no longer internal members of the isolated left section. Their member forces act as **external forces** on that section. Along with $A_x$, $A_y$, and the $15\,\mathrm{N}$ load at $D$, the left section has six external forces:

$$
A_x,\quad A_y,\quad 15\,\mathrm{N}\text{ at }D,\quad F_{DG},\quad F_{DF},\quad F_{EF}.
$$

### Free-body diagram of the left section

<svg xmlns="http://www.w3.org/2000/svg" width="760" height="320" viewBox="0 0 760 320" role="img" aria-label="Free-body diagram of the left truss section with six external forces">
  <defs>
    <marker id="fbd-arr" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#222"/></marker>
  </defs>
  <g stroke="#333" stroke-width="4" fill="none" stroke-linecap="round">
    <path d="M90 80 H195 M90 80 V200 M90 200 H195 M90 80 L195 200 M195 80 V200 M90 200 V260"/>
  </g>
  <g stroke="#222" stroke-width="2.5" fill="none" marker-end="url(#fbd-arr)">
    <path d="M195 10 V68"/><path d="M35 260 H82"/><path d="M90 305 V270"/>
    <path d="M195 80 H275"/><path d="M195 80 L253 157"/><path d="M195 200 H280"/>
  </g>
  <path d="M231 80 A36 36 0 0 1 224 103" stroke="#222" stroke-width="2" fill="none"/>
  <g font-family="Arial, sans-serif" font-size="17" fill="#111">
    <text x="208" y="18">15 N</text><text x="18" y="250">Aₓ = 0</text><text x="100" y="308">Aᵧ = 18.75 N</text>
    <text x="280" y="86">F_DG</text><text x="257" y="164">F_DF</text><text x="282" y="223">F_EF</text>
    <text x="230" y="103">θ</text>
    <text x="78" y="70">C</text><text x="184" y="70">D</text><text x="78" y="225">B</text><text x="183" y="225">E</text><text x="77" y="282">A</text>
  </g>
</svg>

The cut geometry is a $9$-$6$-$\sqrt{117}$ triangle. Thus, for member $DF$,

$$
\cos\theta=\frac{9}{\sqrt{117}}=\frac{3}{\sqrt{13}},
\qquad
\sin\theta=\frac{6}{\sqrt{117}}=\frac{2}{\sqrt{13}}.
$$

Let $w$ be the bay width, $h$ the truss height, and $P$ the downward load at $D$. Thus, later we will use $w=9\,\mathrm{m}$, $h=6\,\mathrm{m}$, and $P=15\,\mathrm{N}$. With the tensile-force assumption shown in the free-body diagram, $F_{DF}$ has components $F_{DF}\cos\theta$ to the right and $F_{DF}\sin\theta$ downward.

### Option 1. Choose pivot point F

Start with the three equilibrium principles, without substituting numerical values. Since the lines of action of $F_{DF}$ and $F_{EF}$ pass through $F$, neither has a moment about $F$:

$$
\left\{
\begin{aligned}
\sum F_x=0:&\qquad A_x+F_{DG}+F_{DF}\cos\theta+F_{EF}=0,\\
\sum F_y=0:&\qquad A_y-P-F_{DF}\sin\theta=0,\\
\sum\tau_F=0:&\qquad hA_x-2wA_y+wP-hF_{DG}=0.
\end{aligned}
\right.
$$

Now use $A_x=0$, $A_y=18.75\,\mathrm{N}$, $P=15\,\mathrm{N}$, $w=9\,\mathrm{m}$, $h=6\,\mathrm{m}$, $\sin\theta=2/\sqrt{13}$, and $\cos\theta=3/\sqrt{13}$. The system becomes

$$
\left\{
\begin{aligned}
F_{DG}+\frac{3}{\sqrt{13}}F_{DF}+F_{EF}&=0,\\
3.75-\frac{2}{\sqrt{13}}F_{DF}&=0,\\
-202.5-6F_{DG}&=0.
\end{aligned}
\right.
$$

Solving the equations in the order $\sum F_y$, $\sum\tau_F$, then $\sum F_x$ gives

$$
\begin{aligned}
F_{DF}&=\frac{A_y-P}{\sin\theta}=\frac{15\sqrt{13}}{8}\,\mathrm{N}\approx6.77\,\mathrm{N},\\
F_{DG}&=A_x-\frac{2w}{h}A_y+\frac{w}{h}P=-33.75\,\mathrm{N},\\
F_{EF}&=-A_x-F_{DG}-F_{DF}\cos\theta=28.125\,\mathrm{N}.
\end{aligned}
$$

Therefore,

$$
\boxed{DG=33.75\,\mathrm{N}\text{ (compression)},\quad
DF=6.77\,\mathrm{N}\text{ (tension)},\quad
EF=28.125\,\mathrm{N}\text{ (tension)}.}
$$

### Option 2. Choose pivot point E

Pivot $E$ is equally valid. The line of action of $F_{EF}$ passes through $E$, and the load at $D$ is vertically aligned with $E$, so both have zero moment about $E$. The equilibrium system is

$$
\left\{
\begin{aligned}
\sum F_x=0:&\qquad A_x+F_{DG}+F_{DF}\cos\theta+F_{EF}=0,\\
\sum F_y=0:&\qquad A_y-P-F_{DF}\sin\theta=0,\\
\sum\tau_E=0:&\qquad hA_x-wA_y-hF_{DG}-hF_{DF}\cos\theta=0.
\end{aligned}
\right.
$$

Substituting the same known reaction forces, geometry, load, and trigonometric values gives

$$
\left\{
\begin{aligned}
F_{DG}+\frac{3}{\sqrt{13}}F_{DF}+F_{EF}&=0,\\
3.75-\frac{2}{\sqrt{13}}F_{DF}&=0,\\
-168.75-6F_{DG}-\frac{18}{\sqrt{13}}F_{DF}&=0.
\end{aligned}
\right.
$$

Solving in the order $\sum F_y$, $\sum\tau_E$, then $\sum F_x$, gives

$$
\begin{aligned}
F_{DF}&=\frac{A_y-P}{\sin\theta}=\frac{15\sqrt{13}}{8}\,\mathrm{N}\approx6.77\,\mathrm{N},\\
F_{DG}&=A_x-\frac{w}{h}A_y-F_{DF}\cos\theta=-33.75\,\mathrm{N},\\
F_{EF}&=-A_x-F_{DG}-F_{DF}\cos\theta=28.125\,\mathrm{N}.
\end{aligned}
$$

The negative value of $F_{DG}$ means that $DG$ is in compression; the positive values of $F_{DF}$ and $F_{EF}$ mean those members are in tension.

The pivot point for a torque equation is arbitrary: any point gives a valid equilibrium equation and, when combined with the force equations, the same final member forces. In practice, choose a pivot through which as many unknown force lines of action as possible pass. This makes their moments zero and usually simplifies the system, as pivot $F$ does in Option 1. Choosing a less convenient point, such as $E$ in Option 2, is still completely valid and leads to the same answer.

---

## Part 3. Solve member DE

### Method A. Use the joint at D

At joint $D$, the forces in $CD$ and $DG$ are horizontal, so they do not appear in vertical force equilibrium. The known downward load at $D$, the vertical component of the already known force in $DF$, and the force in $DE$ are the only vertical forces. Assuming tension in $DE$ initially gives

$$
\sum F_y=0:\qquad -15-F_{DF}\sin\theta-F_{DE}=0.
$$

Using $F_{DF}=15\sqrt{13}/8\,\mathrm{N}$ from Part 2 and $\sin\theta=2/\sqrt{13}$,

$$
F_{DE}=-15-\left(\frac{15\sqrt{13}}{8}\right)\left(\frac{2}{\sqrt{13}}\right)
=-18.75\,\mathrm{N}.
$$

The negative sign means the member is in compression:

$$
\boxed{DE=18.75\,\mathrm{N}\quad\text{(compression)}}.
$$

### Method B. Use a section through CD, DE, and EF

Method A can seem almost like magic: it happens to use a joint where vertical equilibrium gives $DE$ immediately. But what if the problem asked for the force in $DE$ without first asking for $DF$ and $EF$? The regular method of sections finds $DE$ directly.

Cut through members $CD$, $DE$, and $EF$. These three cuts separate a left-hand section containing joints $A$, $B$, $C$, and $E$.

<svg xmlns="http://www.w3.org/2000/svg" width="900" height="390" viewBox="0 0 900 390" role="img" aria-label="Original truss with members CD, DE, and EF highlighted as the section cut">
  <defs>
    <marker id="de-section-arr" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#222"/></marker>
  </defs>
  <g stroke="#333" stroke-width="4" fill="none" stroke-linecap="round" stroke-linejoin="round">
    <path d="M100 90 H700 M100 210 H700"/>
    <path d="M100 90 V210 M250 90 V210 M400 90 V210 M550 90 V210 M700 90 V210"/>
    <path d="M100 90 L250 210 M250 90 L400 210 M400 210 L550 90 M550 210 L700 90"/>
    <path d="M100 210 V335 M700 210 V335"/>
  </g>
  <g fill="none" stroke-linecap="round">
    <path d="M250 90 V210" stroke="#d62828" stroke-width="7"/>
    <path d="M100 90 H250 M250 210 H400" stroke="#2a9d4b" stroke-width="7"/>
  </g>
  <g stroke="#222" stroke-width="2.8" fill="none" marker-end="url(#de-section-arr)">
    <path d="M250 15 V78"/><path d="M400 15 V78"/>
    <path d="M30 335 H90"/><path d="M100 380 V345"/><path d="M700 380 V345"/>
  </g>
  <g font-family="Arial, sans-serif" font-size="18" fill="#111">
    <text x="264" y="25">15 N</text><text x="414" y="25">15 N</text>
    <text x="76" y="357">A</text><text x="711" y="357">L</text>
    <text x="85" y="82">C</text><text x="239" y="82">D</text><text x="390" y="82">G</text><text x="540" y="82">H</text><text x="690" y="82">I</text>
    <text x="84" y="235">B</text><text x="239" y="235">E</text><text x="390" y="235">F</text><text x="540" y="235">J</text><text x="690" y="235">K</text>
    <text x="18" y="322">Aₓ</text><text x="112" y="380">Aᵧ</text><text x="712" y="380">Lᵧ</text>
  </g>
</svg>

*The red member is the requested force, (DE). The green members, (CD) and (EF), are the accompanying cuts needed to isolate the section.*

### Left section after the cut

<svg xmlns="http://www.w3.org/2000/svg" width="760" height="300" viewBox="0 0 760 300" role="img" aria-label="Left truss section after cutting CD, DE, and EF">
  <g stroke="#333" stroke-width="4" fill="none" stroke-linecap="round">
    <path d="M90 80 V200 M90 200 H195 M90 80 L195 200 M90 200 V260"/>
    <path d="M90 80 H195 M195 200 V80 M195 200 H315" stroke-dasharray="7 6"/>
  </g>
  <g font-family="Arial, sans-serif" font-size="17" fill="#111">
    <text x="78" y="70">C</text><text x="78" y="225">B</text><text x="183" y="225">E</text><text x="77" y="282">A</text>
    <text x="137" y="70">CD</text><text x="202" y="145">DE</text><text x="325" y="220">EF</text>
  </g>
</svg>

After the cut, $CD$, $DE$, and $EF$ are external forces on the isolated left section. The free-body diagram is

<svg xmlns="http://www.w3.org/2000/svg" width="760" height="320" viewBox="0 0 760 320" role="img" aria-label="Free-body diagram of the left truss section cut through CD, DE, and EF">
  <defs>
    <marker id="de-fbd-arr" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="#222"/></marker>
  </defs>
  <g stroke="#333" stroke-width="4" fill="none" stroke-linecap="round">
    <path d="M90 80 V200 M90 200 H195 M90 80 L195 200 M90 200 V260"/>
  </g>
  <g stroke="#222" stroke-width="2.5" fill="none" marker-end="url(#de-fbd-arr)">
    <path d="M35 260 H82"/><path d="M90 305 V270"/>
    <path d="M90 80 H170"/><path d="M195 200 V120"/><path d="M195 200 H275"/>
  </g>
  <g font-family="Arial, sans-serif" font-size="17" fill="#111">
    <text x="18" y="250">Aₓ = 0</text><text x="100" y="308">Aᵧ = 18.75 N</text>
    <text x="175" y="86">F_CD</text><text x="202" y="125">F_DE</text><text x="280" y="206">F_EF</text>
    <text x="78" y="70">C</text><text x="78" y="225">B</text><text x="183" y="225">E</text><text x="77" y="282">A</text>
  </g>
</svg>

The cut forces in $CD$ and $EF$ are horizontal. Therefore, vertical equilibrium alone is enough to find $DE$. Nevertheless, the complete equilibrium system is also useful because it gives the accompanying cut forces. Taking moments about $E$ eliminates both $F_{DE}$ and $F_{EF}$:

$$
\left\{
\begin{aligned}
\sum F_x=0:&\qquad A_x+F_{CD}+F_{EF}=0,\\
\sum F_y=0:&\qquad A_y+F_{DE}=0,\\
\sum\tau_E=0:&\qquad -9A_y-6F_{CD}=0.
\end{aligned}
\right.
$$

Substituting $A_x=0$ and $A_y=18.75\,\mathrm{N}$ gives

$$
\left\{
\begin{aligned}
F_{CD}+F_{EF}&=0,\\
18.75+F_{DE}&=0,\\
-9(18.75)-6F_{CD}&=0.
\end{aligned}
\right.
$$

Solving gives

$$
F_{CD}=-28.125\,\mathrm{N},
\qquad
F_{DE}=-18.75\,\mathrm{N},
\qquad
F_{EF}=28.125\,\mathrm{N}.
$$

Thus, $CD$ and $DE$ are in compression, while $EF$ is in tension. In particular,

$$
\boxed{DE=18.75\,\mathrm{N}\quad\text{(compression)}}.
$$

This section is especially efficient for $DE$ because $CD$ and $EF$ are horizontal and disappear from vertical force equilibrium.

---

## Final results

### Support reactions

| Reaction | Result |
| --- | --- |
| $A_x$ | $0\,\mathrm{N}$ |
| $A_y$ | $18.75\,\mathrm{N}$ upward |
| $L_y$ | $11.25\,\mathrm{N}$ upward |

### Requested member forces

| Member | Magnitude | Type |
| --- | ---: | --- |
| $DG$ | $33.75\,\mathrm{N}$ | Compression |
| $DF$ | $6.77\,\mathrm{N}$ | Tension |
| $EF$ | $28.125\,\mathrm{N}$ | Tension |
| $DE$ | $18.75\,\mathrm{N}$ | Compression |

### Obvious zero-force members

| Member | Result |
| --- | --- |
| $BC$ | $0\,\mathrm{N}$ |
| $BE$ | $0\,\mathrm{N}$ |
| $JK$ | $0\,\mathrm{N}$ |

---

## Key takeaways for students

1. **External reactions:** Treat the whole supported structure as one rigid body. Use force balance and torque balance.
2. **Pivot choice:** The pivot can be anywhere. A force whose line of action passes through it contributes zero torque.
3. **Zero-force members:** Apply the standard rules only when the joint conditions actually match the rule.
4. **Method of sections:** A planar rigid body gives three independent equilibrium equations, so a section crossing three unknown member forces is usually the most that can be solved directly.
5. **Method of joints:** Isolate one joint at a time and use its two force-balance equations.
6. **Tension versus compression:** A positive result agrees with the assumed tension direction; a negative result means compression.

The central idea is:

> Physics determines the equilibrium equations. We choose the free body, section, and pivot to make those equations easier to solve.
