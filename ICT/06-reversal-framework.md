# 6. 反转框架（Reversal Framework）

> **来源**：https://nixtrades.com/notes/06-reversal-framework/ ｜ **维护者**：Nix Young
> 注：Community insights 为署名社区评论（非逐字笔记），出处按原文保留。

## 概述（In brief）

本章围绕关键位、摆动形成与位移，组织反转的上下文、确认、失效与低周期精化（lower-timeframe refinement）。它解释支持一次反转需要哪些组件、何时应改为等待延续，以及一次失败的反转如何改变下一步决策。

## 本章解答的问题（Questions this chapter answers）

**在这些笔记中，什么支持一次反转？**
框架组合了关键位、SMT、摆动点、SS / PSP 确认、位移以及支持的形态或时间上下文。见 §6.1

**当没有反转信号时会发生什么？**
本章说不要直接交易反转；取而代之，等待一个合适的延续设局及其确认。见 §6.2

**如何处理失败的反转？**
一旦反转失败，框架把注意力转向相关的失效位和延续入场，而不是强行再来一次反转。见 §6.4

## 6.1 基本反转条件（Basic Reversal Conditions）

### 社区观点（Community insights）

> **Garrett — "Filter Price through 'Candle Profiles'", 46:16 ↗**
>
> 任何时候你在逆着更高周期趋势交易（fading the HTF trend），都应该有一个 SSMT 在场。

> **Garrett — "4H Profiling", 43:20 ↗**
>
> 你要交易的是操纵（manipulation），因为正是操纵形成了扩张——但它需要 SMT 相伴，这样你才知道这是真正的反转。

> **Garrett — "Asset Synchronisation", 46:40 ↗**
>
> 真正验证反转的是位移（displacement）。

> **MMXM Trader — Double Purge Theory, 0:13 ↗**
>
> 市场只有在价格同时打掉买方和卖方（"双重清算"，double purge）之后才会真正反转，只打掉市场单边是不够的。真正能守住的 PD array（订单块、Breaker、公允价值缺口）是双重清算之后形成的那些，而不是之前形成的。

> **MMXM Trader — Draws on Liquidity and Turtle Soup Levels, 3:26 ↗**
>
> 真正的海龟汤（turtle-soup）反转位不是随便一个先前的高点或低点——它特指造成最近一个更高低点（上涨趋势中）或更低高点（下跌趋势中）被打破的那个摆动，因为那正是经典更高高点/更高低点市场结构逻辑下，散户止损与突破买入/卖出止损同时聚集的地方。打掉这个特定位通常产生异常快速、低阻力的行情，因为这波行情一次性蚕食了散户两边的止损，而不是只吃一边。

> **Lathyrus Masterclass — Supplementary Lessons — Afyz Mini-Lesson: Continuations, 47:43**
>
> 反转与延续交易处在定义性权衡的两端：反转提供更大的空间（因而更高的 R:R），恰恰因为它要求更少的既有结构——你是在抓转折本身，所以可能出错的地方更多；而延续提供更小的空间（更低的 R:R），但要求更多结构，因为你交易的是一个已经确立的抽取目标，可能出错的地方更少。

> **Lathyrus Masterclass — Supplementary Lessons — Afyz Mini-Lesson: Continuations, 48:15**
>
> 经验法则：需要保护资金曲线（更看重胜率而非原始 R:R）的较新手交易者应偏向延续设局；更有经验的交易者可以自由选择反转或延续，取决于当天哪个看起来最干净，无需固定偏好。

> **Lathyrus Masterclass — Supplementary Lessons — Afyz Mini-Lesson: Gap Selection Lecture (Continuation Part 2), 0:10**
>
> 如果一笔逆着日线/周线倾向（bias）的反转发生在交易日很早的时候，可以把它当作日内安全可做的，而不必等待完整的日线收盘——那种情况下等待只会把信号推迟到下周的 K 线，没有任何额外好处。

> **AP — "Use Market Structure & Fibonacci Levels for Sniper Entries", 36:19 ↗**
>
> 对结构翻转后的第一个新高/新低保持怀疑——首次突破容易在远离真正高周期区域的位置制造假动作——在承诺反转解读之前，等待同一方向的第二次延续性突破。

> **TTrades — "TTrades Fractal Model - Trading Candle 3", 11:25 ↗**
>
> 更高周期倾向的强弱像音量旋钮一样决定你交易入场周期的激进程度：当 HTF 延续倾向很强时，低周期反转可以直接逆着眼前的局部信号交易；当倾向较弱时，等待低周期也先显示出它自己的延续。

> **TTrades — "TTrades Fractal Model - Trading Candle 3", 19:32 ↗**
>
> 一个用于区分真正反转与单纯盘整的收盘速度诊断：真正的反转应该快速收盘穿越该位；如果穿越过程拖拖拉拉，就把这次动作当作盘整在区间内来回洗，而不是有效反转——即使价格技术上最终还是越过了该位。

> **TTrades — "How To Trade Reversal - Phases Of Price", 2:43 ↗**
>
> 判断什么才算真正相关的反转位的最简启发式：默认用前一日或前一周的高 / 低点，因为它们"总是相关"——只有当两者都不可用时，才保留基于判断的摆动挑选。

