import requests
import chardet
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
header = {'User-Agent':user_agent}
r = requests.get('http://www.baidu.com',headers=header)
for cookie in r.cookies.keys():
    print('{}: {}'.format(cookie,r.cookies.get(cookie)))