import requests
from datetime import datetime

url = "https://sub.maoxiongnet.com/sub?target=clash&new_name=true&url=https://starsea.vip/api/v1/client/subscribe?token=36cc943a57d515c9f378974fed626b42%7Chttps://starsea.vip/api/v1/client/subscribe?token=36cc943a57d515c9f378974fed626b42%7Chttps://starsea.vip/api/v1/client/subscribe?token=36cc943a57d515c9f378974fed626b42%7Chttps://starsea.vip/api/v1/client/subscribe?token=36cc943a57d515c9f378974fed626b42%7Chttps://starsea.vip/api/v1/client/subscribe?token=36cc943a57d515c9f378974fed626b42%7Chttps://starsea.vip/api/v1/client/subscribe?token=36cc943a57d515c9f378974fed626b42&insert=false&emoji=true&list=true&tfo=false&scv=false&emoji=true&fdn=false&sort=false"
r = requests.get(url).text
lines = r.splitlines()
output = f"#更新时间 {datetime.now().strftime('%Y/%m/%d %I:%M:%S %p')}\n#来源 {url}\n"

# 替换字段映射
replacement_mapping = {
    r'"[V2ray公益0.1x]Losangeles-CloudFlare", server: dns.cloudflare-gateway.com': r'"[CF优选IP-0.1x]美国洛杉矶-CF宿云CN-线路", server: cfcn.9sep.org',
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
