import requests
from datetime import datetime
import re
import os

# === 配置 ===
SUB_URL = "https://url.v1.mk/sub?target=clash&url=https%3A%2F%2Fyfjc.xyz%2Fapi%2Fv1%2Fclient%2Fsubscribe%3Ftoken%3Dfbf4186e53e1ae4555272a38cfbf5ee6%7Chttps%3A%2F%2Fpqjc.site%2Fapi%2Fv1%2Fclient%2Fsubscribe%3Ftoken%3D530a210abeb730d20b23ce4aa10062da%26flag%3Dmeta&insert=false&config=https%3A%2F%2Fraw.githubusercontent.com%2FLittleRey%2Fclash-yaml%2Fmain%2Fnewname.ini&append_type=true&emoji=true&list=true&udp=true&expand=true&new_name=true&append_type=false&sort=true"
OUTPUT_FILENAME = "cf-ip.yaml"  # Gist 中的目标文件名
GIST_ID = os.getenv("GIST_ID")  # Gist ID 从环境变量读取
GIST_TOKEN = os.getenv("GIST_TOKEN")  # Gist Token 从环境变量读取

# 优选IP域名列表 + 对应的标识
CF_DOMAINS = [
    ("bestcf.030101.xyz", "CF1"),
    ("cdn.2020111.xyz", "CF2"),
    ("bestcf.top", "CF3")
]

# Cloudflare IP匹配（需要替换的）
CF_IP_PATTERN = r"server:\s*(?:\d{1,3}\.){3}\d{1,3}"

# 1. 抓取订阅
resp = requests.get(SUB_URL, timeout=10)
resp.raise_for_status()
text = resp.text

# 2. 筛选 Vless / Vmess 节点
lines = text.splitlines()
filtered_nodes = [line for line in lines if "[Vless]" in line or "[Vmess]" in line]

# 3. 生成不同 CF 域名版本
final_nodes = []
for domain, tag in CF_DOMAINS:
    for node in filtered_nodes:
        # 替换 server IP 为新域名
        node_new = re.sub(CF_IP_PATTERN, f"server: {domain}", node)
        # 修改名称标识（保留原协议标识）
        node_new = re.sub(r"name:\s*\"([^"]*?)\"", r'name: "\2|CF1"', node_new)

        final_nodes.append(node_new)


# 4. 生成最终 YAML 内容
output_content = "#更新时间 {datetime.now().strftime('%Y/%m/%d %I:%M:%S %p')}\n#来源 {SUB_URL}\nproxies:\n" + "\n".join(f"  - {n}" for n in final_nodes)

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


