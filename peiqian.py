import requests
from datetime import datetime

url = "https://sub.maoxiongnet.com/sub?target=clash&new_name=true&url=https%3A%2F%2Fdy.xn--mesx48ahb331x.com%2Fapi%2Fv1%2Fclient%2Fsubscribe%3Ftoken%3D00c1f636b70a0aae239636289ae2d395&insert=false&emoji=true&list=true&tfo=false&scv=false&emoji=false&fdn=false&sort=false&append_type=true"
r = requests.get(url).text
lines = r.splitlines()
output = f"#更新时间 {datetime.now().strftime('%Y/%m/%d %I:%M:%S %p')}\n#来源 {url}\n"

# 替换字段映射
replacement_mapping = {
    "[VMess]": "[CF优选IP]",
    "香蕉": "GateWay",
    "直连-2": "直连-联通",
    "visa国际": "电信",
    "苹果": "One.One",
    "server: www.gov.ua": "server: cf.cloudflare-gateway.com",
    "server: www.csgo.com": "server: peiben.buildtest.site",
    "server: time.cloudflare.com": "server: security.cloudflare-dns.com",
    "server: www.iakeys.com": "server: cf-lt-dns.sharecentre.online",
    "server: jp.supernike.com": "server: peiben.buildtest.site",
    "server: www.visa.com": "server: cf-dx-dns.sharecentre.online",
    "server: usfree7.supernike.com": "server: peiben.buildtest.site",
    "server: sgfree4.supernike.com": "server: peiben.buildtest.site",
    "server: jpfree1.supernike.com": "server: peiben.buildtest.site",
    "server: 192.203.230.228": "server: cf-yd-dns.sharecentre.online",
    # 添加更多的映射关系
}

for line in lines:
    # 对于每个字段映射，逐一进行替换
    for old_str, new_str in replacement_mapping.items():
        line = line.replace(old_str, new_str)
    
    address = line
    output += address + "\n"

with open('peiqian.yaml', 'w') as file:
    file.write(output)
