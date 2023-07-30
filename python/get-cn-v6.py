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

def save_to_file(file_name, content):
    with open(file_name, 'w') as file:
        file.write(content)

if __name__ == "__main__":
    url = "https://ispip.clang.cn/all_cn_ipv6.txt"
    formatted_payload = convert_format(url)

    if formatted_payload:
        save_to_file("CN-V6.txt", formatted_payload)
        print("Successfully saved to 'CN-V6.txt'.")


