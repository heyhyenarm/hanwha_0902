import streamlit as st
import requests

# FastAPI 백엔드 URL
FASTAPI_URL = "http://127.0.0.1:8000"

st.title("FastAPI&Streamlit 연결 테스트")

# 입력 폼 구성
with st.form("user_form"):
    name = st.text_input("이름", value="김땡땡")
    age = st.number_input("나이", min_value=1, max_value=100, value=20)
    submit_button = st.form_submit_button("백엔드로 전송")

if submit_button:
    # FastAPI로 보낼 데이터 페이로드
    payload = {
        "name": name,
        "age": age
    }

    try: 
        # FastAPI / predict 엔드포인트에 POST 요청
        response = requests.post(f"{FASTAPI_URL}/predict", json=payload)

        if response.status_code == 200:
            result = response.json()
            st.success("FastAPI 응답 성공!")
            st.write(f"**결과**: {result['result_message']}")
        else:
            st.error(f"오류 발생 (상태 코드: {response.status_code})")

    except requests.exceptions.ConnectionError:
        st.error("FastAPI 서버에 연결할 수 없습니다. 백엔드 서버의 실행 유무를 확인하세요. ")
