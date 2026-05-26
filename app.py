import random
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

st.caption("※ 인격 데이터는 예시이며 자유롭게 추가 가능")