正文：一个高质量反转通常需要：

- 关键位被触及
- SMT
- 摆动点
- SS / PSP / SSMT
- 位移 / 缺口
- K 线形态支持
- 时间窗口或驱动事件支持

基本公式：

**反转 = 关键位 + SMT + 摆动点 + SS / PSP + 位移**

Afyz 总结：

反转的根本真理 = CiC + 位移 / 缺口

底层逻辑：

- 市场需要摆动形成才能反转。
- 摆动形成需要关键位。
- CiC 验证该摆动形成。
- 相关性破裂之后的反转信号确认扩张时机。
- CiC 确认倾向；它本身不创造倾向。

## 6.2 反转入场（Reversal Entry）

### 社区观点（Community insights）

> **Garrett — "4H Profiling", 44:20 ↗**
>
> 在反转 K 线的下半/上半部分里，尽可能把仓位放在合理的最低/最高处——但不要过度贪心，因为你不知道反转会走多远。至少，你的止损应该放在那里。

正文：当关键位被触及时：

**如果有反转信号**
（含义：SMT + 经 PSP / SSMT 确认的 SS）

- 交易反转。
- 对于 HTF 4h+ 的 SMT + PSP，不需要额外的 LTF SMT。
- 入场可以放在反转 K 线的折价 EQ（discount EQ）。
- 止损放在 SMT 失效位之外。
- 早入场更容易把止损移到 BE（保本）。

**如果没有反转信号**

- 不要直接交易反转。
- 等待一个延续设局：
  - universal sequence（通用序列）；
  - 15m+ 缺口回测；
  - 30m+ 确认，尤其对晚段延续。

## 6.3 反转的两次机会（Two Chances to Reverse）

### 社区观点（Community insights）

> **Garrett — "GxT Invalidations | Continuations", 04:44 ↗**
>
> 一次反转有两次机会：从关键位的摆动点扩张离开，或者 C2 摆动点先被操纵。如果两次都失败，反转即被失效。

正文：在关键位，一次反转有两次机会：

- 从摆动点扩张离开；
- C2 摆动点被操纵，然后价格反转。

如果两次都失败，反转即被失效。

## 6.4 反转失效（Reversal Invalidation）

### 社区观点（Community insights）

> **MMXM Trader — Counter-Trend Trading Models, 7:21 ↗**
>
> 逆势设局：当区间外流动性被抽取时，若当前抽取目标的对面坐着一个未被修复（unmitigated）的日线公允价值缺口，观察连续三根日线 K 线各自收盘在前一根 K 线的高/低点之内（"三次推动"，three drives）。只要该缺口保持开放，第四天就可以逆势交易回缺口内——如果缺口先被修复，就把该形态视为失效。

> **Anomaly — Lessons — Invalidation Lecture, 26:19**
>
> 一个交易时段的开盘形态本身就兼作失效检查：如果当天先开高而没有确立低点（支持做空倾向），但随后价格做出与该形态暗示相反的动作，把这当作可能的失效信号，而不是等待一个单独的确认。

> **TTrades — "Trading the Invalidation of Daily Bias", 0:41 ↗**
>
> 一个闭合的两项分类，说明哪些日线倾向失效实际可交易：一个逆着原倾向形成的对手方 C2（candle-2）设局，或者价格在配对的低周期上收盘越过前一根 K 线的 EQ——任何其他类型的失效（例如单纯盘整侵蚀倾向）都不被视为可以在相反方向交易。

正文：交易失效的唯一高概率方式：

- 在整体 DoL 内找到离反转最近的相关内部关键位；
- 该位是最可能的失效点；
- 等待价格未能反转；
- 然后寻找延续 / 失效入场。

如果反转交易失败，等待延续交易。

## 6.5 失败摆动交易（Failure Swing Trading）

### 社区观点（Community insights）

> **Garrett — "How I Confirm Narrative with Drivers", 07:13 ↗**
>
> 对失败摆动设局来说，SMT 不是必需的过滤器——摆动、SS 和离开的缺口才是关键。

> **Lathyrus Masterclass — Supplementary Lessons — Afyz Mini-Lesson: Phase of Price & Asset Synchronization, 1:10:18**
>
> 一个特定形态被称为整个框架中单一最高概率的延续序列：由真实反转留下的失败摆动，之后回撤进入该缺口自身的 EQ——在延续概率上排在所有其他 PSP/SMT 组合之上。

> **Lathyrus Masterclass — Supplementary Lessons — Afyz Mini-Lesson: Asset Synchronization & Phases of Price, 0:35**
>
> 当低周期模型自身的抽取目标相对于高周期模型只是一个失败摆动时，这是高概率信号，表明内部到外部的行情应该穿过它继续，而不是在那里反转——在一个只高出（一个分形层级的）失败摆动位，没有结构性理由去反转。

正文：交易失败摆动：

- 必须要有 SS；
- 必须要有离开的缺口（gap away）；
- 不要仅仅因为出现失败摆动就交易；
- 失败摆动必须由强弱切换和位移验证；
- 在区间盘整中，SMT 通常会验证失败摆动；
- 如果干净的 CiSD 距离太远，可以使用失败摆动 CiSD。

