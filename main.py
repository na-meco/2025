import streamlit as st
from PIL import Image
import numpy as np

st.title("🎨 픽셀아트 변환기")

uploaded_file = st.file_uploader("이미지를 업로드하세요", type=["png", "jpg", "jpeg"])

pixel_size = st.slider("픽셀 크기 (작을수록 세밀)", 4, 64, 16)

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    img = img.convert("RGB")  # 색상 통일

    # 원본 크기
    w, h = img.size

    # 축소 -> 확대 (픽셀화)
    img_small = img.resize(
        (w // pixel_size, h // pixel_size),
        resample=Image.NEAREST
    )
    pixel_art = img_small.resize(
        (w, h),
        resample=Image.NEAREST
    )

    st.image(pixel_art, caption="픽셀아트 변환 결과", use_column_width=True)

    # 다운로드 버튼
    img_array = np.array(pixel_art)
    result_image = Image.fromarray(img_array)
    st.download_button(
        label="결과 다운로드",
        data=img_array.tobytes(),
        file_name="pixel_art.png",
        mime="image/png"
    )
