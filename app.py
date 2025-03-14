import streamlit as st
import pandas as pd
import re

# 초기 비밀번호 입력
password = st.text_input("비밀번호를 입력하세요:", type="password")
if password != "369369":
    st.warning("올바른 비밀번호를 입력하세요!")
    st.stop()

st.title("📌 자동 입력 프로그램")

# 입력 박스 (메모장 역할)
text_input = st.text_area("✍️ 여기에 데이터를 붙여넣으세요")

# 데이터 저장용 리스트
data = {"이름": [], "날짜": [], "시간": [], "가격": []}

# 정규식 패턴
date_pattern = r"\d{4}[-/]\d{2}[-/]\d{2}"  # YYYY-MM-DD 또는 YYYY/MM/DD
time_pattern = r"\d{2}:\d{2}"  # HH:MM
price_pattern = r"[\d,]+원|[\d,]+"  # 10,000원 또는 1,000,000
name_pattern = r"[가-힣]{2,4}"  # 한글 이름 (2~4글자)

# 데이터 추출
if text_input:
    lines = text_input.split("\n")
    for line in lines:
        name_match = re.search(name_pattern, line)
        date_match = re.search(date_pattern, line)
        time_match = re.search(time_pattern, line)
        price_match = re.search(price_pattern, line)

        name = name_match.group(0) if name_match else ""
        date = date_match.group(0) if date_match else ""
        time = time_match.group(0) if time_match else ""
        price = price_match.group(0) if price_match else ""

        if name or date or time or price:
            data["이름"].append(name)
            data["날짜"].append(date)
            data["시간"].append(time)
            data["가격"].append(price)

# 데이터프레임 변환
df = pd.DataFrame(data)

# 결과 표시
st.write("📋 **자동 입력 결과**")
st.dataframe(df)

# 엑셀 저장 기능
if not df.empty:
    import openpyxl  # Excel 저장을 위해 필요

    file_name = "자동입력_결과.xlsx"
    df.to_excel(file_name, index=False, engine="openpyxl")
    st.download_button(label="💾 엑셀로 저장", data=open(file_name, "rb"), file_name=file_name, mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")