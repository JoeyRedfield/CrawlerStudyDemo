import requests
import pandas as pd

url = 'https://api.hahow.in/api/products/search?category=COURSE&filter=PUBLISHED&limit=24&page=0&sort=TRENDING'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11'
}
response = requests.get(url, headers=headers)
if response.status_code == 200:
    data = response.json()
    # print()
    products = data['data']['courseData']['products']
    course_list = []
    for product in products:
        course_data = [
            product['title'],
            product['averageRating'],
            product['price'],
            product['numSoldTickets']
        ]
        course_list.append(course_data)
    df = pd.DataFrame(course_list, columns=['课程名称', '评价', '价格', '购买人数'])
    df.to_excel('hahao.xlsx', index=False, engine='openpyxl')
    print('save')
else:
    print('none')
