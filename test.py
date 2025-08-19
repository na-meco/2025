import streamlit as st
import datetime as dt
import random
import hashlib
import io

# -----------------------------
# Utilities
# -----------------------------

def seed_from(sign: str, date: dt.date, extra: str = "") -> int:
    base = f"{sign}|{date.isoformat()}|{extra}"
    return int(hashlib.sha256(base.encode()).hexdigest(), 16) % (2**32 - 1)


def dchoice(rng: random.Random, items, k: int):
    # Deterministic sample without replacement but allow wrap if k > len(items)
    if k <= len(items):
        return rng.sample(items, k)
    # if requesting more than available, repeat shuffled cycles
    out = []
    pool = items[:]
    while len(out) < k:
        rng.shuffle(pool)
        need = min(k - len(out), len(pool))
        out.extend(pool[:need])
    return out


# -----------------------------
# Data: Zodiac
# -----------------------------
ZODIACS = [
    ("양자리", "Aries", (3, 21), (4, 19)),
    ("황소자리", "Taurus", (4, 20), (5, 20)),
    ("쌍둥이자리", "Gemini", (5, 21), (6, 21)),
    ("게자리", "Cancer", (6, 22), (7, 22)),
    ("사자자리", "Leo", (7, 23), (8, 22)),
    ("처녀자리", "Virgo", (8, 23), (9, 22)),
    ("천칭자리", "Libra", (9, 23), (10, 23)),
    ("전갈자리", "Scorpio", (10, 24), (11, 22)),
    ("사수자리", "Sagittarius", (11, 23), (12, 21)),
    ("염소자리", "Capricorn", (12, 22), (1, 19)),
    ("물병자리", "Aquarius", (1, 20), (2, 18)),
    ("물고기자리", "Pisces", (2, 19), (3, 20)),
]

SIGN_TRAITS = {
    "양자리": "도전적 · 추진력 · 솔직",
    "황소자리": "안정적 · 끈기 · 미식",
    "쌍둥이자리": "호기심 · 소통 · 다재다능",
    "게자리": "보호본능 · 배려 · 감수성",
    "사자자리": "자신감 · 창의 · 리더십",
    "처녀자리": "분석적 · 실용 · 섬세함",
    "천칭자리": "조화 · 매력 · 협상",
    "전갈자리": "집중력 · 열정 · 직감",
    "사수자리": "자유 · 낙관 · 탐험",
    "염소자리": "근면 · 책임 · 현실감",
    "물병자리": "독창 · 인도주의 · 통찰",
    "물고기자리": "공감 · 상상력 · 영감",
}

LUCKY_ITEMS = [
    "이어폰", "펜", "노트", "머그컵", "스트랩", "스티커", "책갈피", "스카프", "캔들", "키링",
    "파우치", "우산", "텀블러", "에코백", "스니커즈", "포스트잇", "립밤", "핸드크림", "손수건", "모자",
]

LUCKY_COLORS = [
    "네이비", "화이트", "블랙", "민트", "라벤더", "코랄", "버건디", "베이지", "올리브", "하늘색",
    "라임", "보라", "분홍", "회색", "카멜", "레몬", "초록", "주황", "빨강", "갈색",
]

