import requests

def convert_format(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to fetch data from the URL.")
        return

    lines = response.text.strip().split('\n')
    payload_lines = ['payload:']
    for line in lines:
        line = line.strip()
        payload_lines.append(f'  - IP-CIDR6,{line},no-resolve')

    return '\n'.join(payload_lines)

if __name__ == "__main__":
    url = "https://ispip.clang.cn/all_cn_ipv6.txt"
    formatted_payload = convert_format(url)
    print(formatted_payload)
