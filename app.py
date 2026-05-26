import streamlit as st
import random

# 제목
st.title("🎲 랜덤 건강관리 추천 앱")

# 건강관리 리스트
health_tips = [
    "💧 물 2L 마시기",
    "🚶‍♂️ 30분 산책하기",
    "🥗 채소 많이 먹기",
    "😴 7시간 이상 자기",
    "🧘 스트레칭 10분 하기",
    "📵 자기 전 휴대폰 멀리하기",
    "🏃 계단 이용하기",
    "🍎 과일 먹기",
    "☀️ 햇빛 15분 쬐기",
    "💪 가벼운 운동하기"
]

# 버튼
if st.button("건강관리 추천 받기"):
    tip = random.choice(health_tips)

    st.success("오늘의 건강관리 미션!")
    st.write(tip)

# 하단 문구
st.caption("매일 하나씩 실천해보세요 😄")