# -----------------------------
# Data: Song catalog (mood-tagged)
# -----------------------------
# Each entry: (title, artist, mood)
CATALOG = [
    # Energetic
    ("Dynamite", "BTS", "energetic"),
    ("Tomboy", "(G)I-DLE", "energetic"),
    ("Next Level", "aespa", "energetic"),
    ("Boombayah", "BLACKPINK", "energetic"),
    ("Hype Boy", "NewJeans", "energetic"),
    ("Savage Love (Laxed)", "Jawsh 685 & Jason Derulo", "energetic"),
    ("Levitating", "Dua Lipa", "energetic"),
    ("Blinding Lights", "The Weeknd", "energetic"),
    ("Don't Start Now", "Dua Lipa", "energetic"),
    ("Kill This Love", "BLACKPINK", "energetic"),
    ("QUEENCARD", "(G)I-DLE", "energetic"),
    ("Butter", "BTS", "energetic"),
    ("Spicy", "aespa", "energetic"),
    ("FAST FORWARD", "전소미", "energetic"),
    ("BAMY", "RIIZE", "energetic"),

    # Happy / Uplifting
    ("Palette", "IU (feat. G-DRAGON)", "happy"),
    ("Good Day", "IU", "happy"),
    ("Feel Special", "TWICE", "happy"),
    ("Dance The Night", "Dua Lipa", "happy"),
    ("Shake It Off", "Taylor Swift", "happy"),
    ("Walkin' On Sunshine", "Katrina & The Waves", "happy"),
    ("What Makes You Beautiful", "One Direction", "happy"),
    ("Permission to Dance", "BTS", "happy"),
    ("Holiday", "Girls' Generation", "happy"),
    ("BBoom BBoom", "MOMOLAND", "happy"),
    ("LILAC", "IU", "happy"),
    ("Cheer Up", "TWICE", "happy"),

    # Chill
    ("8", "IU & SUGA", "chill"),
    ("Love Me Like You Do", "Ellie Goulding", "chill"),
    ("drivers license", "Olivia Rodrigo", "chill"),
    ("ocean eyes", "Billie Eilish", "chill"),
    ("Best Part", "Daniel Caesar & H.E.R.", "chill"),
    ("Snooze", "SZA", "chill"),
    ("Angel Baby", "Troye Sivan", "chill"),
    ("Love Dive", "IVE", "chill"),
    ("Paris In The Rain", "Lauv", "chill"),
    ("Through The Night", "IU", "chill"),
    ("At My Worst", "Pink Sweat$", "chill"),
    ("Hair Tie", "woo!ah!", "chill"),

    # Focus / Study
    ("weightless", "Armin van Buuren", "focus"),
    ("Clair de Lune", "Debussy", "focus"),
    ("Gymnopédie No.1", "Satie", "focus"),
    ("River Flows In You", "Yiruma", "focus"),
    ("Nuvole Bianche", "Ludovico Einaudi", "focus"),
    ("Spring Day (Piano)", "BTS Piano Cover", "focus"),
    ("Time", "Hans Zimmer", "focus"),
    ("Comptine d'un autre été", "Yann Tiersen", "focus"),
    ("Merry-Go-Round of Life", "Joe Hisaishi", "focus"),
    ("Canon in D", "Pachelbel", "focus"),
    ("Kiss The Rain", "Yiruma", "focus"),
    ("A Shine Upon You", "Lee Byung-woo", "focus"),

    # Confident / Money / Hustle
    ("MIC Drop", "BTS", "confident"),
    ("Boss Bitch", "Doja Cat", "confident"),
    ("God Is A Woman", "Ariana Grande", "confident"),
    ("IDOL", "BTS", "confident"),
    ("Fancy", "TWICE", "confident"),
    ("Bad Guy", "Billie Eilish", "confident"),
    ("Can't Hold Us", "Macklemore & Ryan Lewis", "confident"),
    ("Uptown Funk", "Mark Ronson ft. Bruno Mars", "confident"),
    ("BOSS", "NCT U", "confident"),
    ("MEGAVERSE", "Stray Kids", "confident"),
    ("Ditto", "NewJeans", "confident"),
    ("Savage", "aespa", "confident"),

    # Romance / Love
    ("Love Scenario", "iKON", "romance"),
    ("Blueming", "IU", "romance"),
    ("ROSE", "D.O.", "romance"),
    ("200%", "AKMU", "romance"),
    ("Love Story", "Taylor Swift", "romance"),
    ("All of Me", "John Legend", "romance"),
    ("Photograph", "Ed Sheeran", "romance"),
    ("Spring Day", "BTS", "romance"),
    ("I Will Always Love You", "Whitney Houston", "romance"),
    ("Officially Missing You", "Tamia", "romance"),
    ("Everytime", "CHEN & Punch", "romance"),
    ("Love poem", "IU", "romance"),

    # Healing / Health
    ("Heal Me", "SHINee", "healing"),
    ("Breathe", "LEE HI", "healing"),
    ("Comforting", "10cm", "healing"),
    ("Way Back Home", "SHAUN", "healing"),
    ("Answer: Love Myself", "BTS", "healing"),
    ("Lost Stars", "Adam Levine", "healing"),
    ("Peaches", "Justin Bieber", "healing"),
    ("Haru Haru", "BIGBANG", "healing"),
    ("Stressed Out", "Twenty One Pilots", "healing"),
    ("If You", "BIGBANG", "healing"),
    ("Hold My Hand", "IU", "healing"),
    ("Hug", "TVXQ!", "healing"),

    # Adventure / Sagittarius vibe
    ("Adventure of a Lifetime", "Coldplay", "adventure"),
    ("On The Road", "Post Malone", "adventure"),
    ("Maps", "Maroon 5", "adventure"),
    ("Rather Be", "Clean Bandit", "adventure"),
    ("Wake Me Up", "Avicii", "adventure"),
    ("Geronimo", "Sheppard", "adventure"),
    ("Ride", "Lana Del Rey", "adventure"),
    ("High Hopes", "Panic! At The Disco", "adventure"),
    ("On The Ground", "ROSÉ", "adventure"),
    ("Run", "BTS", "adventure"),
    ("RUN2U", "STAYC", "adventure"),
    ("We Go Up", "NCT DREAM", "adventure"),
]

