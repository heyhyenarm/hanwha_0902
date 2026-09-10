import streamlit as st
import requests

# FastAPI 백엔드 URL
FASTAPI_URL = "http://127.0.0.1:8000"

st.title("Chat Bot")

# 채팅 기록 초기화
if "messages" not in st.session_state:
    st.session_state.messages = []

# 앱 재작동 시 기록된 채팅 보여주기
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 유저 입력 반응
if prompt := st.chat_input("say something"):
    # 채팅 박스에 담긴 유저 메시지 보여주기
    st.chat_message("user").markdown(prompt)
    # 유저 메시지 기록에 추가하기
    st.session_state.messages.append({"role": "user", "content": prompt})

    payload = {
        "chatting": prompt
    }
    try:
        # FastAPI / predict 엔드포인트에 POST 요청
        response = requests.post(f"{FASTAPI_URL}/chatbot", json=payload)

        if response.status_code == 200:
            result = response.json()
            st.success("FastAPI 응답 성공")
            # 챗봇 대답 보여주기
            response = f"Echo: {result['result_message']}"
            with st.chat_message("assistant"):
                st.markdown(response)
            # 챗봇 대답 기록에 추가하기
            st.session_state.messages.append({"role": "assistant", "content": response})
        else:
            st.error(f"오류 발생 (상태 코드: {response.status_code})")
    except requests.exceptions.ConnectionError:
        st.error("FastAPI 서버에 연결할 수 없습니다. 백엔드 서버의 실행 유무를 확인하세요. ")