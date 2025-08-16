import os
import re
import requests
import yaml
from copy import deepcopy

# === 配置 ===
SUB_URL = "https://url.v1.mk/sub?target=clash&url=https%3A%2F%2Fyfjc.xyz%2Fapi%2Fv1%2Fclient%2Fsubscribe%3Ftoken%3Dfbf4186e53e1ae4555272a38cfbf5ee6%7Chttps%3A%2F%2Fpqjc.site%2Fapi%2Fv1%2Fclient%2Fsubscribe%3Ftoken%3D530a210abeb730d20b23ce4aa10062da%26flag%3Dmeta&insert=false&config=https%3A%2F%2Fraw.githubusercontent.com%2FLittleRey%2Fclash-yaml%2Fmain%2Fnewname.ini&append_type=true&emoji=true&list=true&udp=true&expand=true&new_name=true&append_type=false&sort=true"

OUTPUT_FILENAME = os.getenv("OUTPUT_FILENAME", "cf-ip.yaml")
GIST_ID = os.getenv("GIST_ID")
GIST_TOKEN = os.getenv("GIST_TOKEN")

# 生成的三组域名 + 名称标识
CF_DOMAINS = [
    ("bestcf.030101.xyz", "CF1"),
    ("cdn.2020111.xyz", "CF2"),
    ("bestcf.top", "CF3"),
]

# 国旗 Emoji（区域指示符）的正则：两位区域码
FLAG_RE = re.compile(r"^\s*([\U0001F1E6-\U0001F1FF]{2})\s*(.*)$")
# 去掉 [Vless]/[Vmess]
BRACKET_PROTO_RE = re.compile(r"\s*\[(?i:vless|vmess)\]\s*")

def transform_name(name: str, tag: str) -> str:
    """去掉 [Vless]/[Vmess]，在国旗后插入 CFx|，没有国旗就直接前置 CFx|。"""
    base = BRACKET_PROTO_RE.sub("", name).strip()
    m = FLAG_RE.match(base)
    if m:
        flag, rest = m.groups()
        rest = rest.lstrip("|").strip()  # 清理多余竖线/空格
        return f"{flag} {tag}|{rest}" if rest else f"{flag} {tag}"
    else:
        return f"{tag}|{base}" if base else tag

def load_proxies_from_yaml(text: str):
    """优先按 YAML 解析，取 data['proxies']。解析失败则返回空列表。"""
    try:
        data = yaml.safe_load(text)
        if isinstance(data, dict) and "proxies" in data and isinstance(data["proxies"], list):
            return data["proxies"]
        # 有些订阅直接就是列表
        if isinstance(data, list):
            return data
    except Exception:
        pass
    return []

def main():
    # 1) 拉取订阅
    r = requests.get(SUB_URL, timeout=20)
    r.raise_for_status()
    raw_text = r.text

    # 2) 解析 proxies
    proxies = load_proxies_from_yaml(raw_text)

    # 3) 过滤 vless/vmess（更稳：看 type 字段；兜底：看 name 中是否带标签）
    def is_v_proto(p):
        t = str(p.get("type", "")).lower()
        if t in ("vless", "vmess"):
            return True
        nm = str(p.get("name", ""))
        return ("[Vless]" in nm) or ("[Vmess]" in nm)

    filtered = [p for p in proxies if isinstance(p, dict) and is_v_proto(p)]

    # 4) 复制三份 + 改 server + 改 name
    out = []
    for p in filtered:
        orig_name = str(p.get("name", ""))
        for domain, tag in CF_DOMAINS:
            q = deepcopy(p)
            q["server"] = domain
            q["name"] = transform_name(orig_name, tag)
            out.append(q)

    # 5) 组装 YAML
    output_yaml = yaml.safe_dump({"proxies": out}, allow_unicode=True, sort_keys=False)

    # 6) 只更新指定 Gist 文件
    gist_api = f"https://api.github.com/gists/{GIST_ID}"
    resp = requests.patch(
        gist_api,
        headers={
            "Authorization": f"token {GIST_TOKEN}",
            "Accept": "application/vnd.github.v3+json",
        },
        json={"files": {OUTPUT_FILENAME: {"content": output_yaml}}},
        timeout=20,
    )
    resp.raise_for_status()
    print(f"✅ Gist 已更新：{OUTPUT_FILENAME}（共 {len(out)} 个节点）")

if __name__ == "__main__":
    main()
