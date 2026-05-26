import streamlit as st
import random
import time

# 페이지 설정
st.set_page_config(
    page_title="브롤스타즈 룰렛",
    page_icon="🎮",
    layout="centered"
)

# CSS 스타일
st.markdown("""
<style>
.stApp {
    background-color: #FFD700;
    text-align: center;
}

/* 제목 */
h1 {
    color: black;
    text-align: center;
    font-size: 50px;
}

/* 설명 */
p {
    color: black;
    font-size: 20px;
}

/* 버튼 */
div.stButton > button {
    background-color: black;
    color: yellow;
    font-size: 24px;
    font-weight: bold;
    border-radius: 15px;
    padding: 12px 30px;
    border: none;
}

/* 룰렛 텍스트 */
.roulette {
    font-size: 60px;
    font-weight: bold;
    margin-top: 40px;
    animation: pop 0.4s ease;
}

/* 희귀도 */
.rarity {
    font-size: 35px;
    font-weight: bold;
    margin-top: 10px;
}

/* 애니메이션 */
@keyframes pop {
    0% {
        transform: scale(0.5);
        opacity: 0;
    }

    50% {
        transform: scale(1.3);
    }

    100% {
        transform: scale(1);
        opacity: 1;
    }
}
</style>
""", unsafe_allow_html=True)

# 브롤러 데이터
brawlers = {

    "희귀": [
        "쉘리", "니타", "콜트", "불",
        "브록", "엘 프리모", "발리",
        "포코", "로사"
    ],

    "초희귀": [
        "제시", "다이너마이크", "틱",
        "8비트", "리코", "대릴",
        "페니", "칼", "재키"
    ],

    "영웅": [
        "비비", "비", "에드거",
        "그리프", "그롬", "보니",
        "개일", "코델리우스"
    ],

    "신화": [
        "모티스", "타라", "진",
        "맥스", "미스터 P", "스퀴크",
        "루", "버즈", "팽"
    ],

    "전설": [
        "스파이크", "크로우",
        "레온", "샌디",
        "앰버", "메그", "체스터"
    ]
}

# 희귀도 색상
rarity_colors = {
    "희귀": "#4CAF50",
    "초희귀": "#2196F3",
    "영웅": "#9C27B0",
    "신화": "#FF5722",
    "전설": "#FFD700"
}

# 제목
st.title("🎮 브롤스타즈 룰렛")

st.write("버튼을 눌러 랜덤 브롤러를 뽑아보세요!")

# 결과 표시 영역
result_area = st.empty()

# 버튼
if st.button("🎲 룰렛 돌리기!"):

    # 룰렛 효과
    for _ in range(20):

        rarity = random.choice(list(brawlers.keys()))
        brawler = random.choice(brawlers[rarity])

        color = rarity_colors[rarity]

        result_area.markdown(
            f"""
            <div class="roulette">
                {brawler}
            </div>

            <div class="rarity" style="color:{color};">
                {rarity}
            </div>
            """,
            unsafe_allow_html=True
        )

        time.sleep(0.08)

    # 최종 선택
    final_rarity = random.choice(list(brawlers.keys()))
    final_brawler = random.choice(brawlers[final_rarity])

    final_color = rarity_colors[final_rarity]

    result_area.markdown(
        f"""
        <div class="roulette">
            🎉 {final_brawler} 🎉
        </div>

        <div class="rarity" style="color:{final_color};">
            ★ {final_rarity} ★
        </div>
        """,
        unsafe_allow_html=True
    )

    st.balloons()
