import urllib.request
url = 'http://httpbin.org/get?wd=呵呵'
headers = {
    'BAIDUID=6202FDC88E6E23EAD970789B1CBCAD81':'FG=1; BIDUPSID=6202FDC88E6E23EAD970789B1CBCAD81; PSTM=1560999686; H_PS_PSSID=29326_1422_21126_29135_29238_29098_29131_29368_28831_29220; BD_UPN=12314753; H_PS_645EC=c6d7db75EeFHNLrBM76X3Q6BzFfYdt2bsTF0cO1wTRSkDVjdnIgmrCay0E0; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; BD_CK_SAM=1; PSINO=1; BDSVRTM=102'
}
proxy_handle={
    'http':'http://163.204.240.162:9999'
    'http':'http://183.51.190.51:33913'
    'http':'http://119.191.79.46:80'
    'http':'http://122.193.245.44:9999'
}
proxy = urllib.request.ProxyHandler(proxy_handle)
opener = urllib.request.build_opener(proxy)
response = opener.open(url)
print(urllib.request)
for url in urls:
    response=urllib.request.urlopen(url)
    if response.status!=200:
        print('继续爬')
    else:
        print('错误')