# 演练（Walkthrough）

> **来源**：https://nixtrades.com/decision-tree/walkthrough/

这是一个交互式决策树演练工具。每次运行都干净开始——两次检查之间不保存任何状态。

步骤流程标签依次为：止损开关（Kill switches）→ 硬性门槛（Hard gates）→ 路由（Routing）→ 分支（Branch）→ 评分（Scoring）。

首屏第一步：

- **止损开关 K1 · 共 10 步（Kill switch K1 · 1 of 10）**
- 问题：当前 K 线是否为 C4+？
- 选"是"即在此停止——任何一个止损开关被触发都立即判定为不交易。
- 是 / 否

> 说明：本页为交互式单页应用，需在浏览器中逐步作答；其完整判定逻辑与"决策树（Decision Tree）"页一致。静态抓取只能取得上述外壳（首屏问题），后续每一步的具体问题与"是/否"分支需在站点上交互运行。
