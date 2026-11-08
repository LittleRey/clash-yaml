# ⚙️ Specter 最佳配置指南

  ![Specter]([https://specter.dpejoh.com/ghost.svg](https://specter.dpejoh.com/ghost.svg))

  **简洁轻量化配置，实现强完整性校验通过**  

  作者：[dpejoh]([https://github.com/dpejoh](https://github.com/dpejoh))

> 📄 完整官方文档：[最佳配置](https://specter.dpejoh.com/guide/best-setup.html)
---
## 🧩 通用配置（所有 Root 方案均需执行）
**按此顺序**安装下列模块，完成后**重启设备**：

| 序号 | 模块分类 | 可选方案 | 备注 |
| --- | --- | --- | --- |
| 1 | **Zygisk 实现层** | ZygiskNext、ReZygisk | ZygiskNext 稳定性更佳 |
| 2 | **密钥库欺骗模块** | Tricky Store、TEESimulator、TEESimulator‑RS | TEESimulator‑RS 更新维护最活跃 |
| 3 | **Play Integrity 修复** | PlayIntegrityFork、PIF Inject | PIF Inject 维护更新最活跃 |
| 4 | **属性、vbmeta、密钥盒(Keybox)等综合处理** | **Specter** | 自动处理全部相关工作 |
| 5 | **应用隐藏** | HMA‑OSS Zygisk | HMA‑OSS 必需，优先选用，优于 LSPosed |

> 
> ⚠️ **每个分类仅选择一个方案。安装多个同类模块会引发冲突。**

### 🚫 这些模块无需安装 — 直接跳过

- 任意 **vbmeta 修复模块**
- 任意 **密钥盒管理器**（IntegrityBox、Yurikey 等）
- 任意 **系统属性修复模块**
- **Tricky Store Addon** 及其衍生修改版
- **应用自动目标适配类模块**
- **PIF 指纹刷新类模块**

> 
> Specter 已经可以完成以上全部功能，且实现效果更好。它还会**自动检测冲突模块**，并在模块说明中列出。请卸载它标记出来的冲突模块。

### 💡 需要牢记的几点注意事项

- **保持你的配置尽量精简。** 堆叠过多模块，尤其是反复安装卸载、混用不同方案，会留下大量特征指纹，排错难度急剧上升。杂乱的环境无法得到干净的校验结果。
- **如果你的核心诉求是隐藏 Root，请尽量避免自定义ROM。** 很多应用会直接拦截已解锁的 Bootloader；那些声称可以伪装成官方原厂ROM的模块，往往带来比解决的问题更多的麻烦。如果你想查看设备会暴露出多少检测特征，可以使用 Duck Detector 运行 CROM 检测。
- **安装任何模块前，请阅读其 GitHub 上的自述文档（README）。** 大量“模块不工作”的反馈，根源只是某个开关没有打开，而 README 文档花五分钟就能告诉你该如何设置。

---

## 📱 不同 Root 方案专属说明

### Magisk

- 将需要隐藏 Root 的应用添加到**拒绝列表（Denylist）**
- 如果你使用 **ZygiskNext** 或 **ReZygisk**，**不要在 Magisk 设置内开启原生 Zygisk**
- 使用**官方正式版本**，绝大多数衍生分支已经停止维护，没有实质改进

### KernelSU

- 如果你启用了 **SUSFS**，请安装 [BRENE](https://github.com/rrr333nnn333/BRENE) — 该模块会带来显著改善

### APatch

- 有 KPM 模块可用时优先选用 **KPM 模块**
- 安装 **SELinux Hook** 与 **NoHello KPM** 模块

---

## 💪 获取强完整性（Strong integrity）校验通过

安装 Specter 之后，你大概率只能拿到**基础完整性（Basic integrity）**通过。想要达成**强完整性**：

1. **确认你的密钥盒(Keybox)处于有效状态。** 被软封禁的密钥盒，无论其他配置如何，最高只能拿到设备完整性（Device integrity）
2. 打开 **PIF 网页控制面板(PIF WebUI)**，点击 **Fetch（拉取）**，任选一个设备指纹，或者选择 **Random（随机）**，之后点击 **Autopif**
3. 在 **Play商店开发者选项** 中执行完整性检测

> 
> ✅ 如果依旧无法通过强完整性，**再次执行拉取(Fetch)**。大部分用户尝试 2‑3 次即可成功。

⚠️ **警告：** 在自定义ROM上，**不要使用第三方App检测完整性**，有可能会导致设备认证失效。请使用 Play商店本身检测：个人资料 → 设置 → 关于 → 连续点击 Play商店版本号5‑7次 → 通用 → 开发者选项 → Play Integrity → 检查完整性。

---

## 🕵️ HMA‑OSS（应用隐藏）配置

**自动模式（推荐）：**
在 **Specter WebUI** 的第二页，使用 **HMA‑OSS 配置选项**。也可以从网络下载配置文件，通过 **Restore Config（恢复配置）** 按钮导入。

**手动模式：**

1. 开启所有需要**隐藏Root**的应用，以及所有用于执行隐藏工作的组件
2. 创建新模板，设置为**黑名单模式**，自定义模板名称
3. 将 **HMA‑OSS**、**Termux**、以及各类**检测类App**加入不可见列表
4. 将所有需要绕过Root检测的应用加入**应用生效列表**
5. 如果部分应用依旧失败，开启全部预设规则，对这些应用单独套用模板

---

## 🔒 SELinux 修改行为的隐藏方案

你有四种可选方案：

- **APatch 用户：** [SELinux Hook Module](https://github.com/dpejoh/specter)
- **KernelSU 用户：** 使用最新版本自带的 *Hide SELinux modifications（隐藏SELinux修改）* 选项
- **Dirty SELinux Bypass 模块：** [](https://github.com/oMasko/Dirty_Selinux_Bypass)[https://github.com/oMasko/Dirty_Selinux_Bypass](https://github.com/oMasko/Dirty_Selinux_Bypass)
- **IsolPolicy 模块（依赖 LSPosed）：** [](https://github.com/MhmRdd/Isolation-Policy)[https://github.com/MhmRdd/Isolation-Policy](https://github.com/MhmRdd/Isolation-Policy)

---

  [🏠 返回主指南](../README.md) |
  [👻 Specter 快速上手指南](specter_getting_started_guide.md)

> 
> 专有名词说明
> 
> 
> 1. Keybox：密钥盒（谷歌设备证明密钥）
> 2. Bootloader：启动引导程序
> 3. Zygisk：Zygisk（不翻译，行业通用）
> 4. Denylist：拒绝列表
> 5. SELinux：SELinux（安卓安全强制访问控制，保留原名）
> 6. KPM：KernelSU/APatch 的内核模块格式，保留缩写
> 7. WebUI：网页控制面板
> 8. Basic / Device / Strong integrity：基础完整性、设备完整性、强完整性，沿用Play Integrity社区通用中文叫法。

> 
> ⚠️ 免责声明：本内容仅为技术文档翻译，修改系统完整性校验存在账号风控、应用封禁风险，仅作学习研究用途。
