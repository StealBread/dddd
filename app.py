import streamlit as st
import random
import time

# 페이지 설정
st.set_page_config(
    page_title="브롤스타즈 룰렛",
    page_icon="🎮",
    layout="centered"
)

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
        "게일", "코델리우스"
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

# CSS
st.markdown("""
<style>

/* 전체 배경 */
.stApp {
    background: linear-gradient(180deg, #FFD93D 0%, #FFB800 100%);
}

/* 제목 */
.title {
    font-size: 60px;
    font-weight: 900;
    color: black;
    text-align: center;
    text-shadow:
        4px 4px 0px white,
        8px 8px 0px #00000030;
    margin-top: 20px;
}

/* 설명 */
.desc {
    text-align: center;
    color: black;
    font-size: 22px;
    font-weight: bold;
    margin-bottom: 30px;
}

/* 버튼 */
div.stButton > button {
    width: 100%;
    background: linear-gradient(180deg, #00C6FF 0%, #0072FF 100%);
    color: white;
    font-size: 30px;
    font-weight: 900;
    border-radius: 20px;
    border: 4px solid black;
    padding: 15px;
    box-shadow: 0px 8px 0px #003B80;
    transition: 0.1s;
}

/* 버튼 눌림 효과 */
div.stButton > button:active {
    transform: translateY(6px);
    box-shadow: 0px 2px 0px #003B80;
}

/* 카드 */
.result-box {
    background: white;
    border-radius: 30px;
    border: 6px solid black;
    padding: 40px;
    margin-top: 40px;
    text-align: center;
    box-shadow: 0px 10px 0px #00000030;
}

/* 브롤러 이름 */
.brawler-name {
    font-size: 75px;
    font-weight: 900;
    color: black;
    animation: pop 0.4s ease;
}

/* 희귀도 */
.rarity {
    font-size: 40px;
    font-weight: 900;
    margin-top: 10px;
}

/* 룰렛 애니메이션 */
@keyframes pop {
    0% {
        transform: scale(0.5) rotate(-10deg);
        opacity: 0;
    }

    50% {
        transform: scale(1.2) rotate(5deg);
    }

    100% {
        transform: scale(1);
        opacity: 1;
    }
}

/* Streamlit 기본 요소 숨기기 */
#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    visibility: hidden;
}

</style>
""", unsafe_allow_html=True)

# 제목
st.markdown(
    '<div class="title">🎮 브롤스타즈 룰렛</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="desc">버튼을 눌러 랜덤 브롤러를 뽑아보세요!</div>',
    unsafe_allow_html=True
)

# 결과 영역
result = st.empty()

# 버튼
if st.button("🎲 룰렛 돌리기!"):

    # 룰렛 효과
    for _ in range(25):

        rarity = random.choice(list(brawlers.keys()))
        brawler = random.choice(brawlers[rarity])

        color = rarity_colors[rarity]

        result.markdown(
            f"""
            <div class="result-box">
                <div class="brawler-name">
                    {brawler}
                </div>

                <div class="rarity" style="color:{color};">
                    ★ {rarity} ★
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        time.sleep(0.07)

    # 최종 결과
    final_rarity = random.choice(list(brawlers.keys()))
    final_brawler = random.choice(brawlers[final_rarity])

    final_color = rarity_colors[final_rarity]

    result.markdown(
        f"""
        <div class="result-box">

            <div class="brawler-name">
                🎉 {final_brawler} 🎉
            </div>

            <div class="rarity" style="color:{final_color};">
                ★ {final_rarity} ★
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.balloons()
