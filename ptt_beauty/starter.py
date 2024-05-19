import requests
from bs4 import BeautifulSoup
import os

url = 'https://www.ptt.cc/bbs/Beauty/M.1686997472.A.FDA.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'}
cookies = {'over18': '1'}

def download_img(url, save_path):
    print(f'downloading: {url}')
    response = requests.get(url)
    with open(save_path, 'wb') as file:
        file.write(response.content)

def main():
    response = requests.get(url, headers=headers, cookies=cookies)
    soup = BeautifulSoup(response.text, 'html.parser')

    spans = soup.find_all('span', class_='article-meta-value')
    # 可以去看网页, 也可以看print(span)
    title = spans[2].text

    # 1. 建立图片文件夹
    dir_name = f"images/{title}"
    if not os.path.exists(dir_name):
        # 如果存在的话会报错: FileExistsError: [WinError 183] 当文件已存在时，无法创建该文件。: 'images/[正妹] 張景嵐'
        os.makedirs(dir_name)

    # 2. 找到网页中的所有链接,
    links = soup.find_all('a')
    # 需要确认是图片的格式
    allow_file_name = ['jpg', 'png', 'jpeg', 'gif']
    for link in links:
        href = link.get('href')
        extension = href.split('.')[-1].lower()
        file_name = href.split('/')[-1]
        if not href:
            continue
        if extension in allow_file_name:
            # download_img(href, f'{dir_name}/{file_name}')
            # 更新: 实际上现在的href是个图片的跳转, 还需要再做一次解析:
            response = requests.get(href)
            print(f'url: {href}, status_code: {response.status_code}')
            soup_img = BeautifulSoup(response.text, 'html.parser')
            img = soup_img.find_all('img', class_='image-placeholder')
            print(img[0].src)


if __name__ == '__main__':
    main()
