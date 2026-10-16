# 3. SMT、PSP 与强弱切换（SMT, PSP & Strength Switch）

> **来源**：https://nixtrades.com/notes/03-smt-psp-strength-switch/ ｜ **维护者**：Nix Young ｜ **阅读时长**：7 分钟
> 注：Community insights 为署名社区评论（非逐字笔记），出处按原文保留。

## 概述（In brief）

本章把 SMT、精准摆动点（PSP）和强弱切换（SS）当作一组相互关联的确认工具，用于解读相关性资产、摆动形成与反转时机。它区分一级（one-stage）与二级（two-stage）形态，解释序列 SMT（SSMT）的定义，并把每个工具放进关键位与抽取流动性的更大上下文里。

## 本章解答的问题（Questions this chapter answers）

**在这个框架里，SMT 用来做什么？**
SMT 在一个相关高 / 低点处评估，并由上下文过滤——包括抽取流动性的方向与周围结构的质量。见 §3.1

**什么是精准摆动点（PSP）？**
PSP 把一个摆动点（swing point）与 SMT 结合起来。本章把摆动点、PSP、二级 PSP 结构按确认强度逐级排序。见 §3.2

**什么是强弱切换（Strength Switch）？**
强弱切换是相关性资产之间领先 / 滞后相对关系的变化，在这里用作重新同步与时机确认。见 §3.3

**这里的 SSMT 是什么意思？**
SSMT 被定义为：相对你所用周期上紧邻的前一个高 / 低点（而非更早的某根 K 线）的序列 SMT。见 §3.3

## 3.1 SMT 规则（SMT Rules）

### 社区观点（Community insights）

> **Garrett — "Precision Swing Point", 12:30 ↗**
>
> 市场里每一次回撤、每一次反转，都存在某种形式的 SMT。

> **Garrett — "Precision Swing Point", 22:15 ↗**
>
> 每一次回撤、每一次反转，都携带着某种形式的 SMT。

> **Afyz — trade recap, 5.5R YM short, 11:34 ↗**
>
> "序列 SMT"（sequential SMT）简单说就是两个季度 K 线之间的 SMT——例如 Q2 与 Q3 的那两根 90 分钟 K 线之间。"逻辑流动性目标"（logical liquidity target）不过是均衡（equilibrium）的另一个名字：即你正在交易的那波高周期扩张的 50% 回撤位。

> **Lathyrus Masterclass — Supplementary Lessons — Afyz Mini-Lesson: Asset Synchronization & Phases of Price, 1:20**
>
> "隐藏 SMT"（hidden SMT）指这样一种背离：两个相关资产上被比较的高 / 低点其实并不是在同一天打出的——一个资产的相关高点落在比另一个更早的某一天，这让背离很容易被漏掉，除非你跨天检查高 / 低点、而不只是在当前交易时段内看。

> **TTrades — "SMT Divergence - ICT Concepts", 15:35 ↗**
>
> 不用降周期就能发现"公允价值缺口内部的 SMT"：既然缺口的边界本身就是由一个高 / 低点构成的，检查价格在一个资产上是否越到这条内部边界之上、而在另一个资产上没有——这在功能上就是一次低周期 SMT 读取，只不过直接在高周期图上做。

> **\$niper — "Steal My Asian Session Trading Strategy (Works in all Markets)", 2:05 ↗**
>
> 对这个特定时段策略，把标准的"无 SMT 不交易"规则升级为：专门要求一个序列 SMT——在 6 小时或 90 分钟周期上、相邻季度 / K 线之间的背离——而不只是任何关键位上的任何 SMT。

> **\$niper — "Where to Place your Stop Loss in Trades", 7:28 ↗**
>
> 当一个相关对触及一个公允价值缺口、而另一个对未能触及等效缺口时，这个"未能触及"被当作确认：该缺口是一个真正的脱离缺口（breakaway gap，价格已经跑完它需要的流动性、不必再回来）——这把标准 SMT 背离检查从摆动高 / 低点专门扩展到了缺口触及。

### 反转 SMT（Reversal SMT）

#### 社区观点（Community insights）

> **Garrett — "A Deeper Dive into SMT Divergence", 44:26 ↗**
>
> 一个二级 SMT 不需要两级彼此相邻——第二级可以晚些出现，尽管这种概率较低。

正文：

