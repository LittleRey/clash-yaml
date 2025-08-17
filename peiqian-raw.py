import os
import requests

# ============ 配置 ============
RAW_FILENAME = "test.yaml"   # Gist 中保存的文件名

GIST_ID = os.getenv("GIST_ID")        # Gist ID
GIST_TOKEN = os.getenv("GIST_TOKEN")  # Gist Token
SUB_URL = os.getenv("SUB_URL")        # 订阅 URL
CUSTOM_UA = os.getenv("CUSTOM_UA", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36")  # UA，默认值

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
