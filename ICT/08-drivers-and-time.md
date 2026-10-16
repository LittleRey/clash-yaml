# 8. 驱动事件与时间（Drivers & Time）

> **来源**：https://nixtrades.com/notes/08-drivers-and-time/ ｜ **维护者**：Nix Young ｜ **阅读时长**：3 分钟
> 注：Community insights 为署名社区评论（非逐字笔记），出处按原文保留。

## 8.1 驱动事件叙事（Driver Narrative）

### 社区观点（Community insights）

> **Garrett — "How I Confirm Narrative with Drivers", 11:45 ↗**
>
> 驱动事件之前是否已经先有一次反转，决定了这次是延续还是反转——8:30 的操纵往往引向 9:30/10:00 的延续，9:30 的操纵引向 10:00 的延续。

> **Garrett — "A Deeper Dive into SMT Divergence", 38:42 ↗**
>
> 如果一个 SSMT（序列 SMT）在驱动事件之前形成，预期驱动事件会扩张。

> **Garrett — "How I Confirm Narrative With Drivers", 12:25 ↗**
>
> 如果一个驱动事件交易进一个尚未确立的关键位并未能在那里反转，那就使整天的形态失效，而不只是那一个设局。

> **Garrett — "How I Confirm Narrative With Drivers", 10:50 ↗**
>
> 当一个驱动事件开盘、从之前那次反转的 CiSD 处交易离开、印出一根对手方 K 线并收盘穿回它时，这个驱动事件就确认了延续。

> **Garrett — "4H Profiling", 17:04 ↗**
>
> 6am 反转之所以优于 2am 或 10am，正是因为 8:30/9:30 两个驱动事件落在这个 4H 窗口内，让这次反转有一个驱动事件可以配对。

> **Garrett — weekly trade recap (3K subscribers), 4:55 ↗**
>
> 当日高/低点在驱动事件之前形成时，驱动事件应从它那里离开扩张——那才是该位真实的确认。如果驱动事件反而未能反转或不尊重那个位，把它当作红旗，而不是照交易那个位。

> **Garrett — trade recap, January 2, 31:00 ↗**
>
> 如果前一周或周五已经扩张过，不要预期周一继续那个扩张——预期它反而回撤回前一周的区间，而且预期这次回撤发生在周初而不是周末。

> **The MMXM Trader — "Advanced ICT MMXM Lesson (Everything You Need To Know)", 3:24 ↗**
>
> 用交易者持仓报告（COT）数据作为高周期倾向输入：只看单个期货合约（绝不看交叉盘或 CFD），取过去 12 个月数据，把区间对半分，在一个关键时间点（新季度开盘）检查商业机构/央行相对于那条中线是否处于极端——12 个月区间顶部的读数被解读为最大净多头仓位，映射到图表自身的极值。

> **\$niper — "The Market Maker Sell Model & Quarterly Theory | Full Trade Breakdown \$OIL", 0:33 ↗**
>
> 在看日内价格之前，叠加多年季节性图表（例如原油 39 年月度 OHLC 倾向、白银 5/15/40 年图表）作为技术 SMT 解读之外的补充方向倾向输入——这是一类（历史日历倾向）分析，在本站其余纯价格行为框架中是缺席的。

> **\$niper — "Making \$18,591 Trading \$NQ and \$GOLD", 9:41 ↗**
>
> 一个不在经济日历上的突发事件头条，落在已经预期中的派发窗口内，可以像一个排期驱动事件一样把交易送到目标——驱动事件时机框架同样适用于临时头条风险，而不只是排期发布。

正文：核心规则：

| 驱动事件之前的状态 | 预期 |
|---|---|
| 反转已在驱动事件之前完成 | 驱动事件延续 |
| 反转尚未在驱动事件之前完成 | 驱动事件反转 |
| 驱动事件未能反转 | 失效 |
| 价格在驱动事件之前回撤进一个缺口但未反转 | 驱动事件扩张 |
| 8:30 操纵 | 9:30 / 10:00 延续 |
| 9:30 操纵 | 10:00 延续 |

