from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
#from dotenv import load_dotenv
import os
import streamlit as st
import time

#load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

#ChapOpenAI 생성
llm = ChatOpenAI(api_key=api_key, model='gpt-4o-mini')
prompt = ChatPromptTemplate.from_messages([
    ('system' "You are a helpful assistant."),
    ('user', "{input}")
])

# 문자열 출력 파서
output_parser = StrOutputParser()
chain = prompt|llm| output_parser

st.title("_AI시인 :sunglasses:")
content = st.text_input("시의 주제를 입력하세요", "가을")
st.write("시의 주제", content)

if st.button("시 작성"):
    with st.spinner("Wait for it...", show_time=True):
        result = chain.invoke({'input':content+'에 대한 시를 작성 해 줘'})
        st.write(result)