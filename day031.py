import requests
str_ = 'bg{background-image:url(http://s1.bdstatic.com/r/www/cache/static/global/img/icons_5859e57.png);_background-image:url(http://s1.bdstatic.com/r/www/cache/static/global/img/icons_d5b04cc.gif);background-repeat:no-repeat}'
res = str_.split('=')[1]
print(res)
with open(res,'w',encoding='utf8') as f:
    f.write(res.text)