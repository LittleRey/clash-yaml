import requests
import re
import os
from datetime import datetime
# === 配置 ===
SUB_URL = "https://url.v1.mk/sub?target=clash&url=https%3A%2F%2Fyfjc.xyz%2Fapi%2Fv1%2Fclient%2Fsubscribe%3Ftoken%3Dfbf4186e53e1ae4555272a38cfbf5ee6%7Chttps%3A%2F%2Fpqjc.site%2Fapi%2Fv1%2Fclient%2Fsubscribe%3Ftoken%3D530a210abeb730d20b23ce4aa10062da%26flag%3Dmeta&insert=false&config=https%3A%2F%2Fraw.githubusercontent.com%2FLittleRey%2Fclash-yaml%2Fmain%2Fnewname.ini&append_type=true&emoji=true&list=true&udp=true&expand=true&new_name=true&append_type=false&sort=true"
OUTPUT_FILENAME = "cf-ip.yaml"
GIST_ID = os.getenv("GIST_ID")
GIST_TOKEN = os.getenv("GIST_TOKEN")

CF_DOMAINS = [
    ("bestcf.030101.xyz", "CF1"),
    ("cdn.2020111.xyz", "CF2"),
    ("bestcf.top", "CF3")
]

# 匹配 server IP
CF_IP_PATTERN = r"server:\s*(?:\d{1,3}\.){3}\d{1,3}"

# 1. 抓取订阅
resp = requests.get(SUB_URL, timeout=10)
resp.raise_for_status()
text = resp.text

# 2. 筛选 Vless / Vmess 节点
lines = text.splitlines()
filtered_nodes = [line for line in lines if "[Vless]" in line or "[Vmess]" in line]

final_nodes = []

for domain, tag in CF_DOMAINS:
    for node in filtered_nodes:
        # 替换 server IP
        node_new = re.sub(CF_IP_PATTERN, f"server: {domain}", node)
        
        # 修改 name 字段
        def replace_name(match):
            name_content = match.group(1)
            # 去掉前面的 [Vless] 或 [Vmess] 并去除多余空格
            name_content = re.sub(r"^\s*(?:\[Vless\]|\[Vmess\])\s*", "", name_content)
            name_content = re.sub(r"\s+", " ", name_content.strip())
            # 加上 CF 标识
            return f'name: "{name_content}|{tag}"'
        
        node_new = re.sub(r'name:\s*"([^"]+)"', replace_name, node_new)
        final_nodes.append(node_new)

# 输出到文件
output_content = "#更新时间 {datetime.now().strftime('%Y/%m/%d %I:%M:%S %p')}\n#来源 {SUB_URL}\nproxies:\n" + "\n".join(f"  - {n}" for n in final_nodes)
with open(OUTPUT_FILENAME, "w", encoding="utf-8") as f:
    f.write(output_content)

# 推送到 Gist
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
