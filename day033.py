import  requests
url='http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02127808'
response = requests.get(url)
HTML=response.text
print(HTML)
response=requests.get(url)
content=response.content
name=url.split('/')[-1]
with open(name,'wb') as f:
    f.write(content)