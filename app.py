import streamlit as st
from google import genai

# 페이지 설정
st.set_page_config(
    page_title="연애상담 챗봇",
    page_icon="💖",
)

st.title("💖 연애상담 챗봇")
st.caption("Gemini 2.5 Flash Lite 기반")

# API 키 확인
try:
    api_key = st.secrets["GEMINI_API_KEY"]
except Exception:
    st.error("Secrets에 GEMINI_API_KEY가 설정되지 않았습니다.")
    st.stop()

# Gemini 클라이언트 생성
client = genai.Client(api_key=api_key)

# 채팅 기록 초기화
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": (
                "안녕하세요! 💕\n\n"
                "연애 고민, 썸, 고백, 이별, 인간관계 등 편하게 이야기해 주세요."
            )
        }
    ]

# 기존 대화 출력
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 사용자 입력
prompt = st.chat_input("연애 고민을 입력하세요...")

if prompt:
    # 사용자 메시지 저장
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    try:
        # Gemini에 전달할 대화 구성
        conversation = ""

        for msg in st.session_state.messages:
            role = "사용자" if msg["role"] == "user" else "상담사"
            conversation += f"{role}: {msg['content']}\n"

        system_prompt = """
당신은 친절한 연애상담 전문가입니다.

규칙:
- 공감하며 답변한다.
- 현실적이고 도움이 되는 조언을 제공한다.
- 사용자를 비난하지 않는다.
- 지나친 단정은 피한다.
- 답변은 한국어로 한다.
"""

        full_prompt = f"""
{system_prompt}

다음은 대화 내용이다.

{conversation}

상담사:
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=full_prompt
        )

        answer = response.text

    except Exception as e:
        answer = (
            "⚠️ 오류가 발생했습니다.\n\n"
            f"오류 내용: {str(e)}"
        )

    # 응답 표시
    with st.chat_message("assistant"):
        st.markdown(answer)

    # 기록 저장
    st.session_state.messages.append(
        {"role": "assistant", "content": answer}
    )

# 사이드바
with st.sidebar:
    st.header("설정")

    if st.button("대화 초기화"):
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": (
                    "안녕하세요! 💕\n\n"
                    "연애 고민을 편하게 이야기해 주세요."
                )
            }
        ]
        st.rerun()
