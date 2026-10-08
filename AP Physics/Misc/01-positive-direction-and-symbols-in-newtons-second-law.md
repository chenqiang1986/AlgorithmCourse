# 正方向、字母含义与牛顿第二定律
*AP Physics / Misc*

> **核心约定：先定义方向，再让字母有唯一含义。**
>
> 学生困惑的根源通常不是正负号本身，而是同一个裸字母有时表示“沿所选正方向的分量”，有时又悄悄表示“大小”。本讲义把这两种含义彻底分开。

## 1. 一套可执行的标准

对一维（或沿某一条约束方向）的受力问题，按下面的顺序书写。

1. **写出正方向的单位向量。** 例如 $\hat{\mathbf y}$ 表示竖直向上，或 $\hat{\mathbf s}$ 表示沿绳子指定的正向。它严格定义了“正”。
2. **默认法则：有方向的量，其裸标量字母表示该向量在正方向上的分量。**

   $$
   a=\mathbf a\cdot\hat{\mathbf s},\qquad
   F=\mathbf F\cdot\hat{\mathbf s}.
   $$

   所以 $a$、$F$、$T_s$ 可以是负数；负号是信息，不是错误。
3. **Override（大小）法则：若要用一个符号表示某个向量的大小，必须写绝对值。**

   $$
   |\mathbf T|,\quad |\mathbf a|,\quad |\mathbf F|.
   $$

   例如 $|\mathbf T|$ 永远非负，而 $T_s=\mathbf T\cdot\hat{\mathbf s}$ 可能为正、零或负。不要让一个没有说明的 $T$ 在同一页里兼任这两个角色。
4. **牛顿第二定律先写成向量式。**

   $$
   \boxed{\sum\mathbf F=m\mathbf a}
   $$

   之后若只需一个方向的信息，再与单位向量点乘。正负号就会由点乘自动产生，而不是靠“记住应该加还是减”。

质量 $m$、重力场强度 $g$、长度等本身没有“方向分量”的物理量，仍是正的物理参数。例如重力写作

$$
\mathbf W=m\mathbf g=-mg\hat{\mathbf y},\qquad g=|\mathbf g|>0,
$$

这里 $g$ 是大小；$\mathbf g$ 才是矢量。

## 2. 先看一个常见的混乱

下面两行若没有额外说明，$T$ 的意思不同：

$$
T-mg=ma \qquad\text{与}\qquad mg-T=ma.
$$

第一行常把 $T$ 当作“向上张力的大小”；第二行又把 $T$ 当作“向上张力的大小”，但把下方当作正向。它们本身可以对，却没有告诉读者 $a$ 是哪个方向的分量，也没有说明 $T$ 是分量还是大小。

用本讲义的写法，若 $\hat{\mathbf y}$ 向上：

$$
\underbrace{\mathbf T}_{|\mathbf T|\hat{\mathbf y}}
+\underbrace{\mathbf W}_{-mg\hat{\mathbf y}}
=m\underbrace{\mathbf a}_{a_y\hat{\mathbf y}}
\quad\Longrightarrow\quad
|\mathbf T|-mg=ma_y.
$$

每个符号只做一件事：$|\mathbf T|$ 是大小，$a_y$ 是向上的分量。

## 3. 统一例题：阿特伍德机

**Example (两质量、轻绳、理想滑轮).** 两物体 $m_L$ 和 $m_R$ 由轻绳跨过无摩擦滑轮连接。忽略绳和滑轮质量，取 $g>0$。设 $m_R>m_L$。求两物体的加速度及绳的张力。

<svg viewBox="0 0 740 340" width="740" role="img" aria-label="Atwood machine with an upward vertical unit vector and a rope-positive direction that goes up the left side and down the right side">
  <defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#174a7c"/></marker><marker id="force" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0,0 L0,6 L7,3 z" fill="#a33a25"/></marker></defs>
  <line x1="140" y1="56" x2="140" y2="205" stroke="#333" stroke-width="4"/>
  <path d="M140 56 A115 115 0 0 1 370 56" fill="none" stroke="#333" stroke-width="4"/>
  <line x1="370" y1="56" x2="370" y2="205" stroke="#333" stroke-width="4"/>
  <circle cx="255" cy="56" r="31" fill="#eceff2" stroke="#333" stroke-width="3"/>
  <rect x="102" y="205" width="76" height="65" rx="5" fill="#d8eaf6" stroke="#174a7c" stroke-width="3"/>
  <rect x="326" y="205" width="88" height="84" rx="5" fill="#f8ddd4" stroke="#a33a25" stroke-width="3"/>
  <text x="121" y="244" font-size="23">mₗ</text><text x="349" y="254" font-size="23">mᵣ</text>
  <line x1="75" y1="188" x2="75" y2="107" stroke="#174a7c" stroke-width="3" marker-end="url(#arrow)"/>
  <text x="21" y="98" font-size="20" fill="#174a7c">ŷ（向上）</text>
  <path d="M191 178 L191 93 Q191 69 216 56 L351 56 Q375 69 375 94 L375 178" fill="none" stroke="#174a7c" stroke-width="3" stroke-dasharray="7 5" marker-end="url(#arrow)"/>
  <text x="191" y="38" font-size="19" fill="#174a7c">+ŝ：左侧向上，右侧向下（沿绳跨过顶部向右）</text>
  <line x1="140" y1="199" x2="140" y2="161" stroke="#a33a25" stroke-width="3" marker-end="url(#force)"/><text x="145" y="177" font-size="18" fill="#a33a25">Tₗ</text>
  <line x1="370" y1="199" x2="370" y2="161" stroke="#a33a25" stroke-width="3" marker-end="url(#force)"/><text x="375" y="177" font-size="18" fill="#a33a25">Tᵣ</text>
  <line x1="140" y1="277" x2="140" y2="320" stroke="#a33a25" stroke-width="3" marker-end="url(#force)"/><text x="145" y="314" font-size="18" fill="#a33a25">Wₗ</text>
  <line x1="370" y1="295" x2="370" y2="329" stroke="#a33a25" stroke-width="3" marker-end="url(#force)"/><text x="375" y="323" font-size="18" fill="#a33a25">Wᵣ</text>
