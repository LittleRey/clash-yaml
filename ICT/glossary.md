# 术语表（Glossary）

> **来源**：https://nixtrades.com/glossary/
> **用途**：本表既是交付物，也是全书翻译的统一术语基线——所有章节的术语处理必须与此一致。
> **规则**：英文缩写一律保留原文；首次出现时按需补一个括号中文注释（见下表"中文注释"），之后直接用缩写。

## 术语速查表

| 术语 | 中文注释（首次出现时用） | 说明 |
|---|---|---|
| SMT | Smart Money Technique 背离（智慧资金技术背离） | 相关性破裂的一种 |
| SSMT | Sequential SMT（序列 SMT） | 仅与相邻前一根 K 线比较的 SMT |
| PSP | Precision Swing Point（精准摆动点） | 摆动点 + SMT |
| CiSD | Change in State of Delivery（交付状态改变） | 收盘确认反转/扩张 |
| CiC | Crack in Correlation（相关性破裂） | SMT/SSMT/PSP 的总称信号族 |
| DoL | Draw on Liquidity（流动性抽取目标） | 市场正在交易走向的目标 |
| SS | Strength Switch（强弱切换） | 滞后资产转强 |
| FVG | Fair Value Gap（公允价值缺口） | 三根 K 线失衡区 |
| AMD | Accumulation, Manipulation, Distribution（积累—操纵—派发） | 三阶段日线形态 |
| PoP | Phase of Price（价格阶段） | 盘整/回撤/反转 |
| EQ | Equilibrium（均衡） | 所选 K 线或成交区间的 50% 中点 |
| NWOG | New Week Opening Gap（新周开盘缺口） | 前周收盘与新周开盘之间 |
| NDOG | New Day Opening Gap（新日开盘缺口） | 前日收盘与新日开盘之间 |
| C1/C2/C3/C4 | 第 1/2/3/4 根 K 线（Candle 1/2/3/4） | 反转序列中的 K 线位置 |
| failure swing | 失败摆动（failure swing） | 邻近聚集的高/低点流动性 |
| protected swing | 受保护摆动（protected swing） | 高阻力、预期守住的摆动 |
| driver | 驱动事件（Driver） | 定时、与标的相关的催化剂 |
| killzone | 猎杀区（Killzone，ICT 术语） | 时段过滤器 |
| displacement | 位移（displacement） | 强而果断的单向移动 |
| order pairing | 订单配对（order pairing） | 一侧被操纵形成摆动点的区间 |
| premium/discount | 溢价/折价（premium/discount） | EQ 之上/之下两半 |
| order block | 订单块（order block，ICT 术语） | 位移前最后一根对手方 K 线 |
| breaker | Breaker（失败订单块，ICT 术语） | 破位后反向支撑/阻力区 |
| Propulsion block | 推进块（Propulsion block） | 特定 CiSD，回撤后扩张的入场触发 K 线 |
| IFVG / ICiSD | 反向 FVG / 反向 CiSD（Inverse FVG / Inverse CiSD） | 极性翻转的 PD array |
| IRL / ERL | 区间内流动性 / 区间外流动性（Internal/External Range Liquidity） | 每个设局的两种构件 |
| HTF/LTF | 高周期 / 低周期（Higher/Lower Timeframe） | 周期层级 |
| MTF | 多周期（Multi-Timeframe） | — |
| PD array | 价格交付阵列（Price Delivery array） | 订单块/Breaker/FVG 等价位簇 |
| R:R | 盈亏比（Risk-to-Reward） | — |
| SL / BE | 止损（Stop Loss）/ 保本（Breakeven） | — |
| swing point / swing | 摆动点（swing point） | 结构高点/低点 |
| key level | 关键位（key level） | 高/低点、EQ、缺口、摆动等 |
| turtle-soup | 海龟汤（turtle-soup） | 扫掉最近一个被打破的 HL/LH 形成的止损聚集位 |
| Universal Model | 通用模型（Universal Model） | — |
| double purge | 双重清算（double purge） | 同时打掉买卖双方 |
| seek-and-destroy | 猎杀破坏（seek-and-destroy） | 扩散/展开型盘整形态 |
| narrative | 叙事（narrative） | 价格叙事 |
| expansion / consolidation / retracement / reversal | 扩张 / 盘整 / 回撤 / 反转 | 四种价格阶段 |
| market structure | 市场结构（market structure） | HH/HL、LH/LL 等 |
| swing high / swing low | 摆动高点 / 摆动低点 | 结构极值 |

