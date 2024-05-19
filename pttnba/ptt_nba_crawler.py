import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.ptt.cc/bbs/NBA/index.html'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
# 找到符合条件的网页元素，注意返回的是列表
articles = soup.find_all('div', class_='r-ent')
data_list = []

for a in articles:
    data = {}
    title = a.find('div', class_='title')
    if title and title.a:
        title = title.a.text
    else:
        title = '没有标题'
    popular = a.find('div', class_='nrec')
    if popular and popular.span:
        popular = popular.span.text
    else:
        popular = '没有人气 N/A'

    date = a.find('div', class_='date')
    if date:
        date = date.text
    else:
        date = 'N/A'
    data['标题'] = title
    data['人气'] = popular
    data['日期'] = date
    data_list.append(data)

df = pd.DataFrame(data_list)
df.to_excel('ptt_nba.xlsx', index=False, engine='openpyxl')


# if response.status_code == 200:
#     with open('output.html', 'w', encoding='utf-8') as f:
#         f.write(response.text)
#         print('写入成功')
# else:
#     print('没有抓到网页')