</svg>

理想绳的张力大小处处相同：

$$
|\mathbf T_L|=|\mathbf T_R|\equiv|\mathbf T|>0.
$$

下列四种坐标约定会给出不同符号的“加速度分量”，但同一个物理运动和同一个张力大小。每次都从 $\sum\mathbf F=m\mathbf a$ 出发。

### Convention A：沿绳向右为正

定义 $+\hat{\mathbf s}$ 如图：左边向上、越过滑轮向右、右边向下。令 $a$ 为沿这个绳坐标的加速度分量。因此

$$
\mathbf a_L=a\hat{\mathbf y},\qquad \mathbf a_R=-a\hat{\mathbf y}.
$$

**Solution:**

左、右物体各自应用向量形式的牛顿第二定律：

$$
\begin{aligned}
\mathbf T_L+\mathbf W_L&=m_L\mathbf a_L,
&|\mathbf T|\hat{\mathbf y}-m_Lg\hat{\mathbf y}&=m_La\hat{\mathbf y},\\
\mathbf T_R+\mathbf W_R&=m_R\mathbf a_R,
&|\mathbf T|\hat{\mathbf y}-m_Rg\hat{\mathbf y}&=-m_Ra\hat{\mathbf y}.
\end{aligned}
$$

取 $\hat{\mathbf y}$ 分量并联立：

$$
|\mathbf T|-m_Lg=m_La,\qquad |\mathbf T|-m_Rg=-m_Ra.
$$

$$
\boxed{a=\frac{m_R-m_L}{m_L+m_R}g>0},\qquad
\boxed{|\mathbf T|=\frac{2m_Lm_R}{m_L+m_R}g}.
$$

$a>0$ 的意思恰好是：运动沿所选的 $+\hat{\mathbf s}$，即右物体下落。

$\square$

### Convention B：沿绳向左为正

这次定义 $+\hat{\mathbf s}'=-\hat{\mathbf s}$：左边向下、右边向上。令 $a'$ 是这个新坐标中的分量，于是

$$
\mathbf a_L=-a'\hat{\mathbf y},\qquad \mathbf a_R=a'\hat{\mathbf y}.
$$

**Solution:**

