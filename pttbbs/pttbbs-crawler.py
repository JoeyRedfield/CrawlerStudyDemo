# -*- coding: utf-8 -*-
# @Author  : zhuoyiwu615@gmail.com
# @Time    : 2024/4/6 22:00
# @Desc    : https://www.ptt.cc/bbs/Stock/index.html 前N页帖子数据+推文数据获取 - 同步版本

from typing import List

import requests
from bs4 import BeautifulSoup

import re

from common import NoteContent, NoteContentDetail, NotePushComment

FIRST_N_PAGE = 1  # 前N页的论坛帖子数据
BASE_HOST = "https://www.ptt.cc"

# HEADERS = {
#     "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
# }
HEADERS = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
}

def parse_note_use_bs(html_content: str) -> NoteContent:
    """
    使用BeautifulSoup提取帖子标题、作者、发布日期，基于css选择器提取
    需要注意的时，我们在提取帖子的时候，可能有些帖子状态不正常，会导致没有link之类的数据，所以我们在取值时最好判断一下元素长度
    :param html_content: html源代码内容
    :return:
    """
    soup = BeautifulSoup(html_content, 'lxml')
    
    r_ent = soup.select('#main-container > div.r-list-container.action-bar-margin.bbs-screen > div.r-ent')
    
    for r in r_ent:
        title = r.select('div.title > a')[0].text.strip()
        author = r.select('div.meta > div.author')[0].text.strip()
        date = r.select('div.meta > div.date')[0].text.strip()
        link = r.select('div.title > a')[0]['href'].strip()
    



def get_previos_page_number() -> int:
    """
    打开首页提取上一页的分页Number
    :return:
    """
    uri = '/bbs/Stock/index.html'
    response = requests.get(url=BASE_HOST + uri, headers=HEADERS)

    soup = BeautifulSoup(response.text, "lxml")
    # 拿到实际的分页链接，比如/bbs/Stock/index7120.html
    page_link = soup.select("#action-bar-container > div > div.btn-group.btn-group-paging > a:nth-child(2)")[0]['href'].strip()

    # 拿到数字部分
    numbers = int(re.findall(r'\d+', page_link)[0])

    print(numbers)




def fetch_bbs_note_list(previos_number: int) -> List[NoteContent]:
    """
    获取前N页的帖子列表
    :return:
    """


def fetch_bbs_note_detail(note_content: NoteContent) -> NoteContentDetail:
    """
    获取帖子详情页数据
    :param note_content:
    :return:
    """
    # 获取每一页的帖子列表
    note_list = fetch_bbs_note_detail(get_previos_page_number())

    # 对每一页进行处理


    


def run_crawler(save_notes: List[NoteContentDetail]):
    """
    爬虫主程序
    :param save_notes: 数据保存容器
    :return:
    """
    note_content_list = fetch_bbs_note_list(get_previos_page_number())
    for note_content in note_content_list:
        note_content_detail = fetch_bbs_note_detail(note_content)
        save_notes.append(note_content_detail)
    
    print('爬取完成. ')



if __name__ == '__main__':
    # all_note_content_detail: List[NoteContentDetail] = []
    # run_crawler(all_note_content_detail)
    get_previos_page_number()