- 如果价格在驱动事件之前操纵但未能反转，驱动事件应离开扩张。
- 如果价格在驱动事件之前回撤进一个缺口但未反转，价格应从驱动事件处扩张。
- 如果 SSMT 在驱动事件之前形成，驱动事件应扩张。

## 8.2 驱动事件使用规则（Driver Usage Rules）

### 社区观点（Community insights）

> **Garrett — "GxT Invalidations | Continuations", 47:52 ↗**
>
> 如果价格在驱动事件之前操纵但未能反转，预期驱动事件离开扩张。

> **Garrett — "Precision Swing Point", 24:00 ↗**
>
> 当制造驱动事件的那些 K 线——例如 8:30 数据前的 8am K 线，或 9:30 开盘前的 9am K 线——形成一个 PSP 时，那就是基于时间的 CiC，概率更高。

> **MMXM Trader — News Trading Cheat Sheet, 1:56 ↗**
>
> 股指期货上一次 8:30am 新闻发布通常以两种方式之一展开：要么 8:30 本身就是操纵、9:30 是派发；要么 8:30 先把价格泵向错误方向、还没有打出真正行情所需的止损——那种情况下 9:30 会第二次（与 8:30 同方向）打出那些同样的止损，然后才猛烈反转进入派发。

> **MMXM Trader — News Trading Cheat Sheet, 10:16 ↗**
>
> 对 FOMC，等最后的新闻发布会完全过去，2:45pm 之前不要进场。真正的行情通常发生在收盘前最后一小时（约 3pm），而且它通常会先跑掉两侧流动性，然后才启动真正的行情。

> **\$niper — "This Stupid Simple Trading Strategy Made Me \$3,500 in 1 hour (Copy My Exact Method)", 6:45 ↗**
>
> 如果在一个排期发布（哪怕不是头条级）之前的关键时间已经形成了预发布操纵/SMT，预期这次发布会延续那个动作而不是反转它——"市场不会操纵两次。"作为一般规则陈述，并在多个视频中重复。

> **\$niper — "How I Find Your Daily Bias Simplified ICT Concepts", 12:54 ↗**
>
> 个人执行规则：在高影响力新闻发布后等特定的 30 分钟再交易，而不是立刻进场。

> **\$niper — "How I Made \$4,797.42 Live Trading | Forever Model", 5:28 ↗**
>
> 指出一个常见散户错误：一旦一个排期发布已经制造出 SMT/操纵，价格不需要在向抽取目标扩张之前再次操纵同一个低点——等第二次扫掠会让你错过行情。

正文：

- 如果价格接近一个驱动事件，就等驱动事件。
- 在驱动事件周围，LTF CiSD 是可接受的。
- 驱动事件是逆着影线交易（fade a wick）最容易的方式。
- 如果一根驱动事件 K 线形成 PSP，它就是基于时间的 CiC，概率更高。
- 如果一个驱动事件形成反转，通常只需要单段（1 stage）。
- 如果价格在驱动事件之前回撤进一个缺口且未能反转，把驱动事件用作扩张时机参考。

## 8.3 筛选相关驱动事件（Filtering Relevant Drivers）

### 社区观点（Community insights）

> **Garrett — "How I Confirm Narrative With Drivers", 0:26 ↗**
>
> 把你的新闻日历过滤到你实际交易的那个品种、并且只留红夹（red-folder）事件——指数只关心美元新闻，原油走它自己的能源日历，外汇只关心它自己那对货币的两种货币。

> **AM — "Weekly Profiles For Daily Bias", 5:16 ↗**
>
> 一条常备规则：完全避免周一交易（在所有周线形态下，周一永远只是 Judas swing、盘整或反转，绝不是扩张日），并避免一周内第一个重要高影响力发布之前的每一天——那些前导日往往只是在它之前积累/盘整。

