import streamlit as st
import pandas as pd
import numpy as np

st.title('시간표')
st.write('김가현의 대학교 시간표 :')
st.write(pd.DataFrame({
    '월요일': ['초등과학교육론', '공강', '로봇과프로그래밍'],
    '화요일': ['초등도덕교육의실제', '초등컴퓨팅교재연구', '초등체육교과교육의이해'],
    '수요일': ['초등영어지도법', '앱프로그래밍', '공강'],
    '목요일': ['공강', '공강', '공강'],
    '금요일': ['미술과교재연구및교수법', '공강', '초등수학교육의실제']
}))

st.markdown(
    """
    이건 스트림릿 플레이 그라운드로 만든 나의 시간표야.
    
    **이건 :rainbow[DataFrame]을 써서 만든 시간표지!**

    streamlit markdown을 이용하면 줄바꿈과 빈줄 넣기가 돼.
    아 맞아 * 두 개로 **강조**도 할 수 있어!
    streamlit 전용으로 :rainbow[무지개]도 만들 수 있지!
    """
)

st.write('button을 이용해 버튼도 만들 수 있어. 이 버튼은 평소에는 F지만, 누르면 T가 돼!')
if st.button("풍선을 보내자!"):
    st.balloons()
st.write('if문을 이용해 F가 T가 되었을 때, balloons 명령어로 **:rainbow[풍선]**을 보내는거야!')
