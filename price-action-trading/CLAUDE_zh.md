# CLAUDE.md

本文件为 Claude Code（claude.ai/code）在本仓库中进行代码工作时提供指引。



## XYJTrades PRIMO Model — 交易知识库

资料来自 2 个 PDF：`CIC XYJ.pdf`（59 页）和 `CiC XYJ Time Expansion YT2.pdf`（40 页）
是 **Lathyrus Trading / @XYJTrades** 的交易系统 — 基于 ICT 的 Smart Money 方法论

---

### 核心理念

- **Expansion** 之前必先有 **Swing Formation**
- **Swing Formations** = Market Maker Models（MMXMs）
- MMXMs 在 ERL↔IRL 之间分配流动性 — 这就是 **The Universal Model**
- **每个 Swing** 都伴随 **Cracks in Correlation（CiC）** 形成
- 资产同步 → 可以 expansion；资产不同步 → 处于操控阶段

---

### 术语表

| 术语 | 含义 |
|------|-----------|
| **CiC** | Crack in Correlation — 关联资产走势分叉的位置 |
| **SMT** | Smart Money Technique — 一个资产做假 HH/LL 而另一个不确认 |
| **PSP** | Precision Swing Point — 发出反转信号的 K 线形态 |
| **ERL** | External Range Liquidity（摆动高/低点） |
| **IRL** | Internal Range Liquidity（区间内 FVG、imbalance） |
| **SS** | Strength Switch — 资产角色由弱转强的位置 |
| **P/D** | Premium / Discount zone |
| **FTM** | Failure To Manipulate — 未能抽走流动性的资产 → 领先信号 |
| **2S CiC** | 2-Stage CiC — 本系统核心形态，由 C1→C2→C3 组成 |
| **MMXM** | Market Maker Model |
| **CC SMT** | Correlated Currency SMT |

---

### CiC 算法（3 根 K 线）

```
CiC 1  =  CC SMT      ← 第一根，correlation break 开始
CiC 2  =  PSP         ← Precision Swing Point，确认 manipulation
CiC 3  =  2-Stage SMT ← 确认 K 线，入场点
```

**入场规则：** 在 2-Stage CiC 确认后，于 C3 入场

---

### 4 步同步反转序列（Type 1 反转 — In-Sync）

```
Step 1: Triad（3 个关联资产）一起触及 Universal Model 中的关键位（ERL/IRL）
Step 2: 在该关键位形成 2-Stage CiC → 构建 C2/C3 Swing Formation
Step 3: 做出 SMT（假 HH 或假 LL）的资产 → 操控后 Strength Switch
Step 4: 3 个资产同步反转 + expansion
```

---

### Universal Model 变体

| 变体 | 方向 |
|---------|-----------|
| IRL → ERL | 向上 Expansion → 回调 → 再向上 Expansion |
| ERL → IRL | 向下 Expansion → 回调 |

---

### 资产同步 — Triad 中的 3 个角色

| 角色 | 行为 |
|------|-----------|
| **Leading Asset** | 在 Middle 资产 SMT break / 盘整后率先反转 → 新 PoP |
| **Middle Asset** | 触发 SMT break + Strength Switch（SS-PSP trigger） |
| **Lagging Asset** | 守住 P/D 区间后跟随 expansion |

---

### 2-Stage CiC 变体

1. **2S PSP — PSP 确认 SMT** → 交易 C3
2. **2S PSP — SMT 确认 PSP** → 交易 C2/C3
3. **带 Swing 的 2S CiC** → PSP + Swing formation，交易 C3

---

### Algorithm 1 — 同步反转（Type 1）

**入场序列：**
1. SMT 形成（CiC 1 — CC SMT）
2. PSP 收线（CiC 2）
3. 2S CiC 确认后在 C3 入场

**时间框架：** HTF（H4/日线）定关键位 → LTF（M15/M1）入场

**示例：**
- ES | H4 | 2S PSP → Lagging asset draw 流动性
- NQ | H4 | 未能操控 Internal Low → 10AM Continuation Logic
- YM/ES/NQ Triad — 典型关联资产组合

---

### Algorithm 2 — 异步反转（Type 2）

**要点：**
- 用 **Decoupled Triad Expansions + Failure To Manipulate [C2]** 过滤
  - 走出 FTM 的资产 → 用 Algorithm 1 的 SMT Break Logic 交易
- **Failure To Manipulate + P/D Ranges**
  - Leading Asset 用 SMT 操控 → 用 Type 1 反转逻辑交易

**触发：** 6:00 AM YM 与 ES/NQ Decoupled → 10:00 AM FTM → 2 Stage CiC → 重新同步进入 SMT Break

---

### Strength Switch（SS）— 核心信号

- 发生在 **Middle Asset** 上：SMT 向下 break 时，Lagging Asset 触及前一根 H4 K 线高点
- Lagging Asset 守住 P/D 后 expansion
- Leading Asset 盘整/回调 → 新 Point of Price（PoP）
- **SS-PSP** = 作为 Precision Swing Point 出现的 Strength Switch → 入场触发