MOODS = ["energetic", "happy", "chill", "focus", "confident", "romance", "healing", "adventure"]

CATALOG_BY_MOOD = {m: [s for s in CATALOG if s[2] == m] for m in MOODS}

# -----------------------------
# Fortune engine
# -----------------------------

AREAS = ["사랑", "일/학업", "금전", "건강"]

AREA_TEMPLATES = {
    "high": {
        "사랑": "호감 신호가 또렷합니다. 솔직한 대화가 관계를 한 단계 끌어올려요.",
        "일/학업": "집중력이 최상! 깔끔한 마감과 빠른 피드백으로 성과가 보입니다.",
        "금전": "가치 있는 지출과 작은 수익이 함께 들어옵니다. 투자·저축 모두 유리한 날.",
        "건강": "컨디션이 가벼워요. 가벼운 유산소나 스트레칭이 효율을 끌어올립니다.",
    },
    "mid": {
        "사랑": "기대만큼은 아니어도 안정적이에요. 작은 친절이 큰 효과를 냅니다.",
        "일/학업": "루틴을 지키면 무난히 통과. 새로운 일은 최소화하는 게 좋아요.",
        "금전": "수입·지출 균형감. 큰 결정보다 실행 가능한 절약 한 가지를 시도해보세요.",
        "건강": "기복은 있지만 회복 가능. 수분 섭취와 수면 리듬을 우선하세요.",
    },
    "low": {
        "사랑": "오해가 생기기 쉬워요. 메시지를 한 번 더 확인하고 답변은 부드럽게.",
        "일/학업": "집중 분산 주의. 할 일을 쪼개서 25분 타이머로 끊어가면 좋아요.",
        "금전": "충동구매 경고! 장바구니에 넣고 하루 뒤 결정하세요.",
        "건강": "무리하면 바로 티가 납니다. 휴식·영양 우선으로 스케줄을 조정하세요.",
    },
}

SIGN_OPENERS = {
    "양자리": "불꽃처럼 시작을 여는 날",
    "황소자리": "차분함 속에서 확실히 쌓이는 운",
    "쌍둥이자리": "대화가 기회를 부르는 하루",
    "게자리": "정서적 안전이 실력을 끌어올려요",
    "사자자리": "무대 중앙에 서도 좋은 시점",
    "처녀자리": "정밀함이 빛나는 효율의 날",
    "천칭자리": "균형을 잡는 당신에게 바람이 붑니다",
    "전갈자리": "집중이 성과를 낚아채는 타이밍",
    "사수자리": "확장과 탐험의 행운",
    "염소자리": "꾸준함이 곧 파워가 되는 날",
    "물병자리": "틀을 깨는 아이디어의 순간",
    "물고기자리": "감성이 영감을 만드는 하루",
}

MOOD_BY_AREA = {
    "사랑": "romance",
    "일/학업": "focus",
    "금전": "confident",
    "건강": "healing",
}


def roll_scores(sign: str, date: dt.date):
    rng = random.Random(seed_from(sign, date, "scores"))
    scores = {area: rng.randint(35, 95) for area in AREAS}
    # Small sign-flavor boost
    boost_map = {
        "양자리": "일/학업", "황소자리": "금전", "쌍둥이자리": "사랑", "게자리": "건강",
        "사자자리": "사랑", "처녀자리": "일/학업", "천칭자리": "사랑", "전갈자리": "일/학업",
        "사수자리": "일/학업", "염소자리": "금전", "물병자리": "일/학업", "물고기자리": "사랑",
    }
    boosted = boost_map.get(sign)
    if boosted:
        scores[boosted] = min(100, scores[boosted] + 7)
    return scores


def score_tier(score: int) -> str:
    if score >= 75:
        return "high"
    if score >= 55:
        return "mid"
    return "low"