## 逐条定义（译文）

以下为 glossary 页面逐词条定义的简体中文译文，保留原文关键措辞与框架边界。

### SMT（Smart Money Technique 背离）
SMT 即 "Smart Money Technique divergence"（智慧资金技术背离），是相关性破裂（Crack in Correlation）的一种：正相关的资产没有确认同一个摆动极值——其中一方制造或扫掉了一个高/低点，而另一方没有。在本框架内，SMT 验证关键位上的摆动，并确认已有倾向（bias）；它本身不创造倾向。

### SSMT（Sequential SMT，序列 SMT）
基于时间的相关性破裂：只在所选周期上，将打印出 SMT 的高/低点与紧邻的上一根 K 线的高/低点比较（如前一根 90m、6h、日线或周线 K 线）。不与其更早的 K 线比较。

### PSP（Precision Swing Point，精准摆动点）
摆动点 + SMT。机制上：第 2 根 K 线在两个相关性资产上同时收回到第 1 根 K 线区间内部，但方向相反，从而制造相关性破裂。两级 PSP 等同于两级 SMT。

### CiSD（Change in State of Delivery，交付状态改变）
一种收盘确认：价格通过收盘重新穿回对手方颜色 K 线（或连续若干根对手方 K 线——即把价格送进最近一个摆动的那些 K 线）而改变了交付方向。在本框架内它确认反转/扩张；优先选择带缺口的 V 形、粗壮实体 CiSD。

### CiC（Crack in Correlation，相关性破裂）
笔记中将其定义为一系列信号的总称——"相关性破裂（如 SMT / SSMT / PSP）从关键位验证摆动"——并有一条规则："CiC 确认倾向；它本身不创造倾向。"

### DoL（Draw on Liquidity，流动性抽取目标）
市场正在交易走向的目标。笔记列出的常见形式：日线高/低点、周线 EQ / 前一周 EQ、NWOG/NDOG、HTF 缺口、HTF 摆动高/低点、区间边界 / 区间内部关键位。

### SS（Strength Switch，强弱切换）
明确定义："SS = 滞后资产转强，或领先与滞后资产之间的相对强弱关系发生变化。"被描述为凌驾于所有其他共振（confluence）之上，是资产重新同步的触发。

### FVG（Fair Value Gap，公允价值缺口）
由方向性位移创造的三根 K 线失衡：第 1 根与第 3 根 K 线的影线互不重叠。笔记使用已确认的 FVG 作为抽取目标/关键位，以及回撤或低周期入场参考；缺口在其边界 K 线收盘之前不算确认。

### AMD（Accumulation, Manipulation, Distribution，积累—操纵—派发）
三阶段形态：价格先形成一个区间，然后扫掉一侧并反转穿回区间，再向另一侧的目标扩张。笔记偏好带小日线影线的 AMD 日线形态，并把失败反转/重新扫掠描述为 AMD 反转形态。

### PoP（Phase of Price，价格阶段）
笔记将 PoP 分为盘整、回撤、反转三类，扩张把各阶段连接起来：每个阶段都以扩张开始、以扩张结束。新的 PoP 由摆动形成启动，并以相关性破裂验证。

### EQ（Equilibrium，均衡）
所选 K 线或成交区间的 50% 中点。EQ 以上是溢价（premium）、以下是折价（discount）。笔记按所评估的设局使用整根 K 线 EQ、影线 EQ、日线/周线 EQ 与区间 EQ。

### NWOG（New Week Opening Gap，新周开盘缺口）
前一个交易周收盘与新交易周开盘之间的价格区间。本框架内它是关键位，可充当支撑/阻力，尤其当它与另一个缺口重叠时。

### NDOG（New Day Opening Gap，新日开盘缺口）
前一个交易日收盘与新交易日开盘之间的价格区间。本框架内它与 NWOG 扮演相同的关键位支撑/阻力角色，应用于日线转换处。

### C2/C3/C4 K 线
所选周期上设局的连续 K 线位置。在笔记描述的反转序列中，C1 触及关键位，C2 是下一根 K 线、可能形成反转，C3 是随后的延续机会。如果 C2 已经扩张，不要交易 C3；C4 及更晚不要交易。