---

### Coupled vs Decoupled Expansion

| 类型 | 特征 |
|------|--------|
| **Coupled Expansion** | 3 个资产同步 expansion = In-Sync |
| **Decoupled Expansion** | 资产 expansion 不同步 = 操控阶段 / 异步 |

---

### 时间窗口（重要）

- **6:00 AM** = SMT / PSP 确认窗口（H4 6AM 反转）
- **10:00 AM** = C3 Continuation / FTM trigger
- **Daily ERL→ERL** = 总体流动性 draw

---

### 1-Stage CiC 变体（详解）

| 变体 | 特征 |
|---------|--------|
| **PSP** | 小的 inside/overlapping K 线 — Precision Swing Point |
| **SMT Fill** | Gap/FVG 创建后立刻被回补 |
| **Consecutive Candles** | 同方向连续 2 根 K 线 |
| **With Swings** | PSP + Swing formation（多根 K 线） |

---

### 已确认的资产 Triad

| 市场 | 资产 |
|--------|--------|
| **股指期货** | NQ / YM / ES |
| **黄金** | GC / GBPUSD / GBPEUR |
| **原油** | HO / RB / CL |

---

### C3 vs C2 交易偏好（入场时机过滤）

**C3 反转 — 优先使用场景：**
- C2 在收线前未能反转（因时间或操控深度）
- C3 开盘时 C2 正处于关键位
- C3 机械性反转并 expansion
→ **交易偏好：C3 Expansion**

**C2 反转 Expansion — 使用场景：**
- **小影线**（价格过滤）+ **K 线剩余时间充足**（时间过滤）
→ C2 Reversal Expansion **>** C3

**回到 C3 的条件：**
- **大影线** + **剩余时间有限**
→ C3 Expansion **>** C2 Reversal

---

### Swing 失效判定

| 交易这个 | 而不是这个 |
|-----------|---------|
| 反转（产生 FVGs） | Failure To Manipulate — 盘整不产生 FVGs |

---

### 第 4 章 — 高概率 Continuation 序列

利用 CiC 构建高概率 continuation 摆动：
- **HTF：** 2-Stage CiC
- **LTF：** 同步 K 线
- 类型：Type 1 @ 日线（1 次 swap）、Type 1 @ H4（1 次 swap）、Type 1 @ H4（双向 swap）
- **C3 的 HTF Continuation 特征** — 寻找 HTF K 线 continuation 形态

---

### 第 5 章 — Continuation 的资产同步

- 同样的 3 资产 triad 逻辑既适用于反转，也适用于 continuation
- Middle asset SMT break → 触发 lagging asset 启动
- **理想入场：** SMT PSP + SS 形态（从 Gap Near IQ 延续）
- SS Confirms Reversal 序列在此同样适用

---

### 第 6 章 — Gap 选择 | Range 理论（入场过滤）

**过滤 1：当前 K 线 P/D**
```
C3 在 Discount zone 开盘 → 入场 → 安全止损（K 线低点下方）
C3 在 Premium zone 开盘 → 危险止损（K 线高点上方）
```

**过滤 2：Implied Dealing Ranges**
```
当前 HTF Range 成立 ✓ → 有效入场
需要新 Range           → 先要有 ITM Swing Formation
```

**Gap 有效性：**
- 有效 Gap：由 impulse move 产生的 LTF FVG（反转特征）
- 无效 Gap：盘整产生的 gap（无 FVG = fail to manipulate）
- Bearish Gap vs Bullish Gap — 方向必须与 bias 一致

**要点（第 6 章）：**
- 在 Implied Dealing Range 的 50% 以下入场 FVG = 更 discounted = 更高概率
- 价格必须相对于 Dealing Range 序列在 FVG 上 discounted 入场
- 在靠近当前 HTF range 的 FVG 入场 → 避免需要新 range

---

### 第 7 章 — APD 序列（高级 Premium/Discount）

**目的：** 用 Premium/Discount 概念判断 SMT 是否成立

**Leading Asset 动态：**
- 遵循 ERL→ERL 模型：Expansion → 回调 → Expansion
- P zone = 谨慎 / D zone = 有效入场区

**Lagging Asset 动态：**
- Expansion → 回调（守住 P/D）→ Expansion
- APD 序列：从 Gap Near IQ 延续 + SS Confirms Reversal

---

### Strength Switch 验证（完整规则）

**有效 SMT** = 操控资产短暂反转最强资产

- **Case 1：** 资产做出 **higher high** → 带相对强度反转向下
- **Case 2：** 资产做出 **lower low** → 带相对强度反转向上

**SS 可通过以下方式观察：**
1. 出现 PSP → **SS-PSP**
2. 出现更大 Displacement → **Fair Value Gap（FVG）**
3. 更快反转 → **CISD**（Change in State of Delivery）

