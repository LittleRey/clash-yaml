import os
import requests
from datetime import datetime

# 设置变量
url = "https://github.com/TamTH-Dev/trading-view-scripts/archive/refs/heads/master.zip"
download_dir = "tradebackup"

# 如果保存目录不存在，则创建
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

# 获取当前时间并格式化，作为文件名的一部分
current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
file_name = f"{current_time}_TamTH-Dev.zip"
file_path = os.path.join(download_dir, file_name)

# 下载文件
response = requests.get(url)
if response.status_code == 200:
    with open(file_path, 'wb') as f:
        f.write(response.content)
    print(f"文件成功下载并保存为 {file_path}")
else:
    print("下载失败")
