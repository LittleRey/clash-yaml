import requests
from datetime import datetime

url = "https://ispip.clang.cn/all_cn.txt"
r = requests.get(url).text
lines = r.splitlines()
output = f"#更新时间 {datetime.now().strftime('%Y/%m/%d %I:%M:%S %p')}\n#来源 {url}\npayload：\n"


for line in lines:
    address = line
    output += "  - IP-CIDR," + address + ",no-resolve\n"

with open('cn_ipv4.txt', 'w') as file:
    file.write(output)