---

### 反转特征（什么是反转、什么不是）

```
反转       = 带 FVGs 的 V 形，果断的方向改变
回调       ≠ 反转（不是一回事）
盘整       ≠ 反转（不是一回事，不产生 FVGs）
```

---

### Indicator 开发计划（目标）

老板希望基于这套逻辑做一个 indicator — 平台尚未最终决定
**PDF 状态：** 已读完全部 99 页（CIC XYJ.pdf 59 页 + Time Expansion 40 页）
**候选平台：** TradingView Pine Script v5 / MT5 / Python
**Indicator 状态：** 已写在 `NEO_XYJ_CiC.pine`（Pine Script v5，220 行）— 覆盖 SMT、PSP、2S CiC State Machine、FVG、Session Filter、Dashboard、Alerts

---

## Vertex Match & Gann Square of 9 — 交易知识库

老板对 K 线计数 + 数字学（numerology）应用于寻找反转区间的技术感兴趣。

---

### Vertex Match 是什么

使用 **Digital Root**（不断相加直到得到单位数）配合：
1. **Bar Count** — 从 High/Low 数 K 线然后求 DR → 如果 DR 与之前某根 bar 相同 = "Vertex Match"
2. **Price** — 把价格的各位数字相加直到单位数 → 与时间 DR 求 confluence

**关键数字集合：** `1, 3, 5, 7, 9, 13, 17, 21, 25, 31, 32, 36`

该集合的 Digital Root：

| Bar | DR | Bar | DR |
|-----|----|-----|----|
| 1 | 1 | 13 | 4 |
| 3 | 3 | 17 | 8 |
| 5 | 5 | 21 | 3 |
| 7 | 7 | 25 | **7** ← 匹配 bar 7 |
| 9 | 9 | 31 | **4** ← 匹配 bar 13 |
| | | 32 | **5** ← 匹配 bar 5 |
| | | 36 | **9** ← 匹配 bar 9 |

---

### Gann Square of 9 — 结构

数字从中心螺旋展开 — 同一 spoke 上的数字 = "相同 vibration" = 互为 S/R。

**Cardinal Cross：** 0°=1,9,25,49 / 90°=3,11,27 / 180°=5,13,29 / 270°=7,15,31
**Diagonal Cross：** 45°=2,10,26 / 135°=4,12,28 / 225°=6,14,30 / 315°=8,16,32

### 价格位公式（Square of 9）

```
next_level = (√price ± n × 0.5)²
n = 1（90°）, 2（180°）, 3（270°）, 4（360°）

示例：Gold 3547（√3547 = 59.556）：
  90°  上  = 3,606.7  |  90°  下 = 3,487.6
  180° 上  = 3,667.0  |  180° 下 = 3,428.8
  270° 上  = 3,727.8  |  270° 下 = 3,370.5
  360° 上  = 3,789.1
```

### Price-Time Squaring

```
价格的角度位置 = fractional(√price) × 360°
bar 的角度位置 = fractional(√bar)   × 360°
→ 如果两个角度接近 = "Price Squares Time" = 反转概率高
```

### 3 层 Confluence 框架

```
Layer 1（时间）— bar count 到达 Vertex Match 集合中的关键数字
Layer 2（价格）— 价格靠近 Square of 9 位（90°/180°/270°）
Layer 3（DR）  — Digital Root(price) = Digital Root(bar) = "Squared"

最强信号 = 3 层全部命中 + Price Action 确认（PSP/SMT）
```

### 毕达哥拉斯数字组

```
Group A: 1, 4, 7 （三角）
Group B: 2, 5, 8
Group C: 3, 6, 9  ← Tesla："宇宙的秘密"
```
DR 相同 = vibration 相同 = 行为模式倾向相似。

### 学习进度

- [x] Vertex Match + Digital Root — 已理解
- [x] Gann Square of 9 价格位 — 已理解
- [x] Price-Time Squaring — 已理解
- [ ] Gann Wheel of 24（astro cycles）— 尚未深入
- [ ] Master Numbers 11, 22, 33（毕达哥拉斯）— 尚未深入
- [ ] "Morpheus" 的 Time Dilation Theory — **暂无资料**，等老板发 source

---

## 需保留的约定

- 除非用户明确要求拆分，否则所有内容放在 `index.html` 里 — 单文件布局是本原型的刻意设计。
- 内联 `onclick="fn(...)"` 处理器是既定模式；不要零散地重构为 `addEventListener`。
- UI 中的泰语字符串是唯一事实来源 — 修改相邻代码时不要把它们翻译成英文。
- CSS 使用非常短的 class 名（`.tb`、`.rc`、`.mitem`、`.pg`、`.apg` 等）和定义在 `:root` 中的 CSS 变量。复用已有 token（`--g`、`--bg`、`--sh1`……），不要引入新的 hex 值。
