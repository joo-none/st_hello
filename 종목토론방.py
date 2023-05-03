import streamlit as st
import pandas as pd
import numpy as np

import requests
from bs4 import BeautifulSoup



st.title('종목 토론방 분석')

def get_one_page(item_code, page_no):
    url = f"https://finance.naver.com/item/board.naver?code={item_code}&page={page_no}"
    headers = {"user-agent":"Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    table = pd.read_html(response.text)[1]
    cols = ["날짜", "제목", "글쓴이", "조회", "공감", "비공감"]
    table = table[cols]
    temp = table.dropna()
    return temp

item_code = '086520'
page_no = 1
st.dataframe(get_one_page(item_code, page_no))







