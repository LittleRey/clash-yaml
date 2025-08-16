#!/usr/bin/env python3
# pip install requests pyyaml

import os
import sys
import requests
import yaml

URL = "https://url.v1.mk/sub?target=clash&url=https%3A%2F%2Fyfjc.xyz%2Fapi%2Fv1%2Fclient%2Fsubscribe%3Ftoken%3Dfbf4186e53e1ae4555272a38cfbf5ee6%7Chttps%3A%2F%2Fpqjc.site%2Fapi%2Fv1%2Fclient%2Fsubscribe%3Ftoken%3D530a210abeb730d20b23ce4aa10062da%26flag%3Dmeta&insert=false&config=https%3A%2F%2Fraw.githubusercontent.com%2FLittleRey%2Fclash-yaml%2Fmain%2Fnewname.ini&append_type=true&emoji=true&list=true&udp=true&expand=true&new_name=true&append_type=false&sort=true"


OUTPUT_FILE = "123.yaml"

# 1) 默认 UA，想改就直接改这行
DEFAULT_UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/127.0.0.0 Safari/537.36"
)

# 2) 运行时 export UA="xxx" 即可覆盖上面的默认值
UA = os.getenv("UA", DEFAULT_UA)

HEADERS = {"User-Agent": UA}

def fetch_text(url: str, timeout: int = 10) -> str:
    try:
        resp = requests.get(url, headers=HEADERS, timeout=timeout)
        resp.raise_for_status()
        return resp.text
    except requests.exceptions.RequestException as e:
        # 把异常信息也打出来，方便排查
        print(f"[Error] 抓取失败：{e}", file=sys.stderr)
        sys.exit(1)

def save_yaml(data: dict, file_path: str):
    with open(file_path, "w", encoding="utf-8") as f:
        yaml.dump(
            data,
            f,
            allow_unicode=True,
            default_flow_style=False,
            sort_keys=False,
        )
    print(f"[Info] 已写入 {file_path}")

if __name__ == "__main__":
    text = fetch_text(URL)
    save_yaml({"url": URL, "ua": UA, "body": text}, OUTPUT_FILE)
