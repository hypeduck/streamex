import streamlit as st
import pandas as pd
import numpy as np
import geopandas as gpd
import plotly.express as px


def create_data():
    seoul = gpd.read_file("seoul.json", encoding="utf-8")
    districts = seoul["name_eng"].tolist()
    df1 = pd.read_csv("nano_dust.csv")
    df1.set_index("loc", inplace=True)
    df1 = df1.transpose()
    df1 = df1.loc[df1.index != "avg"]
    df_long = df1.reset_index().melt(
        id_vars=["index"], var_name="name_eng", value_name="num_sold"
    )
    df_long.rename(columns={"index": "date"}, inplace=True)
    df = pd.DataFrame(
        {
            "date": np.tile(pd.date_range("2022-01-01", periods=31), len(districts)),
            "name_eng": np.repeat(districts, 31),
            "num_sold": np.random.randint(1000, 5000, len(districts) * 31),
        }
    )
    df["date"] = df["date"].astype(str)
    df["num_sold"] = df_long["num_sold"]
    return df, seoul


def create_choropleth(df, seoul):
    fig = px.choropleth_mapbox(
        df,
        geojson=seoul.__geo_interface__,
        featureidkey="properties.name_eng",
        locations="name_eng",
        color="num_sold",
        color_continuous_scale="OrRd",
        range_color=[0, 150],
        animation_frame="date",
    ).update_layout(
        mapbox={
            "style": "carto-positron",
            "zoom": 9,
            "center": {
                "lat": seoul.unary_union.centroid.y,
                "lon": seoul.unary_union.centroid.x,
            },
        },
        autosize=True,
    )
    return fig


# def main():
#     st.title("Choropleth Animation Example")
#     df, seoul = create_data()
#     fig1 = create_choropleth(df, seoul)
#     fig2 = create_choropleth(df, seoul)  # 이 부분을 두 개의 다른 데이터 세트로 수정해야 합니다.
#     col1, col2 = st.columns(2)
#     col1.plotly_chart(fig1)
#     col2.plotly_chart(fig2)


def main():
    st.title("Choropleth Animation Example")
    df, seoul = create_data()
    fig1 = create_choropleth(df, seoul)
    fig2 = create_choropleth(df, seoul)  # 이 부분을 두 개의 다른 데이터 세트로 수정해야 합니다.
    st.plotly_chart(fig1)
    st.plotly_chart(fig2)


if __name__ == "__main__":
    main()
