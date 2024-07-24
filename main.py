import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import koreanize_matplotlib

# Streamlit 애플리케이션 제목
st.title('20세 미만 성별 비율 분석')

# 파일 업로드 위젯
uploaded_file = st.file_uploader("파일을 업로드하세요 (CSV 또는 Excel 형식)", type=['csv', 'xlsx'])

if uploaded_file is not None:
    # 파일 형식에 따라 데이터프레임 읽기
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    elif uploaded_file.name.endswith('.xlsx'):
        df = pd.read_excel(uploaded_file)
    else:
        st.error("지원되지 않는 파일 형식입니다.")
        st.stop()

    # 데이터 구조 확인
    st.write("데이터 미리보기:")
    st.write(df.head())

    # 필수 열이 존재하는지 확인
    if 'age' not in df.columns or 'gender' not in df.columns:
        st.error("파일에 'age'와 'gender' 열이 포함되어야 합니다.")
        st.stop()

    # 20세 미만 데이터 필터링
    df_young = df[df['age'] < 20]

    # 성별 비율 계산
    gender_counts = df_young['gender'].value_counts()

    # 원그래프 그리기
    fig, ax = plt.subplots()
    ax.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=140, colors=['blue', 'pink'])
    ax.set_title('20세 미만의 성별 비율')

    st.pyplot(fig)
