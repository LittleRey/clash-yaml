import requests
from datetime import datetime

url = "https://raw.githubusercontent.com/fangkuia/XPTV/refs/heads/main/X/clash.yaml"
r = requests.get(url).text

# 生成头部信息
output = f"# 更新时间 {datetime.now().strftime('%Y/%m/%d %I:%M:%S %p')}\n# 来源 {url}\n"

# 替换文本中的 ',' 为 ', '，并将多余的 ', ,' 替换为 ','
output += r.replace('，', ',').replace(', ', ',').replace(',,', ',')
# 保存结果到文件
with open('rules/XPTV.list', 'w') as file:
    file.write(output)
