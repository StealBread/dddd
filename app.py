import streamlit as st
import random

# 브롤러 목록
brawlers = [
    "쉘리", "니타", "콜트", "불", "브록",
    "엘 프리모", "발리", "포코", "로사",
    "제시", "다이너마이크", "틱", "8비트",
    "엠즈", "스튜", "파이퍼", "팸", "프랭크",
    "비비", "에드거", "그리프", "모티스",
    "타라", "진", "맥스", "미스터 P",
    "스파이크", "크로우", "레온", "샌디"
]

# 페이지 설정
st.set_page_config(
    page_title="브롤스타즈 랜덤 선택기",
    page_icon="🎮",
    layout="centered"
)

# 배경색 변경 (노란색)
st.markdown("""
<style>
.stApp {
    background-color: #FFD700;
}

h1, p {
    color: black;
    text-align: center;
}

div.stButton > button {
    background-color: black;
    color: yellow;
    font-size: 20px;
    border-radius: 12px;
    padding: 10px 20px;
}
</style>
""", unsafe_allow_html=True)

# 제목
st.title("🎮 브롤스타즈 랜덤 선택기")

st.write("버튼을 눌러 랜덤 브롤러를 뽑아보세요!")

# 버튼
if st.button("🎲 브롤러 뽑기"):
    selected = random.choice(brawlers)

    st.success(f"오늘의 브롤러는 👉 {selected}!")

    st.balloons()
