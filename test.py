from requests import get
from lxml import etree



search_headers = {
		"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
		"Accept-Encoding":"gzip, deflate, br",
		"Accept-Language":"zh-CN,zh;q=0.9",
		"Connection":"keep-alive",
		"Cookie":"BAIDUID=9A6CB8E11486C7B179CB26DDC6F0FC0F:FG=1; BIDUPSID=9A6CB8E11486C7B179CB26DDC6F0FC0F; PSTM=1587069432; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BK_SEARCHLOG=%7B%22key%22%3A%5B%22%E4%BD%A0%E5%A5%BD%22%2C%22505%E9%94%99%E8%AF%AF%22%2C%22505%22%2C%22%E6%88%91%E7%9A%84%E4%B8%96%E7%95%8C%22%2C%22%E6%88%91%E7%9A%84%E4%B8%96%E7%95%8C%E6%9D%90%E8%B4%A8%E5%8C%85%22%2C%22%E6%9D%90%E8%B4%A8%E5%8C%85%22%5D%7D; Hm_lvt_55b574651fcae74b0a9f1cf9c8d7c93a=1589639089,1590815598; Hm_lpvt_55b574651fcae74b0a9f1cf9c8d7c93a=1590816719",
		"Host":"baike.baidu.com",
		"Sec-Fetch-Dest":"document",
		"Sec-Fetch-Mode":"navigate",
		"Sec-Fetch-Site":"none",
		"Sec-Fetch-User":"?1",
		"Upgrade-Insecure-Requests":"1",
		"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.113 Safari/537.36"
}

search_url = "https://baike.baidu.com/search/word?word=newton"
response = get(search_url, headers = search_headers)

with open("./index.html","w") as f:
	f.write(response.text)

html_text = response.text
html = etree.HTML(html_text)
search_result = ""
path = "/html/body/div[@class=\"body-wrapper\"]/div[@class=\"content-wrapper\"]/div[@class=\"content\"]/div[@class=\"main-content\"]/div[@class=\"lemma-summary\"]/div[@class=\"para\"]//text()"


for each in html.xpath(path):
	search_result += each.replace("\"","''").replace("“","''").replace("”","''")

print(search_result)