- 反转通常需要 **二级 SMT**。
- 15m 缺口只适合早期反转，最好在折价（discount）区。
- 不要把溢价（premium）区的 15m 缺口当作反转依据。
- 要确认日内高 / 低点，通常需要：
  - 一个摆动点；
  - SMT；
  - 有时需要二级确认。

### 延续 SMT（Continuation SMT）

- 对于新近形成的缺口，一级 SMT 可用于延续。
- 对于陈旧的缺口，通常需要二级 SMT。
- 对于二级 SMT，第一级理想情况下应发生在关键位。
- 在一个缺口内，通常只需要一级。

### SMT 破裂（SMT Break）

#### 社区观点（Community insights）

> **Garrett — "Precision Swing Point", 19:05 ↗**
>
> 当 SMT 破裂时，市场反转。

> **Garrett — "Asset Synchronisation", 01:14:30 ↗**
>
> 当 SMT 破裂时，价格可以反转。

> **\$niper — "Live Day Trading Making No Money (Luckily Breakeven Day)", 5:02 ↗**
>
> 把一个三资产相关组合中仅一个成员的早期破裂（例如道指跌破其亚洲时段低点、而纳斯达克和标普守住）当作一个即时的实盘风险管理触发——对该组合另一个成员中已经持有的仓位止盈或移到保本，即使那个仓位自己的止损还没被碰到。

> **Garrett — Anomaly Live Trading Stream, 22 Jul 2026**
>
> SMT 破裂就是一次强弱切换。

正文：如果没有 SS（Strength Switch）/ HTF 开盘 / 新关键位来为扩张定时，但市场存在一个滞后资产序列（lagging-asset sequence），把这个条件理解为：

- 一个负面条件；
- SMT 破裂方向变得更重要；
- 优先考虑滞后资产的追赶 / SMT 破裂序列；
- 不要强做原始的反转想法。

### SMT 质量过滤器（SMT Quality Filters）

#### 社区观点（Community insights）

> **Garrett — "A Deeper Dive into SMT Divergence", 14:37 ↗**
>
> K 线实体大小可以用来辅助识别 SMT，尽管这是一个较低概率的信号。

> **Garrett — "A Deeper Dive into SMT Divergence", 24:50 ↗**
>
> 双重扫掠（double-sweep）是 SSMT 的一种有效形式，尽管仍然是低概率。

> **Garrett — "A Deeper Dive into SMT Divergence", 8:52 ↗**
>
> 如果两个资产在日线 / 周线高或低点都没留下影线、之后只有其中一个交易进那个开盘价造出一根影线，这个 SMT 就是低质量的——另一个资产仍然有理由回到它自己的位。

> **Garrett — Entries lecture, 1:14:16 ↗**
>
> 只跟踪与你的抽取流动性方向一致的 SMT。在区间另一侧形成的 SMT 与这笔交易无关——它最多只会产生一次回撤，而不会逆着你的抽取目标反转，所以既不需要把它过滤掉、也不必怕它。

正文：低概率 SMT：

- SMT 高 / 低点不是大致在同一时间打出的。
- SMT 填补形成 EQL / EQH（等低 / 等高），除非有一次 V 形回升。
- 双重扫掠有效，但概率低。
- 溢价区内、贴近的 SMT 带一个摆动，通常更像一次回撤。
- 远离关键位的 SMT 质量更低。
- 有效的 SMT 理想情况下应在关键位。
- 例外：一个带 SMT 的失败摆动（failure swing），如果其他条件支持，仍然可以交易。
- 如果两个资产的日线 / 周线高 / 低点都无影线、之后只有一个交易进那个开盘价造出影线，这个 SMT 就是低质量的——另一个资产仍有理由回到它的位。
- 只跟踪与你的抽取流动性方向一致的 SMT。在区间对侧形成的 SMT 与这笔交易无关——它最多只会产生一次回撤，而不会反转你的抽取目标，因此既不需要过滤掉、也不必害怕。

## 3.2 精准摆动点 PSP（Precision Swing Point, PSP）

### 社区观点（Community insights）

> **Garrett — "Precision Swing Point", 01:55 ↗**
>
> 市场没有摆动点就无法反转，没有 SMT 也无法反转——PSP 就是摆动点加 SMT。

> **Garrett — "Precision Swing Point", 04:55 ↗**
>
> 二级 PSP（SMT+PSP 或 PSP+SMT）排在普通 PSP 之上，普通 PSP 又排在普通摆动点之上。

