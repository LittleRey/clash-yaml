import requests
from datetime import datetime

# 下载目标文件
url = "https://github.com/sooyaaabo/Loon/raw/refs/heads/main/Rule/Media-Proxy.lsr"
r = requests.get(url).text

# 生成头部信息
output = f"# 更新时间 {datetime.now().strftime('%Y/%m/%d %I:%M:%S %p')}\n# 来源 {url}\npayload:\n"

# 统一去除多余空格和多余逗号
r = r.replace('[Rule]', '').replace(' ', '').replace('，', '').replace(', ', ',').replace(',,', ',').replace(',DIRECT', '')
# 关键字段前增加 "   - "，避免多次前缀问题
for keyword in ['DOMAIN,','DOMAIN-SUFFIX,', 'DOMAIN-KEYWORD,', 'IP-CIDR,', 'IP-CIDR6,']:
    r = r.replace(keyword, f'   - {keyword}')

# 拼接处理后的内容
output += r

# 保存结果到指定文件
with open('rules/Media-Proxy.list', 'w') as file:
    file.write(output)

print("✅ 处理完成，结果已保存至 rules/XPTV-Plugin.list")
