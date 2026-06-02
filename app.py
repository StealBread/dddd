import streamlit as st
from google import genai

# 페이지 설정
st.set_page_config(
    page_title="게임 챗봇",
    page_icon="🎮",
)

st.title("🎮 게임 챗봇")
st.caption("Gemini 2.5 Flash Lite 기반 게임 상담 챗봇")

# API 키 확인
try:
    api_key = st.secrets["GEMINI_API_KEY"]
except Exception:
    st.error("GEMINI_API_KEY가 Secrets에 설정되지 않았습니다.")
    st.stop()

# Gemini 클라이언트 생성
try:
    client = genai.Client(api_key=api_key)
except Exception as e:
    st.error(f"Gemini 클라이언트 생성 실패: {e}")
    st.stop()

# 채팅 기록 초기화
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "안녕하세요! 🎮 게임 관련 질문을 해보세요. 추천, 공략, 장르 설명 등을 도와드릴게요."
        }
    ]

# 기존 메시지 출력
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 사용자 입력
prompt = st.chat_input("게임에 대해 물어보세요")

if prompt:
    # 사용자 메시지 저장
    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # 대화 기록 생성
    history_text = ""

    for msg in st.session_state.messages:
        role = "사용자" if msg["role"] == "user" else "챗봇"
        history_text += f"{role}: {msg['content']}\n"

    system_prompt = """
당신은 게임 전문 챗봇입니다.

규칙:
- 게임 추천
- 게임 공략 팁
- 장르 설명
- PC, 모바일, 콘솔 게임 정보
- 친절하고 이해하기 쉽게 답변

게임과 무관한 질문도 답변할 수 있습니다.
"""

    full_prompt = f"""
{system_prompt}

대화 기록:
{history_text}

최신 사용자 질문:
{prompt}
"""

    with st.chat_message("assistant"):
        try:
            with st.spinner("답변 생성 중..."):
                response = client.models.generate_content(
                    model="gemini-2.5-flash-lite",
                    contents=full_prompt
                )

                answer = response.text

                st.markdown(answer)

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer
                    }
                )

        except Exception as e:
            error_msg = f"오류가 발생했습니다: {e}"

            st.error(error_msg)

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": error_msg
                }
            )
