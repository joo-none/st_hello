import streamlit as st
import pandas as pd
import numpy as np

import requests
from bs4 import BeautifulSoup



st.title('종목 토론방 분석')

# 한페이지를 수집하는 함수
def get_one_page(item_code, page_no):
    url = f"https://finance.naver.com/item/board.naver?code={item_code}&page={page_no}"
    headers = {"user-agent":"Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    table = pd.read_html(response.text)[1]
    cols = ["날짜", "제목", "글쓴이", "조회", "공감", "비공감"]
    table = table[cols]
    temp = table.dropna()
    return temp

# 여러 페이지를 수집하는 함수
def jongmok_toron(item_code, last_page):
    
    post_list = []
    for page_no in range(1, last_page + 1):

        df = get_one_page(item_code, page_no)
        post_list.append(df)  
        time.sleep(0.001)

    post_list = pd.concat(post_list, ignore_index=True)
    return post_list

# 내용 링크를 수집하는 함수
def jongmok_context(item_code, page_no):
    url = f'https://finance.naver.com/item/board.naver?code={item_code}&page={page_no}'
    headers = {"user-agent":"Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    base_url = 'https://finance.naver.com/'
    sub_url_list = [soup.select('td.title > a')[i]['href'] for i in range(len(soup.select('td.title > a')))]
    context_url_list = [base_url + i for i in sub_url_list]
    return context_url_list


item_code = '086520'
page_no = 1
st.dataframe(jongmok_context(item_code, page_no))







