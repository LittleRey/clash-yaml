# 👻 Specter 快速上手指南

  ![Specter]([https://specter.dpejoh.com/ghost.svg](https://specter.dpejoh.com/ghost.svg))

  **由 [dpejoh]([https://github.com/dpejoh](https://github.com/dpejoh)) 开发的一体化 Play Integrity 模块**  

  自动处理密钥盒、系统属性、target.txt 以及安全补丁日期

**Specter** 是一体化 Play Integrity 模块，设备首次开机时会自动管理密钥盒（keybox）、设备指纹（系统属性）、`target.txt` 与安全补丁日期。不再需要额外的密钥盒管理器、属性修复模块或是 vbmeta 修复模块 —— Specter 可以包揽全部工作。

> 
> 📄 完整官方文档：[快速入门](https://specter.dpejoh.com/getting-started.html) • [最佳配置指南](https://specter.dpejoh.com/guide/best-setup.html) • [网页控制面板使用指南](https://specter.dpejoh.com/guide/webui.html)

---

## 📦 前置条件

1. 设备已获取 Root，支持 **Magisk**、**KernelSU**、**APatch**
2. **Tricky Store**（[下载地址](https://github.com/5ec1cff/TrickyStore/releases/latest)），也可以使用它的衍生分支：
   - [TEESimulator](https://github.com/JingMatrix/TEESimulator/releases/latest)
   - [TEESimulator‑RS](https://github.com/Enginex0/TEESimulator%E2%80%91RS/releases/latest)> 
   > 💡 **提示：** 如果未检测到对应模块，Specter 会**自动安装 TEESimulator‑RS**
3. **PIF 衍生模块（推荐）**
   - [Play Integrity Fix](https://github.com/KOWX712/PlayIntegrityFix/releases/latest)
   - [Play Integrity Fork](https://github.com/osm0sis/PlayIntegrityFork/releases/latest)

---

## 🛠️ 安装步骤

1. 在 [发布页](https://github.com/dpejoh/specter/releases/latest) 下载 **`Specter‑vX.X.X.zip`**
2. 在 **Magisk / KernelSU / APatch** 中刷入该压缩包
3. **重启设备** —— 首次开机自动执行初始化配置：
   - 备份原始文件
   - 生成 `target.txt`
   - 设置安全补丁日期
   - 部署密钥盒

到此完成。首次重启之后 Specter 会自动完成全部配置工作。

---

## 🔍 后续参考

- [最佳配置指南](specter_best_setup_guide.md) — 推荐模块组合与实现强完整性校验的方法
- [Specter 网页控制面板指南](https://specter.dpejoh.com/guide/webui.html) — 通过网页界面完成全部设置

---

  [🏠 返回主指南](../README.md) |
  [⚙️ Specter 最佳配置](specter_best_setup_guide.md)

> 
> ### 专有名词说明
> 
> 
> - keybox：密钥盒（谷歌设备证明密钥）
> - props：系统属性，文档中保留业务语境意译
> - target.txt：PIF 模块配置文件，文件名原样保留
> - vbmeta：安卓校验分区，保留原名词
> - WebUI：网页控制面板
> - Play Integrity：谷歌播放完整性校验，保留项目原名
> - Flash：刷入（模块刷机术语）

> 
> ⚠️ 免责声明：本文档仅为技术翻译，修改系统完整性校验存在账号风控、应用封禁风险，仅供学习研究使用。
