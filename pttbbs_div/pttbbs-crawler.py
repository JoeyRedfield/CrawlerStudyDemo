import requests
import pandas as pd
from bs4 import BeautifulSoup
from commons import  BriefArticle

url = 'https://www.ptt.cc/bbs/Stock/index.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}


def main():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    articles = soup.select('div.r-ent')
    data_list = []
    for article in articles:
        data_item = {}
        data_item['hot'] = 'N/A' if article.find('div', class_='nrec') is None else article.find('div',
                                                                                                 class_='nrec').text.strip()
        data_item['title'] = 'N/A' if article.find('div', class_='title') is None else article.find('div',
                                                                                                    class_='title').text.strip()
        data_item['author'] = 'N/A' if article.find('div', class_='author') is None else article.find('div',
                                                                                                      class_='author').text.strip()
        data_item['date'] = 'N/A' if article.find('div', class_='date') is None else article.find('div',
                                                                                                  class_='date').text.strip()

        href = article.select_one('div.title a')['href']
        link = f'https://www.ptt.cc{href}'
        data_item['link'] = 'N/A' if href is None else link
        data_list.append(data_item)

    df = pd.DataFrame(data_list)
    df.to_excel('data_list.xlsx', index=False, engine='openpyxl')
    print(data_list)


if __name__ == '__main__':
    main()