> **Anomaly — Advanced course — Lesson 5: Candle Confirmations, 5:29**
>
> 一个二级破裂并不总要求它的一级 PSP 恰好发生在关键位本身——PSP 可以在更早一根、远离该位的 K 线上形成，价格只是之后才到达真正的缺口 / 关键位，这个组合仍然算作一次有效的二级确认。

正文：PSP = **摆动点 + SMT**。

市场没有摆动点和 SMT 两者，就无法做出高质量反转。

概率排序：

1. 摆动点（swing point）
2. PSP
3. 二级 PSP
   - SMT + PSP
   - PSP + SMT

关键规则：

- PSP 理想情况下应发生在摆动点处。
- 二级 PSP = 二级 SMT。
- SMT + PSP 是最高概率的反转结构。
- 当 SMT 破裂时，可能制造一次真正的反转。
- 一根驱动 K 线（driver candle）形成 PSP，是一个基于时间的 CiC（Crack in Correlation，相关性破裂），概率更高。
- 脱钩之后，早上 6:00 的 4h 收盘常常会形成一个 PSP，这对上午 10:00 的 4h 重新同步很重要。

## 3.3 强弱切换 SS（Strength Switch, SS）

### 社区观点（Community insights）

> **Garrett — "A Deeper Dive into SMT Divergence", 16:59 ↗**
>
> 缺口大小的差异——一个资产跳空、另一个没有——可以识别出一次强弱切换。

> **Garrett — "A Deeper Dive into SMT Divergence", 20:30 ↗**
>
> 资产之间看涨 / 看跌 K 线倾向的差异，也可以识别出一次强弱切换。

> **Garrett — "A Deeper Dive into SMT Divergence", 36:00 ↗**
>
> 价格位移速度——一个资产比另一个走得快——可以识别出一次强弱切换。

> **Garrett — "Asset Synchronisation", 59:15 ↗**
>
> 当一个资产处于折价、而另一个已经超出溢价，那就是一次强弱切换。

> **Garrett — "How I Confirm Narrative With Drivers", 33:24 ↗**
>
> 相关资产前一天如何收盘可以暗示相对强弱——那个收回到自己区间内部的，比仍然看跌的那个显得更强，这是一条线索，告诉你 SMT 大概会朝哪边化解。

> **Garrett — "A Deeper Dive into SMT Divergence", 4:21 ↗**
>
> 一个资产留下一个缺口不回补、而另一个把缺口补了，是强弱切换显现的另一种方式。

> **Garrett — "A Deeper Dive into SMT Divergence", 4:26 ↗**
>
> 两个相关资产在不同时间收盘跌破同一个摆动低点，或一个先 CiSD、另一个后 CiSD，是相对强弱显现的又一种方式。

> **Garrett — "A Deeper Dive into SMT Divergence", 4:49 ↗**
>
> 一个资产相对其相关对回撤更浅，这本身就是一种强弱切换。

> **Garrett — live back-test stream, 0:13 ↗**
>
> 如果你觉得吃力，就简化到只剩两个设局：用于反转的强弱切换 PSP，以及用于延续的强弱切换 SMT 填补。其他一切都是次要的。

> **Erik — metals live-teaching stream, 33:16 ↗**
>
> 解读一个基于缺口的强弱切换是一段两步叙事：造出缺口的那个资产最初更强，但如果它之后又交易回自己的缺口内、而另一个资产没有，它就变成了更弱的那个——缺口确认强势，交易进缺口确认弱势。

> **Erik — indices strength-switching recap, 13:16 ↗**
>
> 强弱切换不只出现在反转或追赶行情之前——它们也在一段已经进行中的扩张内部持续发生，每个资产会暂时把强势交给另一个。在交易途中注意到这一点，是两个资产正朝同一个抽取目标走的确认，而不是警告信号。

> **Garrett — Q&A stream, 38:57 ↗**
>
> SSMT 永远只问一个问题：刚刚打出 SMT 的那个高 / 低点，是不是某个特定周期上紧邻的前一根 K 线的高 / 低点（前一根 90 分钟、6H、日线或周线）？不比这更早。

### 定义（Definition）

SS = 滞后资产转强，或领先资产与滞后资产之间的相对强弱关系发生变化。

常见形态：