### Failure swing（失败摆动）
在同一个小区间内与其他高/低点聚集的邻近高/低点，属于低阻力流动性，通常是一个抽取目标而不是受保护的反转位。扫掉聚集区中的一个高/低点并不会移除该目标——在聚集区内所有相关高/低点都被扫掉之前，该区域始终是目标。本框架内，离开它交易需要 Strength Switch 和缺口/位移。

### Protected swing（受保护摆动）
高阻力摆动：价格操纵一个相关的、有间隔的摆动，并确立一个预期会守住的位——理想情况是该位被缺口标记后缺口已回补并经 CiSD 确认。它与聚集的失败摆动流动性相反。本框架内，没有特殊确认不要直接交易进受保护摆动；不要把尚未完成的"未来缺口"当作保护。

### Driver（驱动事件）
用于为扩张或反转定时的、已排期的、与标的相关的市场催化剂。在笔记中指直接影响品种的红夹新闻（red-folder news），外加指数 9:30 纽约证券交易所开盘。单纯一个钟点时间不是驱动事件；例如 8:30 只有在有相关数据发布排期时才重要。

### Killzone（猎杀区）
ICT 术语：一个反复出现的交易时段窗口，用作集中市场参与时段的时间过滤器，如伦敦或纽约窗口。Killzone 只标识何时寻找设局；它本身不是设局或入场信号。本笔记不采用该术语，因此不设定固定钟点时间。

### Displacement（位移）
脱离区间或摆动、强势而果断的单向移动：价格以有限回撤穿越高/低点，常常留下缺口/FVG。本框架内它是定性层面的扩张或反转确认；笔记不设定固定 K 线大小阈值。

### Order pairing（订单配对）
一种区间：一侧被操纵形成摆动点，价格随后向另一侧派发。本框架内，当另一侧包含失败摆动聚集区时最有利；1h 订单配对区间可充当关键位。

### Premium/discount（溢价/折价）
所选 K 线或成交区间在 EQ（50% 中点）处分为两半：EQ 以上为溢价，以下为折价。本框架内，把它作为带 Strength Switch 确认的情境化回撤/失效过滤器使用，而非机械套用：避免在溢价区做多、在折价区做空。

### Order block（订单块）
ICT 术语：位移之前最后一根对手方颜色 K 线（或连续对手方 K 线），之后作为支撑/阻力参考。笔记反复把 "order block" 作为与 FVG、摆动并列的标准关键位类型之一使用，当作既定 ICT 术语，不展开其自身几何：例如 CiSD 收盘穿回的、价格回撤进入以做延续入场的、或交易时段操纵进去的对象。

### Breaker（Breaker，失败订单块）
ICT 术语：一个失败的订单块——其破位价之后在相反方向被尊重为支撑/阻力区的结构 K 线。笔记只提过一次，与摆动、FVG 或订单块并列，作为大于 1h 意义的"延展/操纵"（protraction/manipulation）关键位示例，未展开其自身结构。

### Propulsion block（推进块）
价格回撤回到一根 K 线区间内、直至第 3 根 K 线开盘（在 30m 或小时线读取）后、在新一轮扩张前即刻形成的特定 CiSD。本框架内它是该回撤的入场触发 K 线。

### IFVG / ICiSD（反向 FVG / 反向 CiSD）
反向 PD array。IFVG 是价格已收盘跌破的多头 FVG（或已收盘升破的空头 FVG），其极性翻转为新方向上的阻力或支撑，而非原始缺口方向。ICiSD 是一个原始 CiSD 位，在被尊重并扩张后，后来被一根对手方 K 线收盘穿回——该位此后被视为"受保护"。本框架内，二者都可作为比等待完整高周期 CiSD 收盘更早的确认。

### IRL / ERL（区间内 / 区间外流动性）
Internal Range Liquidity / External Range Liquidity——每个设局两种构件的缩写：IRL 是失衡/缺口，ERL 是摆动高/低点。IRL → ERL：先回撤进入内部缺口，再扩张到外部摆动流动性（顺势延续）；ERL → IRL：先取外部摆动流动性，再回撤进留下的内部缺口（也是延续）；ERL → ERL：先偏离聚集区的一侧，再交付到对侧（反转——即订单配对区间形态）。
