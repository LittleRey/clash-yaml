import os
import requests

# ============ 配置 ============
RAW_FILENAME = "sub-Peiqian-AIR-RAW.yaml"   # Gist 中保存的文件名

# 👉 直接写订阅链接
SUB_URL = "https://dash.pqjc.site/api/v1/pq/ee04d97589701ed0718111f556f48b7c"

# 👉 Gist 配置（可以直接写死，也可以用环境变量）
GIST_ID = os.getenv("GIST_ID", "你的gist id")
GIST_TOKEN = os.getenv("GIST_TOKEN", "你的gist token")

# 👉 自定义 UA（可改）
CUSTOM_UA = "clash-verge"

# ============ 抓取原始内容 ============
headers = {"User-Agent": CUSTOM_UA}
resp = requests.get(SUB_URL, headers=headers, timeout=15)
resp.raise_for_status()
text = resp.text

print("=== 原始内容前 10 行 ===")
for i, line in enumerate(text.splitlines()[:10], 1):
    print(f"{i:02d}| {line}")
print("=== 原始内容结束 ===")

# ============ 更新到 Gist ============
gist_api_url = f"https://api.github.com/gists/{GIST_ID}"
payload = {
    "files": {
        RAW_FILENAME: {
            "content": text
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

print(f"✅ 原始订阅已保存到 Gist 文件 {RAW_FILENAME}")