def fortune_paragraphs(sign: str, date: dt.date):
    scores = roll_scores(sign, date)
    parts = []
    opener = SIGN_OPENERS.get(sign, "오늘")
    parts.append(f"**{opener}** — {SIGN_TRAITS.get(sign, '')}")
    for area in AREAS:
        s = scores[area]
        tier = score_tier(s)
        tip = AREA_TEMPLATES[tier][area]
        parts.append(f"**{area} {s}/100** · {tip}")
    # lucky picks
    rng = random.Random(seed_from(sign, date, "lucky"))
    color = rng.choice(LUCKY_COLORS)
    item = rng.choice(LUCKY_ITEMS)
    lucky_num = rng.randint(1, 99)
    parts.append(f"**라키 컬러**: {color} · **라키 넘버**: {lucky_num} · **라키 아이템**: {item}")
    return parts, scores


def decide_moods(scores):
    # pick primary mood from best area, with health safeguard
    best_area = max(scores, key=scores.get)
    primary = MOOD_BY_AREA[best_area]
    alt = ["happy", "energetic", "chill", "adventure"]
    # if health low, prepend healing
    if scores["건강"] < 55:
        alt.insert(0, "healing")
    return [primary] + alt


def recommend_songs(sign: str, date: dt.date, scores, k: int):
    rng = random.Random(seed_from(sign, date, "songs"))
    moods = decide_moods(scores)
    pool = []
    for m in moods:
        pool.extend(CATALOG_BY_MOOD.get(m, []))
    # de-duplicate while keeping order
    seen = set()
    uniq_pool = []
    for s in pool:
        key = (s[0], s[1])
        if key not in seen:
            uniq_pool.append(s)
            seen.add(key)
    picks = dchoice(rng, uniq_pool, k)
    return picks


def playlist_to_text(sign: str, date: dt.date, songs):
    lines = [f"[{date.isoformat()}] {sign} 오늘의 플레이리스트 ({len(songs)}곡)"]
    for i, (title, artist, mood) in enumerate(songs, 1):
        lines.append(f"{i:02d}. {title} — {artist}  #{mood}")
    return "\n".join(lines)


# -----------------------------
# UI
# -----------------------------
st.set_page_config(page_title="별자리 오늘의 운세 & 노래 추천", page_icon="✨", layout="wide")

st.title("✨ 별자리 오늘의 운세 & 노래 추천")
st.caption("날짜에 따라 운세와 추천 곡이 달라져요. (동일한 날짜·별자리는 항상 동일 추천)")

with st.sidebar:
    st.header("설정")
    sign = st.selectbox(
        "별자리를 선택하세요",
        [k for k, _, _, _ in ZODIACS],
        index=0,
    )
    today = dt.date.today()
    picked_date = st.date_input("날짜 선택", value=today, min_value=dt.date(2000,1,1), max_value=dt.date(2100,12,31))
    num_songs = st.slider("추천 곡 수", min_value=10, max_value=60, value=25, step=5)
    st.markdown("---")
    st.write("**참고**: 추천은 고정된 DB 기반이며, CSV로 확장할 수 있는 기능은 곧 추가할 수 있어요.")

cols = st.columns([1.2, 1])

with cols[0]:
    st.subheader(f"{picked_date.strftime('%Y-%m-%d')} · {sign} 운세")
    paras, scores = fortune_paragraphs(sign, picked_date)
    for p in paras:
        st.markdown(f"- {p}")

    st.markdown("### 영역별 점수")
    score_cols = st.columns(4)
    for i, area in enumerate(AREAS):
        with score_cols[i]:
            st.metric(label=area, value=f"{scores[area]}/100")

with cols[1]:
    st.subheader("오늘의 무드")
    st.write(
        " → ".join(decide_moods(scores))
    )

st.markdown("---")

songs = recommend_songs(sign, picked_date, scores, num_songs)

st.subheader(f"추천 플레이리스트 · {len(songs)}곡")
for idx, (title, artist, mood) in enumerate(songs, 1):
    st.write(f"{idx:02d}. **{title}** — {artist}  · #{mood}")

# Download
playlist_text = playlist_to_text(sign, picked_date, songs)
bytes_io = io.BytesIO(playlist_text.encode("utf-8"))
st.download_button(
    label="플레이리스트(.txt) 다운로드",
    data=bytes_io,
    file_name=f"{picked_date.isoformat()}_{sign}_playlist.txt",
    mime="text/plain",
)

st.markdown(
    "<small>ⓘ 이 앱은 교육·데모 목적이며 모든 상표와 곡 타이틀은 각 권리자에게 귀속됩니다.</small>",
    unsafe_allow_html=True,
)
