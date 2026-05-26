import streamlit as st
import random
from datetime import datetime
import pandas as pd
import os

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

# 기록 파일 이름
FILE_NAME = "health_history.csv"

# CSV 파일 없으면 생성
if not os.path.exists(FILE_NAME):
    df = pd.DataFrame(columns=["날짜", "추천"])
    df.to_csv(FILE_NAME, index=False)

# 버튼 클릭
if st.button("건강관리 추천 받기"):
    tip = random.choice(health_tips)

    # 현재 날짜시간
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 화면 출력
    st.success("오늘의 건강관리 미션!")
    st.write(tip)

    # 기존 기록 불러오기
    df = pd.read_csv(FILE_NAME)

    # 새 기록 추가
    new_data = pd.DataFrame({
        "날짜": [now],
        "추천": [tip]
    })

    df = pd.concat([df, new_data], ignore_index=True)

    # 저장
    df.to_csv(FILE_NAME, index=False)

# 기록 보기
st.subheader("📋 추천 기록")

history_df = pd.read_csv(FILE_NAME)

if len(history_df) > 0:
    st.dataframe(history_df)
else:
    st.write("아직 기록이 없습니다.")

# 하단 문구
st.caption("매일 하나씩 실천해보세요 😄")
