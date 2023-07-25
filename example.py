import streamlit as st
import altair as alt
import numpy as np
import pandas as pd

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
