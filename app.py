import random
import streamlit as st

st.set_page_config(
    page_title="림버스 컴퍼니 인격 랜덤 선택기",
    page_icon="🎲",
    layout="centered"
)

# 인격 데이터
identities = {
    "이상": [
        "W사 3등급 정리 요원",
        "세븐 협회 6과",
        "검계 살수",
        "로보토미 E.G.O::홍적"
    ],
    "파우스트": [
        "쥐는 자",
        "로보토미 E.G.O::후회",
        "남부 세븐 협회",
        "LCB 수감자"
    ],
    "돈키호테": [
        "중지 작은 아우",
        "W사 정리 요원",
        "남부 시 협회",
        "N사 중간 망치"
    ],
    "료슈": [
        "남부 리우 협회",
        "검계",
        "LCCB 대리",
        "쿠로쿠모 와카슈"
    ],
    "뫼르소": [
        "R사 코뿔소팀",
        "N사 큰 망치",
        "중지 큰형님",
        "장미스패너 공방 대표"
    ],
    "홍루": [
        "흑운회",
        "갈고리 사무소",
        "콩콩이파",
        "남부 디에치 협회"
    ],
    "히스클리프": [
        "토끼팀",
        "시 협회",
        "피쿼드호",
        "멀티크랙 사무소"
    ],
    "이스마엘": [
        "어금니 보트센터",
        "피쿼드호 선원",
        "남부 리우 협회",
        "LCCB 대리"
    ],
    "로쟈": [
        "흑운회 와카슈",
        "장미스패너 공방",
        "남부 디에치 협회",
        "남부 츠바이 협회"
    ],
    "싱클레어": [
        "N사 못 박는 자",
        "마리아치",
        "새벽 사무소",
        "검계"
    ],
    "오티스": [
        "검계",
        "남부 세븐 협회",
        "G사 부장",
        "마탄"
    ],
    "그레고르": [
        "쌍갈고리 해적단",
        "남부 츠바이 협회",
        "장미스패너 공방",
        "G사 일등대리"
    ]
}

st.title("🎲 림버스 컴퍼니 인격 랜덤 선택기")
st.write("원하는 수감자의 인격을 랜덤으로 선택해보자!")

# 수감자 선택
selected_character = st.selectbox(
    "수감자를 선택하세요",
    list(identities.keys())
)

col1, col2 = st.columns(2)

with col1:
    if st.button("선택한 수감자 랜덤 뽑기"):
        result = random.choice(identities[selected_character])

        st.success(f"{selected_character}의 랜덤 인격")
        st.subheader(f"✨ {result}")

with col2:
    if st.button("전체 랜덤 뽑기"):
        random_character = random.choice(list(identities.keys()))
        result = random.choice(identities[random_character])

        st.success("전체 랜덤 결과")
        st.subheader(f"🎯 {random_character} - {result}")

st.divider()

st.caption("※ 인격 데이터는 자유롭게 추가 가능")
