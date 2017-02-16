import urllib.request
import http.cookiejar

URL_ROOT = "http://www.baidu.com"

cookie = http.cookiejar.CookieJar()  # 声明一个CookieJar对象实例来保存cookie
handler = urllib.request.HTTPCookieProcessor(cookie)  # 利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
opener = urllib.request.build_opener(handler)  # 通过handler来构建opener

response = opener.open(URL_ROOT)  # 此处的open方法同urllib2的urlopen方法，也可以传入request

for item in cookie:
    print('Name = ' + item.name)
    print('Value = ' + item.value)