import streamlit as st
import datetime

st.set_page_config(page_title="💖 사주 궁합 테스트 💖", page_icon="🔮", layout="centered")

# 🎨 제목 & 설명
st.markdown("""
<h1 style='text-align: center; color: hotpink;'>💘 운명 궁합 테스트 💘</h1>
<p style='text-align: center; font-size:18px;'>
🌟 당신과 그 사람의 인연, 사주로 알아보아요! 🌟<br>
생년월일과 성별만 입력하면 💖 사랑 점수 💖가 나옵니다.
</p>
""", unsafe_allow_html=True)

# 👫 입력 폼
st.subheader("✨ 당신의 정보")
col1, col2 = st.columns(2)
with col1:
    my_birth = st.date_input("📅 생년월일", datetime.date(2000, 1, 1))
with col2:
    my_gender = st.selectbox("🚻 성별", ["남성", "여성"])

st.subheader("✨ 상대방의 정보")
col3, col4 = st.columns(2)
with col3:
    partner_birth = st.date_input("📅 생년월일", datetime.date(2000, 1, 1), key="partner_birth")
with col4:
    partner_gender = st.selectbox("🚻 성별", ["남성", "여성"], key="partner_gender")

# 🧮 간단 궁합 계산 함수
def calc_score(birth1, birth2):
    diff_days = abs((birth1 - birth2).days)
    score = 100 - (diff_days % 60)  # 간단한 모의 계산
    if score < 40:
        score += 20  # 너무 낮으면 보정
    return min(score, 100)

if st.button("🔮 궁합 보기"):
    score = calc_score(my_birth, partner_birth)

    # 결과 출력
    st.markdown(f"""
    <div style='text-align:center; font-size:22px;'>
        💞 <b style='color:deeppink;'>당신들의 궁합 점수</b> 💞<br>
        <h1 style='color:gold; font-size:60px;'>{score}점</h1>
        {"💖 완벽한 궁합! 천생연분 💖" if score >= 85 else "💌 서로 노력하면 좋은 인연 💌" if score >= 60 else "⚡ 성격 차이 주의! ⚡"}
    </div>
    """, unsafe_allow_html=True)

    # 결과 메시지
    if score >= 85:
        st.success("🌟 축하드려요! 두 분은 정말 운명적인 만남이에요!")
    elif score >= 60:
        st.info("💫 아직 성장할 여지가 있는 관계! 대화를 많이 해보세요.")
    else:
        st.warning("🌧 가치관 차이가 있을 수 있으니 천천히 알아가세요.")

    # 다운로드 버튼 (텍스트 저장)
    result_text = f"사주 궁합 결과\n점수: {score}점\n메시지: {'운명적 사랑' if score>=85 else '노력이 필요한 관계'}"
    st.download_button(
        label="📥 결과 저장하기",
        data=result_text,
        file_name="궁합결과.txt",
        mime="text/plain"
    )
