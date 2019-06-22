import  requests
URLS1=[]
URLS2=[]
URLS3=[]
url='http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02127808'
response = requests.get(url)
HTML=response.text
print(HTML)
if 'farm1' in url:
    URLS1.append(url)
elif 'farm2' in url:
    URLS2.append(url)
elif 'farm3' in url:
    URLS3.append(url)
response=requests.get(url)
content=response.content
name=url.split('/')[-1]
with open(name,'wb') as f:
    f.write(content)