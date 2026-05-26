import streamlit as st
import random
from datetime import datetime
import pandas as pd
import os

# 파일 이름
HISTORY_FILE = "health_history.csv"
TIPS_FILE = "health_tips.csv"

# 기본 건강관리 리스트
default_tips = [
    "💧 물 2L 마시기",
    "🚶‍♂️ 30분 산책하기",
    "🥗 채소 많이 먹기",
    "😴 7시간 이상 자기",
    "🧘 스트레칭 10분 하기",
]

# 건강관리 파일 없으면 생성
if not os.path.exists(TIPS_FILE):
    tips_df = pd.DataFrame({"건강관리": default_tips})
    tips_df.to_csv(TIPS_FILE, index=False)

# 기록 파일 없으면 생성
if not os.path.exists(HISTORY_FILE):
    history_df = pd.DataFrame(columns=["날짜", "추천"])
    history_df.to_csv(HISTORY_FILE, index=False)

# 제목
st.title("🎲 랜덤 건강관리 추천 앱")

# 건강관리 목록 불러오기
tips_df = pd.read_csv(TIPS_FILE)
health_tips = tips_df["건강관리"].tolist()

# -----------------------------
# 건강관리 추가
# -----------------------------
st.subheader("➕ 건강관리 추가")

new_tip = st.text_input("추가할 건강관리를 입력하세요")

if st.button("건강관리 추가"):
    if new_tip.strip() != "":
        # 중복 체크
        if new_tip not in health_tips:
            new_data = pd.DataFrame({"건강관리": [new_tip]})
            tips_df = pd.concat([tips_df, new_data], ignore_index=True)
            tips_df.to_csv(TIPS_FILE, index=False)

            st.success("건강관리가 추가되었습니다!")
            st.rerun()
        else:
            st.warning("이미 존재하는 건강관리입니다.")
    else:
        st.warning("내용을 입력해주세요.")

# -----------------------------
# 랜덤 추천
# -----------------------------
st.subheader("🎯 랜덤 추천")

if st.button("건강관리 추천 받기"):
    tip = random.choice(health_tips)

    # 현재 날짜시간
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 출력
    st.success("오늘의 건강관리 미션!")
    st.write(tip)

    # 기록 저장
    history_df = pd.read_csv(HISTORY_FILE)

    new_history = pd.DataFrame({
        "날짜": [now],
        "추천": [tip]
    })

    history_df = pd.concat([history_df, new_history], ignore_index=True)
    history_df.to_csv(HISTORY_FILE, index=False)

# -----------------------------
# 기록 보기
# -----------------------------
st.subheader("📋 추천 기록")

history_df = pd.read_csv(HISTORY_FILE)

if len(history_df) > 0:
    st.dataframe(history_df)
else:
    st.write("아직 기록이 없습니다.")

# -----------------------------
# 현재 건강관리 목록
# -----------------------------
st.subheader("📝 현재 건강관리 목록")

for i, tip in enumerate(health_tips, start=1):
    st.write(f"{i}. {tip}")

# 하단 문구
st.caption("매일 하나씩 실천해보세요 😄")
