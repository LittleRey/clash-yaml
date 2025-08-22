import requests
import re
import os

# === 配置 ===
SUB_URL = "https://gist.githubusercontent.com/LittleRey/bd1bde16aa68e9504f1fb81e777a0187/raw/test.yaml"
OUTPUT_FILENAME = "cf-ip.yaml"  # Gist 中的目标文件名
GIST_ID = os.getenv("GIST_ID")  # Gist ID 从环境变量读取
GIST_TOKEN = os.getenv("GIST_TOKEN")  # Gist Token 从环境变量读取

# 优选IP域名列表 + 对应的标识
CF_DOMAINS = [
    ("bestcf.030101.xyz", "CF1"),
    ("cdn.2020111.xyz", "CF2"),
    ("bestcf.top", "CF3"),
    ("bestcf.cloudflare.182682.xyz", "CF4"),
    ("xhj.dbm.ddns-ip.net", "CF5"),
    ("fangqi.cloudflare.182682.xyz", "CF6")
]

# Cloudflare IP匹配（需要替换的）
CF_IP_PATTERN = r"server:\s*(?:\d{1,3}\.){3}\d{1,3}"

# 1. 抓取订阅
resp = requests.get(SUB_URL, timeout=10)
resp.raise_for_status()
text = resp.text

# ===== 调试打印 =====
print("=== 原始内容前 10 行 ===")
for i, line in enumerate(text.splitlines()[:10], 1):
    print(f"{i:02d}| {line}")
print("=== 原始内容结束 ===")

# 2. 筛选 Vless / Vmess 节点
lines = text.splitlines()
filtered_nodes = [line for line in lines if "[Vless]" in line or "[Vmess]" in line]

# 3. 打印筛选结果
print("=== 筛选结果 ===")
print("\n".join(filtered_nodes) or "(空)")

# 3. 生成不同 CF 域名版本
final_nodes = []
for domain, tag in CF_DOMAINS:
    for node in filtered_nodes:
        # 替换 server IP 为新域名
        node_new = re.sub(CF_IP_PATTERN, f"server: {domain}", node)
        # 修改名称标识（保留原协议标识）
        node_new = re.sub(r"(\[Vless\]|\[Vmess\])\s*", rf"{tag} ", node_new)
        final_nodes.append(node_new)

# 4. 生成最终 YAML 内容
output_content = "proxies:\n" + "\n".join(f" {n}" for n in final_nodes)

# 5. 推送到 Gist（只更新指定文件）
gist_api_url = f"https://api.github.com/gists/{GIST_ID}"
payload = {
    "files": {
        OUTPUT_FILENAME: {
            "content": output_content
        }
    }
}
r = requests.patch(
    gist_api_url,
    headers={
        "Authorization": f"token {GIST_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    },
    json=payload
)
r.raise_for_status()
print(f"✅ Gist 文件 {OUTPUT_FILENAME} 更新成功")
