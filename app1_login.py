import  streamlit as st

#----------------------------------
# <0> 초기 로그인화면 
# st.title('로그인')
# id = st.text_input('아이디')
# pw = st.text_input('패스워드', type='password')
# btn = st.button('로그인')

# [참고] '''주석''' 주석이 안됨
# 실행> streamlit run app1_login.py


# # -------------------------------------
# # <1> 로그인 화면
# # 세션 상태 초기화
# if "logged_in" not in st.session_state:
#     st.session_state["logged_in"] = False
#
#
# # 로그인 함수 정의
# # 예로 아이디: user, 패스워드: admin1234
# def login():
#     if id =='user' and pw == 'admin1234':
#         st.session_state["logged_in"] = True
#         st.success("로그인 성공")
#     else:
#         st.error("로그인 실패")
#
# # 로그아웃 함수 정의
# def logout():
#     st.session_state["logged_in"] = False
#     st.info("로그아웃되었습니다")
#
# # 로그인 화면
# if not st.session_state['logged_in']:
#     st.title('로그인')
#     id = st.text_input('아이디')
#     pw = st.text_input('패스워드', type='password')
#     if st.button('로그인'):
#         login()
# else: # 로그인 후 화면
#     st.title('우리 사이트 환영합니다')
#     st.write('로그인 후에만 볼 수 있는 화면입니다')
#     if st.button('로그아웃'):
#         logout()

# [실행결과] user/admin1234 로그인 후 성공한 후에 새로고침이나 다시 로그인 버튼을 클릭해야 화면 전환

