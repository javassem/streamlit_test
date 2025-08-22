'''
    streamlit 설치
    > pip install streamlit
    > python.exe -m pip install --upgrade pip
    
    streamlit 실행
    > streamlit run 파일명
'''


# ---------------------------------------------------
# <1>
import streamlit as st

from langchain.chat_models import init_chat_model
#from dotenv import load_dotenv
#load_dotenv() # .env  파일을 읽어서 키값 가져옴

# ChatOpenAI 초기화
llm = init_chat_model("gpt-4o-mini", model_provider="openai")
# llm = init_chat_model("gpt-4o-mini", model_provider="openai", temperature=0.1, max_tokens=5 )

# answer = llm.invoke('hello')
# print(answer)

# <2>
#answer = llm.invoke('한국의 날씨는')
#print(answer.content)

st.title('AI 와 대화하기')
my_question = st.text_input('질문을 작성하세요')

# 실행 버튼을 눌렸을 대 실행하도록
# if st.button('요청하세요'):
if my_question:
    answer = llm.invoke(my_question)
    st.write('[ 기본적인 답변 ]')
    st.write(answer)

    # ----------------------------------------------
    # LLM  체인
    # 랭체인에서 체인(chain)은 여러가지 도구나 컴포넌트를 연결하는 개념
    #  - 프롬프트와 답변을 생성하는 LLM을 연결하는 가장 기본적인 모듈

    # 프롬프트 템플릿 생성
    from langchain_core.prompts import ChatPromptTemplate
    prompt = ChatPromptTemplate.from_messages([
        ("system","You are a helpful assistant."),
        ("user","{input}")
    ])
    # LLM 체인 구성
    chain = prompt | llm

    #  내부동작 순서
    #  1- 사용자 입력(input)이 프롬프트 템플릿(prompt)로 전달된다
    #  2- 프롬프트 템플릿의 출력이 GPT 모델(LLM)의 입력으로 전달
    #  3- chain.invoke() 함수를 통해 chain = prompt | llm  체인이 실행된다

    # <3>
    # answer = chain.invoke({'input':'안녕'})
    # print(answer)
    answer2 = chain.invoke({'input':my_question})
    st.write('[ LLM을 통한 답변 ]')
    st.write(answer2)

    # -------------------------------------------------
    # 출력파서 연결 - 모델의 답변만 출력하도록
    # 문자열 출력 파서
    from langchain_core.output_parsers import StrOutputParser
    output_parser = StrOutputParser()

    # LLM 체인 구성
    chain = prompt | llm | output_parser

    # <4>
    # answer = chain.invoke({'input':'안녕'})
    # print(answer)
    answer3 = chain.invoke({'input':my_question})
    st.write('[ 출력파서를 추가한 답변 ]')
    st.write(answer3)