$$
\begin{aligned}
\mathbf T_L+\mathbf W_L&=m_L(-a'\hat{\mathbf y}),\\
\mathbf T_R+\mathbf W_R&=m_R(a'\hat{\mathbf y}).
\end{aligned}
$$

因此

$$
|\mathbf T|-m_Lg=-m_La',\qquad |\mathbf T|-m_Rg=m_Ra'.
$$

$$
\boxed{a'=\frac{m_L-m_R}{m_L+m_R}g<0},\qquad
\boxed{|\mathbf T|=\frac{2m_Lm_R}{m_L+m_R}g}.
$$

$a'<0$ 不是“解错”；它精确地说运动与新选的正方向相反。并且 $a'=-a$。

$\square$

### Convention C：对所有物体都取竖直向上为正

定义唯一的空间单位向量 $+\hat{\mathbf y}$ 向上。令

$$
a_L\equiv\mathbf a_L\cdot\hat{\mathbf y},\qquad a_R\equiv\mathbf a_R\cdot\hat{\mathbf y}.
$$

绳不可伸长给出约束 $a_R=-a_L$；注意它不是“感觉上反着动”，而是关于同一个单位向量的分量关系。

**Solution:**

$$
\begin{aligned}
\mathbf T_L+\mathbf W_L&=m_La_L\hat{\mathbf y},\\
\mathbf T_R+\mathbf W_R&=m_R(-a_L\hat{\mathbf y}).
\end{aligned}
$$

投影到 $\hat{\mathbf y}$：

$$
|\mathbf T|-m_Lg=m_La_L,\qquad |\mathbf T|-m_Rg=-m_Ra_L.
$$

$$
\boxed{a_L=\frac{m_R-m_L}{m_L+m_R}g>0},\qquad
\boxed{a_R=-a_L<0}.
$$

左块的向上分量为正，右块的向上分量为负；这是同一运动的两个坐标描述。

$\square$

### Convention D：对所有物体都取竖直向下为正

定义 $+\hat{\mathbf d}=-\hat{\mathbf y}$ 向下，令 $b_L=\mathbf a_L\cdot\hat{\mathbf d}$。约束仍为 $b_R=-b_L$。现在张力的 $\hat{\mathbf d}$ 分量是 $-|\mathbf T|$，重力的分量是 $+mg$。

**Solution:**

$$
\begin{aligned}
\mathbf T_L+\mathbf W_L&=m_Lb_L\hat{\mathbf d},\\
\mathbf T_R+\mathbf W_R&=m_R(-b_L\hat{\mathbf d}),
\end{aligned}
$$

投影到 $\hat{\mathbf d}$：

$$
-|\mathbf T|+m_Lg=m_Lb_L,\qquad -|\mathbf T|+m_Rg=-m_Rb_L.
$$

$$
\boxed{b_L=\frac{m_L-m_R}{m_L+m_R}g<0},\qquad
\boxed{b_R=-b_L>0}.
$$

下为正时，左块的结果为负，右块的结果为正；这正是图中的实际运动。

$\square$

### Convention E：完全使用正的“大小”——但要把它写成特例

有些教材不先建立一个共同的正方向，而是先根据 $m_R>m_L$ 判断：左块向上、右块向下。然后令

$$
a\equiv|\mathbf a_L|=|\mathbf a_R|>0,\qquad
T\equiv|\mathbf T|>0.
$$

这不是默认分量法；这是一次明确的 **override**。它可用，但每一个方向都必须由箭头或文字给出。

**Solution:**

仍先写向量式：

$$
T\hat{\mathbf y}-m_Lg\hat{\mathbf y}=m_L(a\hat{\mathbf y}),
$$

$$
T\hat{\mathbf y}-m_Rg\hat{\mathbf y}=m_R(-a\hat{\mathbf y}).
$$

把第二式整体乘以 $-1$ 后，才得到两条“大小式”：

$$
T-m_Lg=m_La,\qquad m_Rg-T=m_Ra.
$$

$$
\boxed{a=\frac{m_R-m_L}{m_L+m_R}g},\qquad
\boxed{T=\frac{2m_Lm_R}{m_L+m_R}g}.
$$

这套写法让 $a,T$ 都保持正值，但代价是：必须事先判定实际方向；若猜反了，方程不能“自动”给你一个负数来纠正。这里的裸 $a,T$ 是**明确声明的全正大小约定**，故意暂时取代了本讲义的默认分量法则；课堂上最容易造成混乱的，正是没有声明就把这种大小写法和前四种分量写法混在一起。

$\square$

## 4. 四套分量约定的对照

| 约定 | 裸字母表示什么 | $m_R>m_L$ 时的结果 | 负号说什么？ |
|---|---|---|---|
| 沿绳向右 $+\hat{\mathbf s}$ | 沿绳正向分量 $a$ | $a>0$ | 运动沿绳向右 |
| 沿绳向左 $+\hat{\mathbf s}'$ | 沿新正向分量 $a'$ | $a'<0$ | 实际向右，反于新正向 |
| 竖直向上 $+\hat{\mathbf y}$ | $a_L,a_R$ 为向上分量 | $a_L>0,\ a_R<0$ | 左上、右下 |
| 竖直向下 $+\hat{\mathbf d}$ | $b_L,b_R$ 为向下分量 | $b_L<0,\ b_R>0$ | 左上、右下 |
| 全部取大小 | $a=|\mathbf a|,\ T=|\mathbf T|$ | 两者均 $>0$ | 方向在字母之外另行声明 |

无论选哪一种，物理上不变的是

$$
|\mathbf a|=\frac{|m_R-m_L|}{m_L+m_R}g,
\qquad
|\mathbf T|=\frac{2m_Lm_R}{m_L+m_R}g.
$$

## 5. 交卷前的 30 秒检查

- 我是否写出了 $+\hat{\mathbf e}$，而不仅是“取右为正”？
- 每个有方向的裸标量（如 $a,F_x,T_s$）是否确实是相对同一单位向量的分量？
- 若某个字母是大小，我是否把它写成 $|\mathbf Q|$，或明确声明了它是正的大小？
- 我是否先写了 $\sum\mathbf F=m\mathbf a$，再投影到所需方向？
- 得到负号时，我是否把它翻译成“方向与正向相反”，而不是立即怀疑计算？

最后一个习惯尤其重要：**正方向不是对运动的预测，而是一把尺的朝向。** 选哪边都可以；只要单位向量、字母含义和牛顿第二定律三者一致，答案描述的是同一个世界。