> **AM — NFP trade recap, 0:38 ↗**
>
> 在 NFP 周，把通常的发布前谨慎延伸到 NFP 前一天（周四）和周一：周四往往在发布前积累、然后数据一出被两侧操纵，所以周二、周三和发布后的周五才是那周真正值得找交易的高概率日。

> **AM — Continuation trade breakdown, 3:24 ↗**
>
> 不是每个高影响力发布都配同样的"前一天"谨慎：CPI（或 FOMC 会议纪要）前一天仍然可以交易，只是稍加谨慎——这与 NFP 前一天（完全避免）区别对待。

> **MMXM Trader — \$65K Week Breakdown, 11:31 ↗**
>
> 当一天内在股指期货上同时有 8:30 和 9:45 两个红夹新闻发布（"两阶段"新闻事件）时，10am 之前不要交易——两个发布之间那段时间往往震荡，10am 才是真正行情开始的地方。

> **MMXM Trader — News Trading Cheat Sheet, 11:24 ↗**
>
> 对 NFP，等 8:30，然后看它往哪边破：如果 NFP 顺着高周期抽取目标方向派发，整天别做——很可能一团糟。只在 NFP 逆着高周期抽取目标操纵时才参与，因为那会在 9:30 和/或 10am 给出一个干净（一些）的头皮机会——10am 通常是两者中更干净的那个。

> **Lathyrus Masterclass — The Lathyrus Model — Lecture 10: Driver Pairing, 0:35**
>
> 在那几个值得跟踪的驱动事件窗口中，8:30 往往承载最重的发布（CPI、NFP），通常是两个 AM 时段中更重要的；9:30/10:00 相比之下通常更轻。

> **Lathyrus Masterclass — The Lathyrus Model — Lecture 10: Driver Pairing, 2:21**
>
> 一个值得关注的特定三阶段升级：8:30 驱动事件开盘后原地不动（一根失效/震荡 K 线），9:30 才对相关摆动和失败摆动一起完成真正的操纵，10:00 开盘并把扩张送到抽取目标。

> **AM Trades — "Blending The Economic Calendar, Daily Chart, & Weekly Profiles", 6:05 ↗**
>
> 一个比单纯"只看高影响力"更锐利的三层新闻影响分类：高影响（CPI、FOMC 新闻发布会、NFP）——避免之前那一天，专注于之后交易；中影响（GDP、PCE、核心 PPI）——不要在发布前一刻进场或持仓穿过去，但不需要提前整天避开；低影响（大多数其他发布）——通常可以安全持仓穿过，当作背景噪音。

> **AM Trades — "Blending The Economic Calendar, Daily Chart, & Weekly Profiles", 25:48 ↗**
>
> 对 FOMC 周具体而言：避免周一、周二，以及周三美东时间 2:30pm 之前的一切——把 2:30pm 新闻发布会本身（而不是更早的 2:00pm 声明或 FOMC 纪要）当作真正为周四/周五设局的事件。

> **TTrades — "How To Use The Economic Calendar For Trading", 1:35 ↗**
>
> 一张分级的三层新闻限制表（归功于 AM Trades）：高影响——避免前一天、避免发布本身、之后看；中影响——不需要避免前一天，但避免发布前一个时段、避免发布、之后看；低影响——完全无限制。

> **\$niper — "How I Frame My Weekly Bias & Narrative", 3:13 ↗**
>
> 当一周经济日历显示直到周中才有排期高影响力新闻时，把之前整段多日都当作低信念期，并在整段期间降低仓位，除非一笔交易同时有强高周期叙事支撑——这是周级别的宏观窗口纪律，区别于日内窗口纪律。

> **\$niper — "This \"Secret\" Trading Strategy Makes Me Over \$10k/Month", 1:26 ↗**
>
> 在注意到亏损日集中在那周排期高影响力新闻驱动事件的前一个工作日之后，立了一条规则：不仅在驱动事件当天降优先级，也在已知驱动事件前一天降优先级。

> **\$niper — "The Market Maker Sell Model & Quarterly Theory | Full Trade Breakdown \$NQ", 2:44 ↗**
>
> 当一周内有两个重大日历事件（例如 FOMC 新闻发布会加 NFP）时，把整周当作低概率，只取附近目标这种"低垂果实"，而不是大的区间外抽取目标。

