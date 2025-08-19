import streamlit as st
import random
from datetime import datetime

# 운세 및 음악 추천 데이터
fortune_music_data = {
    "양자리": {
        "운세": [
            "오늘은 새로운 시작에 적합한 날이에요. 도전을 두려워하지 마세요!",
            "에너지가 넘치는 하루입니다. 활동적으로 움직여 보세요!"
        ],
        "음악": [
            ("Eye of the Tiger - Survivor", "https://www.youtube.com/watch?v=btPJPFnesV4"),
            ("Don't Stop Me Now - Queen", "https://www.youtube.com/watch?v=HgzGwKwLmgM")
        ]
    },
    "황소자리": {
        "운세": [
            "안정과 평화를 추구하는 하루입니다. 느긋하게 하루를 보내세요.",
            "자연 속에서 힐링하는 시간이 필요해요."
        ],
        "음악": [
            ("Banana Pancakes - Jack Johnson", "https://www.youtube.com/watch?v=OkyrIRyrRdY"),
            ("Better Together - Jack Johnson", "https://www.youtube.com/watch?v=u57d4_b_YgI")
        ]
    },
    "쌍둥이자리": {
        "운세": [
            "오늘은 사람들과의 대화에서 좋은 기운이 생겨요.",
            "새로운 정보를 접하게 되는 날이에요!"
        ],
        "음악": [
            ("Happy - Pharrell Williams", "https://www.youtube.com/watch?v=ZbZSe6N_BXs"),
            ("Can't Stop the Feeling! - Justin Timberlake", "https://www.youtube.com/watch?v=ru0K8uYEZWw")
        ]
    },
    # 필요한 별자리 계속 추가 가능
}

st.set_page_config(page_title="오늘의 운세 & 음악 추천", layout="centered")

st.title("🔮 오늘의 운세에 어울리는 음악 추천 🎵")

# 별자리 선택
zodiac = st.selectbox("자신의 별자리를 선택하세요:", list(fortune_music_data.keys()))

if zodiac:
    # 오늘 날짜
    today = datetime.now().strftime("%Y년 %m월 %d일")
    st.markdown(f"### 📅 {today} - {zodiac} 운세")

    # 운세와 음악 랜덤 선택
    fortune = random.choice(fortune_music_data[zodiac]["운세"])
    music_title, music_link = random.choice(fortune_music_data[zodiac]["음악"])

    st.success(f"✨ 운세: {fortune}")
    st.markdown(f"🎧 추천 음악: [{music_title}]({music_link})")
    st.video(music_link)  # 유튜브 영상 임베드

