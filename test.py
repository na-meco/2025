import streamlit as st
import random
from datetime import datetime

# --- 12별자리 운세 및 풍부한 음악 데이터 ---
fortune_music_data = {
    "양자리": {
        "운세": [
            "새로운 시작이 당신을 기다립니다.",
            "도전 정신이 성공을 부르는 하루예요.",
            "오늘은 결단력이 중요한 순간이 될 거예요."
        ],
        "음악": [
            ("Titanium - David Guetta ft. Sia", "https://www.youtube.com/watch?v=JRfuAukYTKg"),
            ("Stronger - Kanye West", "https://www.youtube.com/watch?v=PsO6ZnUZI0g"),
            ("Fight Song - Rachel Platten", "https://www.youtube.com/watch?v=xo1VInw-SKc"),
            ("Born This Way - Lady Gaga", "https://www.youtube.com/watch?v=6JCLY0Rlx6Q"),
            ("Warrior - Demi Lovato", "https://www.youtube.com/watch?v=KVZ-P-ZI6W4"),
            ("Rise - Katy Perry", "https://www.youtube.com/watch?v=lFIIMEe2Ht0")
        ]
    },
    "황소자리": {
        "운세": [
            "마음의 평화를 찾기 좋은 날입니다.",
            "느긋함 속에서 행운이 숨어 있어요.",
            "자연과 가까이하면 에너지가 충전돼요."
        ],
        "음악": [
            ("Better Together - Jack Johnson", "https://www.youtube.com/watch?v=u57d4_b_YgI"),
            ("Banana Pancakes - Jack Johnson", "https://www.youtube.com/watch?v=OkyrIRyrRdY"),
            ("Put Your Records On - Corinne Bailey Rae", "https://www.youtube.com/watch?v=t0eQL5R3GHs"),
            ("Sunday Morning - Maroon 5", "https://www.youtube.com/watch?v=S2Cti12XBw4"),
            ("Slow Dancing in a Burning Room - John Mayer", "https://www.youtube.com/watch?v=32GZ3suxRn4"),
            ("Imagine - John Lennon", "https://www.youtube.com/watch?v=YkgkThdzX-8")
        ]
    },
    "쌍둥이자리": {
        "운세": [
            "다양한 정보가 당신을 찾아오는 날입니다.",
            "소통에서 기회를 발견하게 돼요.",
            "새로운 만남이 즐거움을 줄 거예요."
        ],
        "음악": [
            ("Happy - Pharrell Williams", "https://www.youtube.com/watch?v=ZbZSe6N_BXs"),
            ("Can’t Stop The Feeling! - Justin Timberlake", "https://www.youtube.com/watch?v=ru0K8uYEZWw"),
            ("Good Time - Owl City & Carly Rae Jepsen", "https://www.youtube.com/watch?v=H7HmzwI67ec"),
            ("Electric Love - BORNS", "https://www.youtube.com/watch?v=RYr96YYEaZY"),
            ("Tongue Tied - Grouplove", "https://www.youtube.com/watch?v=1x1wjGKHjBI"),
            ("Valerie - Mark Ronson ft. Amy Winehouse", "https://www.youtube.com/watch?v=4HLY1NTe04M")
        ]
    },
    # ... 생략된 별자리들은 동일한 구조로 계속 작성됩니다 ...
    # 게자리, 사자자리, 처녀자리, 천칭자리, 전갈자리, 사수자리, 염소자리, 물병자리, 물고기자리
}

# --- 나머지 별자리에 대한 데이터도 같은 구조로 추가하세요 ---
# (각 별자리에 운세 3개, 음악 6개 이상 추천)

# --- 앱 시작 ---
st.set_page_config(page_title="오늘의 운세와 음악 추천", layout="centered")
st.title("🔮 오늘의 운세에 어울리는 음악 🎵")

# 별자리 선택
zodiac = st.selectbox("자신의 별자리를 선택하세요:", list(fortune_music_data.keys()))

# 날짜 선택
selected_date = st.date_input("날짜를 선택하세요:", value=datetime.today())

if zodiac and selected_date:
    # 시드 고정으로 날짜 + 별자리에 따라 결과 고정
    seed_key = f"{zodiac}-{selected_date.strftime('%Y-%m-%d')}"
    random.seed(seed_key)

    # 운세 및 음악 선택
    fortune = random.choice(fortune_music_data[zodiac]["운세"])
    music_recommendations = random.sample(fortune_music_data[zodiac]["음악"], k=2)

    # 출력
    st.markdown(f"### 📅 {selected_date.strftime('%Y년 %m월 %d일')} - {zodiac} 운세")
    st.success(f"✨ 오늘의 운세: {fortune}")

    st.markdown("🎵 **오늘 당신을 위한 음악 추천:**")
    for title, link in music_recommendations:
        st.markdown(f"- [{title}]({link})")
        st.video(link)
