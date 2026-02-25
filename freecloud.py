import os
import requests

# ============ 配置 ============
RAW_FILENAME = "freecloud.yaml"   # Gist 中保存的文件名

# 👉 直接写订阅链接
SUB_URL = "https://api.vavv.cn/sub?target=clash&url=https%3A%2F%2Fwww.djjc.cfd%2Fapi%2Fv1%2Fclient%2Fsubscribe%3Ftoken%3Da78bf1d8e049c81b1b3abd34e258c75f&insert=false&config=https%3A%2F%2Fraw.githubusercontent.com%2FLittleRey%2Fclash-yaml%2Fmain%2Fnewname.ini&append_type=true&emoji=true&list=true&udp=true&expand=true&new_name=true&append_type=false&sort=true"
#SUB_URL = "https://api.vavv.cn/sub?target=clash&url=https%3A%2F%2Fgist.githubusercontent.com%2FLittleRey%2Fbd1bde16aa68e9504f1fb81e777a0187%2Fraw%2FshoudongFreeCloud.yaml&insert=false&config=https%3A%2F%2Fraw.githubusercontent.com%2FLittleRey%2Fclash-yaml%2Fmain%2Fnewname.ini&append_type=true&emoji=true&list=true&udp=true&expand=true&new_name=true&append_type=false&sort=true"

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
