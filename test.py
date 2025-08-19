import streamlit as st
import random
from datetime import datetime

# 전체 12개 별자리와 그에 따른 운세 및 음악 추천
fortune_music_data = {
    "양자리": {
        "운세": [
            "새로운 도전을 시작하기에 좋은 날입니다.",
            "열정이 넘치는 하루가 될 거예요. 추진력 있게 움직이세요!"
        ],
        "음악": [
            ("Stronger - Kanye West", "https://www.youtube.com/watch?v=PsO6ZnUZI0g"),
            ("Born This Way - Lady Gaga", "https://www.youtube.com/watch?v=6JCLY0Rlx6Q")
        ]
    },
    "황소자리": {
        "운세": [
            "안정과 평화를 즐기세요. 마음의 여유가 중요합니다.",
            "느긋한 태도가 좋은 결과를 가져올 거예요."
        ],
        "음악": [
            ("Gravity - John Mayer", "https://www.youtube.com/watch?v=Fo4746jagH8"),
            ("I'm Yours - Jason Mraz", "https://www.youtube.com/watch?v=EkHTsc9PU2A")
        ]
    },
    "쌍둥이자리": {
        "운세": [
            "소통이 활발한 날입니다. 새로운 정보를 많이 접하게 돼요.",
            "변화에 유연하게 대처하면 좋은 기회가 생길 거예요."
        ],
        "음악": [
            ("Happy - Pharrell Williams", "https://www.youtube.com/watch?v=ZbZSe6N_BXs"),
            ("Can't Stop The Feeling - Justin Timberlake", "https://www.youtube.com/watch?v=ru0K8uYEZWw")
        ]
    },
    "게자리": {
        "운세": [
            "감정이 풍부해지는 날이에요. 주변 사람들과 정서적 유대를 쌓아보세요.",
            "가족이나 친한 사람들과의 시간이 큰 위로가 될 거예요."
        ],
        "음악": [
            ("Fix You - Coldplay", "https://www.youtube.com/watch?v=k4V3Mo61fJM"),
            ("Someone Like You - Adele", "https://www.youtube.com/watch?v=hLQl3WQQoQ0")
        ]
    },
    "사자자리": {
        "운세": [
            "자신감을 가지고 행동하면 주변의 주목을 받을 수 있어요.",
            "당신의 리더십이 필요한 순간입니다!"
        ],
        "음악": [
            ("Roar - Katy Perry", "https://www.youtube.com/watch?v=CevxZvSJLk8"),
            ("Uptown Funk - Bruno Mars", "https://www.youtube.com/watch?v=OPf0YbXqDm0")
        ]
    },
    "처녀자리": {
        "운세": [
            "세부사항에 집중하면 좋은 성과를 낼 수 있어요.",
            "정리정돈과 계획 세우기에 좋은 날입니다."
        ],
        "음악": [
            ("Pocketful of Sunshine - Natasha Bedingfield", "https://www.youtube.com/watch?v=gte3BoXKwP0"),
            ("Shake It Off - Taylor Swift", "https://www.youtube.com/watch?v=nfWlot6h_JM")
        ]
    },
    "천칭자리": {
        "운세": [
            "균형과 조화를 중시해야 하는 날이에요.",
            "타인과의 협력이 중요한 시점입니다."
        ],
        "음악": [
            ("Just the Way You Are - Bruno Mars", "https://www.youtube.com/watch?v=LjhCEhWiKXk"),
            ("Count on Me - Bruno Mars", "https://www.youtube.com/watch?v=ZMsvwwp6SZI")
        ]
    },
    "전갈자리": {
        "운세": [
            "직관을 믿고 움직이세요. 숨겨진 진실이 드러날 수 있어요.",
            "강한 집중력이 당신을 성공으로 이끌 거예요."
        ],
        "음악": [
            ("Believer - Imagine Dragons", "https://www.youtube.com/watch?v=7wtfhZwyrcc"),
            ("Demons - Imagine Dragons", "https://www.youtube.com/watch?v=mWRsgZuwf_8")
        ]
    },
    "사수자리": {
        "운세": [
            "새로운 여행이나 지식에 도전해보세요!",
            "자유롭고 낙천적인 태도가 행운을 가져올 거예요."
        ],
        "음악": [
            ("Adventure of a Lifetime - Coldplay", "https://www.youtube.com/watch?v=QtXby3twMmI"),
            ("On Top of the World - Imagine Dragons", "https://www.youtube.com/watch?v=w5tWYmIOWGk")
        ]
    },
    "염소자리": {
        "운세": [
            "목표를 향해 꾸준히 나아가야 할 날입니다.",
            "책임감 있게 행동하면 좋은 결과가 따를 거예요."
        ],
        "음악": [
            ("Hall of Fame - The Script ft. will.i.am", "https://www.youtube.com/watch?v=mk48xRzuNvA"),
            ("The Climb - Miley Cyrus", "https://www.youtube.com/watch?v=NG2zyeVRcbs")
        ]
    },
    "물병자리": {
        "운세": [
            "독창적인 아이디어가 빛나는 날입니다.",
            "새로운 시도를 두려워하지 마세요!"
        ],
        "음악": [
            ("Electric Feel - MGMT", "https://www.youtube.com/watch?v=MmZexg8sxyk"),
            ("Rather Be - Clean Bandit ft. Jess Glynne", "https://www.youtube.com/watch?v=m-M1AtrxztU")
        ]
    },
    "물고기자리": {
        "운세": [
            "감성적이고 예술적인 에너지가 넘치는 날이에요.",
            "꿈과 상상력을 현실로 옮겨보세요."
        ],
        "음악": [
            ("Dreams - Fleetwood Mac", "https://www.youtube.com/watch?v=mrZRURcb1cM"),
            ("Let Her Go - Passenger", "https://www.youtube.com/watch?v=RBumgq5yVrA")
        ]
    }
}

# Streamlit 앱 시작
st.set_page_config(page_title="오늘의 운세와 음악 추천", layout="centered")
st.title("🔮 오늘의 운세에 어울리는 음악 🎧")

# 별자리 선택
zodiac = st.selectbox("자신의 별자리를 선택하세요:", list(fortune_music_data.keys()))

if zodiac:
    today = datetime.now().strftime("%Y년 %m월 %d일")
    st.markdown(f"### 📅 {today} - {zodiac} 운세")

    # 랜덤 운세 및 음악 추천
    fortune = random.choice(fortune_music_data[zodiac]["운세"])
    music_title, music_link = random.choice(fortune_music_data[zodiac]["음악"])

    st.success(f"✨ 오늘의 운세: {fortune}")
    st.markdown(f"🎵 추천 음악: [{music_title}]({music_link})")
    st.video(music_link)
