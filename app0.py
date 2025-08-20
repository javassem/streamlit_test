'''
        >  python.exe -m pip install --upgrade pip
     설치> pip install streamlit

     실행> streamlit run app0.py
'''

import streamlit as st
import pandas as pd
import numpy as np

# 제목
st.title("헬로우 스트림릿")

# 슬라이더
number = st.slider("숫자 선택", 0, 100)
st.write("선택된 숫자:", number)

# 차트 예시 데이터 생성
chart_data = pd.DataFrame( np.random.randn(20,3), columns=['가','나','다'] )

# 라인차트
st.line_chart(chart_data)