> **\$niper — "How I Made \$961.90 Live Trading NQ", 3:25 ↗**
>
> 在 NFP 周，刻意用更小的执行周期配对（小时→5m 而不是 4H→15m），这样到目标所需的点数波动更小，理由是这适合 NFP 前通常较低波动的价格行为。

正文：

- 只在真正影响所交易品种的红夹新闻事件周围交易。把日历过滤到该品种、且只留红夹影响。
- 对指数而言，只有美元红夹新闻相关，而 9:30 纽约证券交易所开盘是指数专属时间。它不适用于黄金、原油或外汇。
- 8:30 本身并不重要。只有当当天确实有一个红夹 8:30 新闻事件时它才重要。
- 原油/能源驱动事件来自能源日历，不是美元日历。美元新闻不驱动原油。
- 谨慎协议：避免在 NFP、CPI 或 FOMC 新闻发布会当天、发布前一刻直接进场。交易发布前一天没问题。

## 8.4 围绕驱动事件的仓位入场（Positional Entries Around Drivers）

### 社区观点（Community insights）

> **Garrett — "How I Confirm Narrative With Drivers", 18:36 ↗**
>
> 最干净的驱动事件设局发生在日线 K 线还处在 protraction（延展）阶段时（正在形成影线、尚未扩张）——那时候一次操纵最可能产生干净、单边、无回撤的扩张。

> **AM — Weekly trade review, 10:28 ↗**
>
> 在次日开盘附近（确认之前）做一个仓位入场，只有两个条件同时满足才合理：当天完全单边的倾向（另一侧什么都不做），以及前收盘已经把附近的对手方颜色 K 线验证为可以隔夜持有的支撑。

> **Lathyrus Masterclass — Supplementary Lessons — Summit Exclusive: Final Q&A, 0:22**
>
> 在极深过 50% 的区间深处、离最终抽取目标很近处做延续，有时会留下没有空间做一个干净的 CiSD 确认入场。在那种特定情况下，仅凭交易区间逻辑入场是可接受的，而不是跳过交易——但一有确认就迅速移到保本，因为没有空间留给更深的止损。

> **Lathyrus Masterclass — Supplementary Lessons — Summit Exclusive: Final Q&A, 0:23**
>
> 同一个突破缺口延续可以两种方式交易：在缺口内早做仓位入场（止损更便宜、出错风险更高），或等完全收盘穿过该位后做确认入场（更安全、R:R 更差）——框架为风险偏好的选择，而不是单一"正确"方式；仓位版通过价格收盘穿回该位时移到保本管理。

> **\$niper — "Anticipating Price Delivery | \$GBPCAD Trade Breakdown | ICT Concepts", 6:52 ↗**
>
> 在一个排期驱动事件之前、对尚未形成的高周期 K 线，"仓位放在影线里，而不是实体里"——这是一个视觉启发式，用于驱动事件前仓位入场，区别于标准的对手方 K 线簇要求。

正文：

- 日线 K 线有一个 protraction（延展）阶段，在扩张前形成影线；还有一个扩张阶段，形成实体。
- 最高概率的驱动事件配对，是驱动事件到来时价格仍处在 protraction 阶段——因为日线区间还没扩张，那里的一次操纵应产生单边、无回撤的扩张。
- 仓位入场（positional entry）意味着在驱动事件之前开仓、而不是等确认，它要求驱动事件的开盘紧邻一组成熟、粗壮的对手方 K 线，这样交易才不会被影线扫掉；而且该关键位尚未被扩张离开过。
- 仓位入场还需要留一个可到达的开放目标，例如失败摆动/低阻力流动性，或一个尚未确立的前高/前低，否则预期的行情没有明确去处。
- 对 CPI 或 NFP 这种高成交量驱动事件，前高/前低接近一个有保证的目标，因为在那种成交量下市场不会盘整穿过它们。
