import re

def extract_mau_urls(file_path):
    """
    从指定的txt文件中提取所有符合"mau": "https://*****/格式的字段
    
    参数:
        file_path: txt文件的路径
    返回:
        匹配到的所有字段列表
    """
    # 定义正则表达式模式
    pattern = r'"mau": "https://.*?/"'
    
    try:
        # 读取文件内容
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # 查找所有匹配的字段
        matches = re.findall(pattern, content)
        
        return matches
    
    except FileNotFoundError:
        print(f"错误: 找不到文件 {file_path}")
        return []
    except Exception as e:
        print(f"处理文件时出错: {str(e)}")
        return []

if __name__ == "__main__":
    # 替换为你的txt文件路径
    txt_file_path = "top-brokers.json"
    
    # 提取符合条件的字段
    mau_urls = extract_mau_urls(txt_file_path)
    
    # 打印结果
    print(f"共找到 {len(mau_urls)} 个匹配项:")
    for url in mau_urls:
        print(url)
    
    # 可选: 将结果保存到新文件
    if mau_urls:
        with open("extracted_mau_urls.txt", 'w', encoding='utf-8') as out_file:
            for url in mau_urls:
                out_file.write(url + '\n')
        print("\n结果已保存到 extracted_mau_urls.txt")
