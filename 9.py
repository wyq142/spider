import urllib.request
param = urllib.parse.urlencode({'wd':9},encoding='utf8')
url = 'http://www.baidu.com/s?'+param
response=urllib.request.urlopen(url)
HTML = response.read().decode('utf8')
print(HTML)