- SSMT（Sequential SMT，序列 SMT）
- PSP
- 缺口大小差异
- 位移（displacement）速度差异
- K 线实体差异
- 看涨 / 看跌 K 线倾向差异
- 双重扫掠，低概率

### SSMT 的定义（SSMT Defined）

SSMT（序列 SMT）是一个基于时间的 CiC：它只问刚刚打出 SMT 的那个高 / 低点，是不是某个特定周期上前一根 K 线的高 / 低点——前一根 90 分钟高 / 低点、前一根 6h 高 / 低点、前一根日线高 / 低点，或前一根周线高 / 低点。仅此而已；它不与所用周期上任何比紧邻前一根更早的 K 线比较。

### SS 的优先级（Priority of SS）

- **SS 凌驾于所有其他共振（confluence）之上。**
- 如果资产脱钩，等待 SS 再入场。
- SS 是资产重新同步（re-sync）的触发。
- SS 确认日内 ERL ↔ IRL，即 DH / DL（日内高 / 日内低）。
- 如果 SS 出现在一次反转处，通常所有资产都会到达抽取目标。
- 如果没有 SS，所有资产都需要一个 V 形，之后才能考虑反转。
- 为扩张定时时，SS 优先于 HTF 开盘和新关键位。

## 3.4 二级 SMT 的形态（Two-Stage SMT Forms）

### 社区观点（Community insights）

> **Garrett — "A Deeper Dive into SMT Divergence", 9:22 ↗**
>
> 二级 SMT 要么表现为同一周期的一个"屋顶"（roof，扫掠之后很快在贴近的高 / 低点发生一次强弱切换），要么表现为一个大的高周期 SMT 被一个更小的低周期 SMT 确认——无论哪种，在一次强弱切换真正确认它之前都不要相信。

正文：二级 SMT 可以有不止一种形态：

- **同周期形态（Same-timeframe form）**：扫掉高低点的那个资产，不久后在一个贴近的高 / 低点切换强弱，有时形状像一个屋顶。
- **高周期 / 低周期形态（Higher-timeframe / lower-timeframe form）**：一个大区间的高周期 SMT（例如一个日线摆动高点），被一个更小区间的低周期 SMT 确认。
- 两种形态在被信任之前，都仍应经过一次强弱切换确认。在强弱切换出现之前，不要假定一级 SMT 已经守住。

## 3.5 PSP 变体（PSP Variants）

### 社区观点（Community insights）

> **Garrett — "GxT | Precision Swing Point | Pt.1", 27:35 ↗**
>
> 机械地看收盘：PSP 是第 2 根 K 线在两个相关资产上都收回到第 1 根 K 线区间内部，但一个收阳、另一个收阴。那个相反的收盘，就是相关性破裂。

> **Garrett — "GxT | Precision Swing Point | Pt.1", 29:56 ↗**
>
> 延续 PSP（Continuation PSP）形成于一次真正反转之后的回撤中，而不是在反转本身——一个资产在那次回撤里打出一个摆动点、另一个没有，正是这个 SMT 结束了回撤、恢复了原来的扩张。

> **Garrett — "GxT | Precision Swing Point | Pt.1", 31:39 ↗**
>
> 强弱切换 PSP（Strength Switch PSP）是最高概率的序列之一：扫掉高 / 低点的那个资产通常是三资产组合里较强的那个，所以当它逆着自己预期的倾向收盘时，这个错配就是叠加在 PSP 之上的一次强弱切换。

正文：

- 机械地看，PSP 是第 2 根 K 线在两个相关资产上都收回到第 1 根 K 线区间内部、但方向相反的那个——一个收阳、一个收阴。那个相反的收盘就是 CiC。

- **延续 PSP（Continuation PSP）**：形成于一次真正反转之后的回撤之中，而不是在反转本身。一个资产在那次回撤里造出一个摆动点、另一个没有，从而形成一个 SMT——这是回撤结束、原始扩张恢复的触发，而不是一个新的反转信号。

- **强弱切换 PSP（Strength Switch PSP）**：扫掉一个高 / 低点的资产通常是三资产组合中较强的那个，但它反而逆着自己预期的倾向收盘。这个错配本身就是一次强弱切换，叠加在 PSP 之上，是可交易的最高概率序列之一。

## 3.6 真正反转的确认次序（Confirmation Ordering for a True Reversal）

### 社区观点（Community insights）

