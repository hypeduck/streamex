import streamlit as st
import altair as alt
import numpy as np
import pandas as pd
from datetime import time, datetime

st.header("Demo")

st.write("1번")
st.write("2번")

df = pd.DataFrame({"first": [1, 2, 3, 4], "second": ["가", "나", "다", "라"]})

st.write(df)

st.write("공백")

st.write("데이터프레임", df, "데이터프레임")

df2 = pd.DataFrame(np.random.randn(200, 3), columns=["a", "b", "c"])
c = (
    alt.Chart(df2)
    .mark_circle()
    .encode(x="a", y="b", size="c", color="c", tooltip=["a", "b", "c"])
)

st.write(c)

st.header("깃 테스트")
st.subheader("깃 테스트")
st.write("깃 테스트")

age = st.slider("너 몇 살이니", 0, 130, 25)
st.write("나는", age, "살이야.")

values = st.slider("레인지 선택", 0.0, 100.0, (25.0, 75.0))
st.write("값:", values)

appointment = st.slider("계획", value=(time(11, 30), time(12, 45)))
st.write("계획된 시간 : ", appointment)

start_time = st.slider(
    "시작시간?", value=datetime(2020, 1, 1, 9, 30), format="MM/DD/YY - hh:mm"
)
st.write(f"시작시간 : {start_time}")

st.header("라인차트")

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.line_chart(chart_data)

st.header("선택박스")

option = st.selectbox("좋아하는 색상은?", ("파랑", "빨강", "초록"))

st.write("너의 색상은", option)

st.header("멀티 선택")
optiions = st.multiselect("좋아하는 색상들은?", ["초록", "노랑", "빨강"], ["노랑", "빨강"])

st.write(f"선택 색상들 : {optiions}")

st.header("체크박스")

icecream = st.checkbox("아이스크림")
coffee = st.checkbox("커피")
cola = st.checkbox("콜라")

if icecream:
    st.write("수박바")
if coffee:
    st.write("스타벅스")
if cola:
    st.write("코카콜라")
