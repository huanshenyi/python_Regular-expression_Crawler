import requests
import re
from lxml import etree

def parse_page(url):
   headers={
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
   }
   response = requests.get(url , headers=headers)
   text=response.text

   #xpath方法
   # html=etree.HTML(response.text)
   # title=html.xpath("//div[@class='sons']//div[@class='cont']//a[@target='_blank']/b/text()")
   # print(title)
   #正規表現

   titles = re.findall(r'<div\sclass="cont">.*?<b>(.*?)</b>', text, re.DOTALL)
   dynasties = re.findall(r'<p class="source">.*?<a.*?>(.*?)</a>', text, re.DOTALL)
   authors = re.findall(r'<p class="source">.*?<a.*?>.*?<a.*?>(.*?)</a>', text, re.DOTALL)
   content_tage = re.findall(r'<div class="contson".*?>(.*?)</div>', text, re.DOTALL)
   contents=[]
   for tage in content_tage:
       #print(content.replace('<br />', ''))
       x = re.sub(r'<.*?>', '', tage)
       contents.append(x.strip())

   # lists=[]
   # for a,b,c,d in zip(titles,dynasties,authors,contents):
   #     lists.append({'タイトル':a,'時代':b,'著者':c,'本文':d})

   poems=[]
   for value in zip(titles, dynasties, authors, contents):
       title, dynasty, author, content = value
       poem = {
           'title': title,
           'dynasty': dynasty,
           'author': author,
           'content': content
       }
       poems.append(poem)
   for poem in poems:
        print(poem)
        print("="*40)

def main():
    for x in range(1,5):
        url="https://www.gushiwen.org/default_{key}.aspx".format(key=x)
        parse_page(url)

if __name__ == '__main__':
    main()
