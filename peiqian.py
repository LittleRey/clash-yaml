import requests
from datetime import datetime

url = "https://url.v1.mk/sub?target=clash&url=https%3A%2F%2Fyfjc.xyz%2Fapi%2Fv1%2Fclient%2Fsubscribe%3Ftoken%3Dfbf4186e53e1ae4555272a38cfbf5ee6%7Chttps%3A%2F%2Fpqjc.site%2Fapi%2Fv1%2Fclient%2Fsubscribe%3Ftoken%3D530a210abeb730d20b23ce4aa10062da%26flag%3Dmeta&insert=false&config=https%3A%2F%2Fraw.githubusercontent.com%2FLittleRey%2Fclash-yaml%2Fmain%2Fnewname.ini&append_type=true&emoji=true&list=true&udp=true&expand=true&new_name=true&append_type=false&sort=true"
r = requests.get(url).text
lines = r.splitlines()
output = f"#更新时间 {datetime.now().strftime('%Y/%m/%d %I:%M:%S %p')}\n#来源 {url}\n"

# 替换字段映射
replacement_mapping = {
    r'"[V2ray公益0.1x]Losangeles-CloudFlare", server: dns.cloudflare-gateway.com': r'"[CF优选IP-0.1x]美国洛杉矶-CF_IP-线路", server: 162.159.46.1',
    r'"[V2ray公益0.1x]Losangeles-CloudFlare 2", server: dns.cloudflare-gateway.com': r'"[CF优选IP-0.1x]美国洛杉矶-电信线路", server: cf-dx-dns.sharecentre.online',
    r'"[V2ray公益0.1x]Losangeles-CloudFlare 3", server: dns.cloudflare-gateway.com': r'"[CF优选IP-0.1x]美国洛杉矶-联通线路", server: cf-lt-dns.sharecentre.online',
    r'"[V2ray公益0.1x]Losangeles-CloudFlare 4", server: dns.cloudflare-gateway.com': r'"[CF优选IP-0.1x]美国洛杉矶-移动线路", server: cf-yd-dns.sharecentre.online',
    r'"[V2ray公益0.1x]Losangeles-CloudFlare 5", server: dns.cloudflare-gateway.com': r'"[CF优选IP-0.1x]美国洛杉矶-GateWay", server: cf.cloudflare-gateway.com',
    r'"[V2ray公益0.1x]Losangeles-CloudFlare 6", server: dns.cloudflare-gateway.com': r'"[CF优选IP-0.1x]美国洛杉矶-BuildTest", server: peiben.buildtest.site',
    r'"[V2ray公益0.1x]Losangeles-CloudFlare 7", server: dns.cloudflare-gateway.com': r'"[CF优选IP-0.1x]美国洛杉矶-GateWay", server: peiben.buildtest.site',

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
