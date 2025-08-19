import streamlit as st
import random
from datetime import datetime

# 12별자리 전체 데이터
fortune_music_data = {
    "양자리": {
        "운세": [
            "새로운 도전이 기회를 가져올 수 있어요.",
            "오늘은 당신의 용기를 시험하는 날입니다.",
            "생각보다 좋은 소식이 들려올 거예요!"
        ],
        "음악": [
            ("Titanium - David Guetta ft. Sia", "https://www.youtube.com/watch?v=JRfuAukYTKg"),
            ("Stronger - Kanye West", "https://www.youtube.com/watch?v=PsO6ZnUZI0g"),
            ("Born This Way - Lady Gaga", "https://www.youtube.com/watch?v=6JCLY0Rlx6Q"),
            ("Warrior - Demi Lovato", "https://www.youtube.com/watch?v=KVZ-P-ZI6W4"),
            ("Rise - Katy Perry", "https://www.youtube.com/watch?v=lFIIMEe2Ht0"),
            ("Don't Stop Me Now - Queen", "https://www.youtube.com/watch?v=HgzGwKwLmgM")
        ]
    },
    "황소자리": {
        "운세": [
            "마음의 평화를 찾게 되는 하루입니다.",
            "작은 기쁨이 큰 만족을 줍니다.",
            "자연과 가까이하면 좋은 기운을 받아요."
        ],
        "음악": [
            ("Better Together - Jack Johnson", "https://www.youtube.com/watch?v=u57d4_b_YgI"),
            ("Sunday Morning - Maroon 5", "https://www.youtube.com/watch?v=S2Cti12XBw4"),
            ("Slow Dancing in a Burning Room - John Mayer", "https://www.youtube.com/watch?v=32GZ3suxRn4"),
            ("Imagine - John Lennon", "https://www.youtube.com/watch?v=YkgkThdzX-8"),
            ("Put Your Records On - Corinne Bailey Rae", "https://www.youtube.com/watch?v=t0eQL5R3GHs"),
            ("Banana Pancakes - Jack Johnson", "https://www.youtube.com/watch?v=OkyrIRyrRdY")
        ]
    },
    "쌍둥이자리": {
        "운세": [
            "새로운 사람들과의 만남이 당신을 자극해요.",
            "오늘은 커뮤니케이션에 날개를 달아보세요!",
            "흥미로운 정보가 행운을 가져옵니다."
        ],
        "음악": [
            ("Happy - Pharrell Williams", "https://www.youtube.com/watch?v=ZbZSe6N_BXs"),
            ("Can't Stop The Feeling! - Justin Timberlake", "https://www.youtube.com/watch?v=ru0K8uYEZWw"),
            ("Valerie - Mark Ronson ft. Amy Winehouse", "https://www.youtube.com/watch?v=4HLY1NTe04M"),
            ("Good Time - Owl City & Carly Rae Jepsen", "https://www.youtube.com/watch?v=H7HmzwI67ec"),
            ("Electric Love - BØRNS", "https://www.youtube.com/watch?v=RYr96YYEaZY"),
            ("Uptown Girl - Billy Joel", "https://www.youtube.com/watch?v=hCuMWrfXG4E")
        ]
    },
    # 나머지 별자리 생략 없이 전부 추가하세요. 아래는 예시로 3개 더 넣음
    "게자리": {
        "운세": [
            "감정이 풍부한 하루입니다. 음악이 위로가 될 거예요.",
            "가족이나 친구와 따뜻한 시간을 보내보세요.",
            "당신의 감성이 빛나는 날이에요."
        ],
        "음악": [
            ("Fix You - Coldplay", "https://www.youtube.com/watch?v=k4V3Mo61fJM"),
            ("Photograph - Ed Sheeran", "https://www.youtube.com/watch?v=nSDgHBxUbVQ"),
            ("Let Her Go - Passenger", "https://www.youtube.com/watch?v=RBumgq5yVrA"),
            ("All of Me - John Legend", "https://www.youtube.com/watch?v=450p7goxZqg"),
            ("Say You Love Me - Jessie Ware", "https://www.youtube.com/watch?v=nxg4C365LbQ"),
            ("Jealous - Labrinth", "https://www.youtube.com/watch?v=50VWOBi0Vfs")
        ]
    },
    "사자자리": {
        "운세": [
            "오늘은 당신의 존재감이 극대화되는 날입니다.",
            "당당한 태도가 매력을 더해줄 거예요.",
            "무대의 중심은 바로 당신입니다."
        ],
        "음악": [
            ("Roar - Katy Perry", "https://www.youtube.com/watch?v=CevxZvSJLk8"),
            ("Can't Hold Us - Macklemore & Ryan Lewis", "https://www.youtube.com/watch?v=2zNSgSzhBfM"),
            ("Break Free - Ariana Grande", "https://www.youtube.com/watch?v=L8eRzOYhLuw"),
            ("Stronger - Kelly Clarkson", "https://www.youtube.com/watch?v=Xn676-fLq7I"),
            ("Power - Little Mix", "https://www.youtube.com/watch?v=QjhbdnAzves"),
            ("Uptown Funk - Bruno Mars", "https://www.youtube.com/watch?v=OPf0YbXqDm0")
        ]
    },
    "처녀자리": {
        "운세": [
            "꼼꼼함이 오늘의 성공을 이끕니다.",
            "작은 계획이 큰 결과를 만들 거예요.",
            "정리와 청소가 생각보다 중요한 의미를 가져요."
        ],
        "음악": [
            ("Shake It Off - Taylor Swift", "https://www.youtube.com/watch?v=nfWlot6h_JM"),
            ("Good as Hell - Lizzo", "https://www.youtube.com/watch?v=SSo3DK0TLQ0"),
            ("Try - Colbie Caillat", "https://www.youtube.com/watch?v=GXoZLPSw8U8"),
            ("Confident - Demi Lovato", "https://www.youtube.com/watch?v=cwLRQn61oUY"),
            ("Love Myself - Hailee Steinfeld", "https://www.youtube.com/watch?v=bMpFmHSgC4Q"),
            ("Pocketful of Sunshine - Natasha Bedingfield", "https://www.youtube.com/watch?v=gte3BoXKwP0")
        ]
    },
    # 나머지 6개 별자리도 같은 형식으로 추가 필요
}

# 앱 기본 설정
st.set_page_config(page_title="오늘의 운세와 음악", layout="centered")
st.title("🔮 오늘의 운세에 어울리는 음악 🎧")

# 사용자 입력
zodiac = st.selectbox("자신의 별자리를 선택하세요:", list(fortune_music_data.keys()))
selected_date = st.date_input("운세를 보고 싶은 날짜를 선택하세요:", value=datetime.today())

if zodiac and selected_date:
    # 날짜 기반으로 seed 생성 (매일 달라짐)
    date_str = selected_date.strftime("%Y-%m-%d")
    seed_str = f"{zodiac}-{date_str}"
    random.seed(seed_str)  # 매일 같은 날짜+별자리면 고정되지만 날짜 바뀌면 결과도 바뀜

    # 운세 선택
    fortune_list = fortune_music_data[zodiac]["운세"]
    today_fortune = random.choice(fortune_list)

    # 음악 추천
    music_list = fortune_music_data[zodiac]["음악"]
    today_music = random.sample(music_list, k=2)

    # 출력
    st.markdown(f"### 📅 {date_str} - {zodiac} 운세")
    st.success(f"✨ 오늘의 운세: {today_fortune}")

    st.markdown("🎵 오늘의 추천 음악:")
    for title, url in today_music:
        st.markdown(f"- [{title}]({url})")
        st.video(url)