简化规则：

**失败摆动交易 = 失败摆动 + SS + 离开的缺口**

## 6.6 反转信号的两种形式（Two Forms of Reversal Signature）

### 社区观点（Community insights）

> **Garrett — "How I Confirm Narrative With Drivers", 7:52 ↗**
>
> 反转信号可以以两种方式出现：立即的"扩张进入该位、再扩张离开该位"并由 CiSD 确认；或者较慢的版本，第 1 根 K 线操纵、第 2 根 K 线盘整、扩张实际显现在第 3 根 K 线。

> **MMXM Trader — How Highs and Lows Form, 1:44 ↗**
>
> 当价格第一次深入一个结构区间的高/低点时，先不要降周期——停留在该区间自身的周期上，让第一根 K 线完整收盘，然后读它的形态。如果它是反转 K 线，或带有长影线/犹豫收盘，不要预期该位会被再次探访——真正的高/低点很可能正在那里形成，之后形成的 PD array 是可交易的。但如果它带着完整实体收盘越过了该位（没有反转信号、没有长影线），预期该位会在后面的 K 线上被再次运行——真正的极值在那里形成，而不是在这一根。被止损出局后眼看着价格继续走，通常就是在这两种 K 线类型中搞错了该降周期的那一种。

> **TTrades — "Reversal Sequence (TTRS) - How To Blend PD Arrays", 4:50 ↗**
>
> 一个形成中反转的显式确认阶梯，按确定性与入场时机的递进排序：(1) 高/低点的清算/海龟汤（若已有 SMT 可跳过），(2) 反转（收盘重新穿越制造扫掠腿的 FVG），(3) 交付状态改变 / 订单块形成，(4) 最后的 Breaker 块和/或 FVG，大致可互换。

正文：一种形式是即时的：触及关键位、形成摆动，看到扩张进入该位、随后扩张离开，由 CiSD 确认。

另一种形式先盘整：第 1 根 K 线操纵该位，第 2 根 K 线盘整或收盘，扩张实际显现在第 3 根 K 线。

无论哪种形式，底层仍需要摆动点、关键位和 CiC 来支持交易。

## 6.7 通过低周期分形精化入场（Refining Entry via Lower-Timeframe Fractal）

### 社区观点（Community insights）

> **Afyz — "True Reversal Logic" trade breakdown, 4:53 ↗**
>
> 覆盖宽大的反转 K 线影线，与等待同一反转的更紧凑的嵌套低周期分形（nested lower-timeframe fractal），两者到达同一个抽取目标——但嵌套分形给出明显更好的盈亏比。

> **Anomaly — Advanced course — Lesson 3: Invalidations Refinement, 12:08**
>
> 一个精化后的关键位可以同时验证两根不同的嵌套 K 线——例如，一个位于前一根 4h K 线上半部分的小时摆动，可以同时确认日线 K 线扩张的延续以及那根 4h K 线自身区间的延续。

> **Anomaly — Advanced course — Lesson 3: Invalidations Refinement, 7:34**
>
> 为嵌套摆动/入场选择的精确低周期配对不必遵循固定规则——30 分钟摆动精化到 3 分钟或 5 分钟入场是可互换的选择，小时摆动与其自身合适缩放的入场周期同理。

> **Lathyrus Masterclass — Supplementary Lessons — Afyz Mini-Lesson: Phase of Price & Asset Synchronization, 1:14:06**
>
> 当有多个有效的低周期位可用于精化入场时，优先选一个全新的、未被触碰过的嵌套分形，而不是已被探访过的——例如一个未被触及的 1h 缺口，优于一个价格已经访问过一次的 30m 缺口——即使两者技术上仍然有效。

> **Lathyrus Masterclass — Supplementary Lessons — Summit Exclusive: Final Q&A, 1:01**
>
> 当几个低周期分形都能确认同一个摆动时，如果更精细的那个（例如 1 分钟优于 3 分钟）能产生干净、精确对齐的失效位，就选它——它同时给出更好的入场价格和更利落的止损参考。

> **TTrades — "Improve Your Trade Entries Within Fair Value Gaps (FVG)", 0:13 ↗**
>
> 在异常大的公允价值缺口内收紧入场的三种可互换方式，收敛到相近的价格：(1) 用 0.5 fib 分割缺口，在中点而非远端入场；(2) 向左看是否有与缺口对齐的订单块或 Breaker，从它的开盘入场；(3) 降到更低周期，在同一区域内寻找更小的嵌套失衡。每一种都以更低的成交率换取更小的风险——没有哪一种比另一种更"正确"。

正文：同一反转可以有两种交易方式：用宽止损覆盖反转 K 线自身的影线；或等待下一根 K 线开盘，交易同一反转的更小嵌套分形，以获得更紧的止损。

两者到达同一个抽取目标，但冒嵌套分形的高 / 低点而不是整根反转 K 线影线的风险，能显著改善盈亏比。

以与高周期反转相同的方式确认嵌套分形：在其自身高 / 低点有 SMT，随后有它自己的 CiSD。
