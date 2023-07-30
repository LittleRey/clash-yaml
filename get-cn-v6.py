import requests
from datetime import datetime

url = "https://ispip.clang.cn/all_cn_ipv6.txt"
output = f"#更新时间 {datetime.now().strftime('%Y/%m/%d %I:%M:%S %p')}\n#来源 {url}\npayload：\n"

try:
    r = requests.get(url)
    if r.status_code == 200:
        lines = r.text.splitlines()
        for line in lines:
            output += f"  - IP-CIDR6,{line},no-resolve\n"

        with open('cn-ipv6.txt', 'w') as file:
            file.write(output)

        print("文件ip.txt已生成，包含格式化后的IPv6地址列表。")
    else:
        print("无法获取URL内容。")
except requests.exceptions.RequestException as e:
    print("发生错误：", e)