> **Afyz — Master Class Q&A / tutorial session, 42:36 ↗**
>
> 每远离真正反转一步，所需的相关性破裂就少一级：反转本身需要两级，它造出的延续缺口需要一级，而一旦你在那个缺口内部交易低周期分形，除了一个普通 V 形反转信号之外就什么都不需要了。

> **Erik — metals live-teaching stream, 11:34 ↗**
>
> 看着像高周期延续的，在你实际执行的低周期上可能是一次真正的反转——而反转需要两级相关性破裂，不是一级。对一个本质上是嵌套反转的东西只用一级去尝试，就是它失败的原因。

> **GxTradez — "A Complete Trading Framework (Universal Models, SMT, Swing Points)", 12:16 ↗**
>
> 一张把具体确认组合对应到每个通用模型（Universal Model）变体的清单：单独一个 SMT 填补对 Internal→External 就够了；单独一个摆动点 SMT 对 External→Internal 就够了；单独一个 PSP 只"暗示"（并未完全确认）一次真正的 External→External 反转；最高概率的组合是关键位上的 SMT 加一个二级 PSP（即 PSP 本身又被一个摆动点 SMT 确认）。

> **\$niper — "How To Perfect Your Swing Trading | \$AUDJPY Trade Breakdown | Market Maker Buy Model", 5:59 ↗**
>
> 一条处理冲突周期信号的显式优先级规则：当低周期（小时线）SMT 读取暂时偏向组合中相反的那个资产时，坚持既定的高周期（日线 / 周线）倾向、不要翻转——LTF 读取被置于 HTF 倾向之下。

> **\$niper — "My Biggest Swing Trade Yet | The Forever Model | \$GBPJPY Trade Breakdown", 6:24 ↗**
>
> 当中期 SMT（一个小时线 / 短期低点读取）与高周期（日线）SMT 读取矛盾时，把高周期 SMT 当作主导、仍然按它交易——这是一条显式的 SMT 冲突化解规则。

正文：一次真正的反转永远需要两个 CiC，但哪一个先形成，决定了第 2 根 K 线本身是否可交易、还是必须等第 3 根 K 线：

- **PSP 确认 SMT（PSP confirms SMT）**：一个精准摆动点先在关键位收盘，随后一个连续 K 线 SMT 在第 2 根 K 线仍开盘时确认它。因为二级破裂已经完成，第 2 根 K 线本身就可以当作反转来交易。

- **SMT 确认 PSP（SMT confirms PSP）**：先形成一个 SMT，但该摆动要等到那根 K 线作为 PSP 收盘才被确认。由于二级破裂直到收盘才完成，你无法实时信任第 2 根 K 线——等待第 3 根 K 线，把它当作延续来交易。

- **二级 PSP 加二级 SMT（Two-stage PSP with two-stage SMT）**：形成一个二级 PSP，它造出的高或低点随后又被第二个、独立的二级 SMT 跑过并重新确认。这个三级组合更罕见，但一旦出现就是一个非常高概率的信号。

- 如果根本没有二级 CiC——例如只有一个单独的 PSP、或只有一个没有确认的单独 SMT——那就不是真正的反转，这个分形不应交易。

- 作为经验法则，每远离反转一步，所需的 CiC 数量就减一：真正的反转本身需要两个；它造出的高周期延续缺口需要一个（一次 SMT 填补或单个 PSP / SMT 收盘就够）；在那个缺口内部交易的低周期反转信号，除了 V 形反转信号本身之外不再需要任何东西，因为高周期的破裂已经完成了过滤。

### 跨周期确认一次反转（Confirming a Reversal Across Timeframes）

一根 K 线自己的周期并不总能直接显示出二级破裂。有三种情况：

1. **同周期确认（Same-timeframe confirmation）**：该 K 线在自己的高 / 低点处就打出了二级 CiC——直接交易它，不需要进一步轮廓分析。

2. **低周期轮廓分析（Lower-timeframe profiling）**：该 K 线在自己周期上没有二级破裂，但一个更低周期（例如用一个 4h 摆动去轮廓分析一根日线 K 线的影线）反而显示出二级破裂。用那个低周期确认来信任这根高周期影线。

3. **任何相关周期上都没有确认（No confirmation on any relevant timeframe）**：该 K 线自己的周期、以及合适的更低周期，都没有显示二级破裂。这里没有真正的反转——等待该 K 线收盘，然后从它造出的新失效位改做延续。
