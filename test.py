import streamlit as st
import random
from datetime import datetime

# 12별자리 운세와 풍부한 음악 데이터
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
            ("Electric Love - BØRNS", "https://www.youtube.com/watch?v=RYr96YYEaZY"),
            ("Tongue Tied - Grouplove", "https://www.youtube.com/watch?v=1x1wjGKHjBI"),
            ("Valerie - Mark Ronson ft. Amy Winehouse", "https://www.youtube.com/watch?v=4HLY1NTe04M")
        ]
    },
    "게자리": {
        "운세": [
            "감정에 솔직해지는 하루가 될 거예요.",
            "소중한 사람과 대화를 나누면 마음이 가벼워져요.",
            "과거의 추억이 현재를 비춰주는 날입니다."
        ],
        "음악": [
            ("Fix You - Coldplay", "https://www.youtube.com/watch?v=k4V3Mo61fJM"),
            ("Someone Like You - Adele", "https://www.youtube.com/watch?v=hLQl3WQQoQ0"),
            ("Photograph - Ed Sheeran", "https://www.youtube.com/watch?v=nSDgHBxUbVQ"),
            ("All of Me - John Legend", "https://www.youtube.com/watch?v=450p7goxZqg"),
            ("Let Her Go - Passenger", "https://www.youtube.com/watch?v=RBumgq5yVrA"),
            ("Say You Love Me - Jessie Ware", "https://www.youtube.com/watch?v=nxg4C365LbQ")
        ]
    },
    "사자자리": {
        "운세": [
            "당신의 에너지가 모두를 사로잡는 날입니다.",
            "자신감을 가지고 행동해 보세요!",
            "당신의 리더십이 빛을 발할 거예요."
        ],
        "음악": [
            ("Roar - Katy Perry", "https://www.youtube.com/watch?v=CevxZvSJLk8"),
            ("Uptown Funk - Bruno Mars", "https://www.youtube.com/watch?v=OPf0YbXqDm0"),
            ("Can't Hold Us - Macklemore & Ryan Lewis", "https://www.youtube.com/watch?v=2zNSgSzhBfM"),
            ("Stronger (What Doesn’t Kill You) - Kelly Clarkson", "https://www.youtube.com/watch?v=Xn676-fLq7I"),
            ("Break Free - Ariana Grande", "https://www.youtube.com/watch?v=L8eRzOYhLuw"),
            ("Power - Little Mix", "https://www.youtube.com/watch?v=QjhbdnAzves")
        ]
    },
    "처녀자리": {
        "운세": [
            "계획을 세우고 실천하기 좋은 날입니다.",
            "세부적인 부분에 집중하면 성공할 수 있어요.",
            "정리정돈이 당신의 머리를 맑게 해줄 거예요."
        ],
        "음악": [
            ("Shake It Off - Taylor Swift", "https://www.youtube.com/watch?v=nfWlot6h_JM"),
            ("Pocketful of Sunshine - Natasha Bedingfield", "https://www.youtube.com/watch?v=gte3BoXKwP0"),
            ("Love Myself - Hailee Steinfeld", "https://www.youtube.com/watch?v=bMpFmHSgC4Q"),
            ("Good as Hell - Lizzo", "https://www.youtube.com/watch?v=SSo3DK0TLQ0"),
            ("Try - Colbie Caillat", "https://www.youtube.com/watch?v=GXoZLPSw8U8"),
            ("Confident - Demi Lovato", "https://www.youtube.com/watch?v=cwLRQn61oUY")
        ]
    },
    "천칭자리": {
        "운세": [
            "균형과 조화가 중요한 하루입니다.",
            "타인의 의견을 존중하면 좋은 결과가 따를 거예요.",
            "협력이 필요한 일이 생길 수 있어요."
        ],
        "음악": [
            ("Just the Way You Are - Bruno Mars", "https://www.youtube.com/watch?v=LjhCEhWiKXk"),
            ("Count on Me - Bruno Mars", "https://www.youtube.com/watch?v=ZMsvwwp6SZI"),
            ("Home - Phillip Phillips", "https://www.youtube.com/watch?v=HoRkntoHkIE"),
            ("Put It All On Me - Ed Sheeran", "https://www.youtube.com/watch?v=ryJgDL9jzKk"),
            ("Lucky - Jason Mraz & Colbie Caillat", "https://www.youtube.com/watch?v=acvIVA9-FMQ"),
            ("Best Part - Daniel Caesar ft. H.E.R.", "https://www.youtube.com/watch?v=hKgl5-lkT8U")
        ]
    },
    "전갈자리": {
        "운세": [
            "직관이 뛰어난 하루입니다. 감정에 귀를 기울이세요.",
            "중요한 결정을 내리게 될 수도 있어요.",
            "내면의 목소리를 믿어보세요."
        ],
        "음악": [
            ("Believer - Imagine Dragons", "https://www.youtube.com/watch?v=7wtfhZwyrcc"),
            ("Demons - Imagine Dragons", "https://www.youtube.com/watch?v=mWRsgZuwf_8"),
            ("Take Me To Church - Hozier", "https://www.youtube.com/watch?v=MYSVMgRr6pw"),
            ("Elastic Heart - Sia", "https://www.youtube.com/watch?v=KWZGAExj-es"),
            ("Control - Halsey", "https://www.youtube.com/watch?v=1qxSwJC3LyA"),
            ("Bury a Friend - Billie Eilish", "https://www.youtube.com/watch?v=HUHC9tYz8ik")
        ]
    },
    "사수자리": {
        "운세": [
            "새로운 아이디어가 떠오르는 날입니다.",
            "모험과 도전 정신이 복을 부를 거예요.",
            "즐거운 변화가 찾아옵니다."
        ],
        "음악": [
            ("On Top of the World - Imagine Dragons", "https://www.youtube.com/watch?v=w5tWYmIOWGk"),
            ("Adventure of a Lifetime - Coldplay", "https://www.youtube.com/watch?v=QtXby3twMmI"),
            ("Send Me On My Way - Rusted Root", "https://www.youtube.com/watch?v=IGMabBGydC0"),
            ("Good Life - OneRepublic", "https://www.youtube.com/watch?v=jZhQOvvV45w"),
            ("Riptide - Vance Joy", "https://www.youtube.com/watch?v=uJ_1HMAGb4k"),
            ("Hey, Soul Sister - Train", "https://www.youtube.com/watch?v=kVpv8-5XWOI")
        ]
    },
    "염소자리": {
        "운세": [
            "차분하게 목표를 향해 나아가야 할 날입니다.",
            "노력의 결실이 나타날 수 있어요.",
            "꾸준함이 결국 성공을 이끌 거예요."
        ],
        "음악": [
            ("The Climb - Miley Cyrus", "https://www.youtube.com/watch?v=NG2zyeVRcbs"),
            ("Hall of Fame - The Script", "https://www.youtube.com/watch?v=mk48xRzuNvA"),
            ("Work - Rihanna ft. Drake", "https://www.youtube.com/watch?v=HL1UzIK-flA"),
            ("Whatever It Takes - Imagine Dragons", "https://www.youtube.com/watch?v=gOsM-DYAEhY"),
            ("Don't Stop - Fleetwood Mac", "https://www.youtube.com/watch?v=mrZRURcb1cM"),
            ("Unstoppable - Sia", "https://www.youtube.com/watch?v=cxjvTXo9WWM")
        ]
    },
    "물병자리": {
        "운세": [
            "독창적인 생각이 빛나는 날입니다.",
            "남들과 다른 당신의 시도가 큰 변화를 만들 수 있어요.",
            "새로운 기술이나 지식에 도전해보세요."
        ],
        "음악": [
            ("Electric Feel - MGMT", "https://www.youtube.com/watch?v=MmZexg8sxyk"),
            ("Rather Be - Clean Bandit", "https://www.youtube.com/watch?v=m-M1AtrxztU"),
            ("Midnight City - M83", "https://www.youtube.com/watch?v=dX3k_QDnzHE"),
            ("Clocks - Coldplay", "https://www.youtube.com/watch?v=d020hcWA_Wg"),
            ("Pompeii - Bastille", "https://www.youtube.com/watch?v=F90Cw4l-8NY"),
            ("Kids - MGMT", "https://www.youtube.com/watch?v=bIEOZCcaXzE")
        ]
    },
    "물고기자리": {
        "운세": [
            "감수성이 예민해지는 날입니다. 예술적인 감각이 돋보여요.",
            "감정 표현을 솔직하게 해보세요.",
            "꿈과 현실 사이에서 균형을 잡아야 해요."
        ],
        "음악": [
            ("Dreams - Fleetwood Mac", "https://www.youtube.com/watch?v=mrZRURcb1cM"),
            ("Let Her Go - Passenger", "https://www.youtube.com/watch?v=RBumgq5yVrA"),
            ("A Thousand Years - Christina Perri", "https://www.youtube.com/watch?v=rtOvBOTyX00"),
            ("Lost Stars - Adam Levine", "https://www.youtube.com/watch?v=cL4uhaQ58Rk"),
            ("Ocean Eyes - Billie Eilish", "https://www.youtube.com/watch?v=viimfQi_pUw"),
            ("River Flows In You - Yiruma", "https://www.youtube.com/watch?v=7maJOI3QMu0")
        ]
    }
}

# Streamlit UI 구성
st.set_page_config(page_title="오늘의 운세와 음악", layout="centered")
st.title("🔮 오늘의 운세에 어울리는 음악 🎧")

zodiac = st.selectbox("자신의 별자리를 선택하세요:", list(fortune_music_data.keys()))
selected_date = st.date_input("운세를 보고 싶은 날짜를 선택하세요:", value=datetime.today())

if zodiac and selected_date:
    seed = f"{zodiac}-{selected_date}"
    random.seed(seed)

    fortune = random.choice(fortune_music_data[zodiac]["운세"])
    music_choices = random.sample(fortune_music_data[zodiac]["음악"], 2)

    st.markdown(f"### 📅 {selected_date.strftime('%Y년 %m월 %d일')} - {zodiac} 운세")
    st.success(f"✨ 오늘의 운세: {fortune}")
    st.markdown("🎵 오늘의 추천 음악:")

    for title, link in music_choices:
        st.markdown(f"- [{title}]({link})")
        st.video(link)
