# 화면과 sqlite 연결

import sqlite3
import streamlit as st
import pandas as pd

# 데이타베이스 연결 ( 파일로 저장됨 )
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# 화면
st.title('사용자 추가')
st.subheader('사용자 정보 입력')
name= st.text_input('이름')
age = st.text_input('나이')

# 데이타 삽입 버튼
if st.button('사용자 추가'):
    if name and age:
        cursor.execute('INSERT INTO users(name,age) VALUES(?,?)',
                       (name, int(age)))
        conn.commit()
        st.success(f'사용자 {name}을 추가하였습니다')
    else:
        st.error('이름과 나이를 정확하게 입력하세요')

# 데이타 조회
st.subheader('사용자 목록보기')
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()
df = pd.DataFrame(rows, columns=['아이디','이름','나이'])
st.dataframe(df)

# 연결 종료
conn.close()
