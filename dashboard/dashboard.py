import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os, datetime

df_day = pd.read_csv("../dataset/day.csv")
df_hour = pd.read_csv("../dataset/hour.csv")

def preprocess(df_day:pd.DataFrame, df_hour:pd.DataFrame):
  df_day = df_day.copy()
  df_hour = df_hour.copy()

  #manage the collapse column of day and hour dataframe
  day_measure = ['temp', 'atemp', 'hum', 'windspeed', 'casual', 'registered', 'cnt']
  day_measure_dict = {x:f"{x}_day" for x in day_measure}
  df_day.rename(columns=day_measure_dict, inplace=True)

  drop_measure = [x for x in df_day.columns if x not in day_measure_dict.values()]
  drop_measure.remove('dteday')
  df_day.drop(drop_measure, axis=1, inplace=True)

  df_merge = pd.DataFrame(df_hour.merge(df_day, on="dteday", how="left"))

  return df_merge

def plot_season(df:pd.DataFrame):
    df = df.copy()
    season_1 = df[df['season']==1]
    season_1 = season_1['season'].count()
    season_2 = df[df['season']==2]
    season_2 = season_2.season.count()
    season_3 = df[df['season']==3]
    season_3 = season_3.season.count()
    season_4 = df[df['season']==4]
    season_4 = season_4.season.count()

    label = ["Springer","Summer","Fall","Winter"]
    x = [season_1, season_2, season_3, season_4]

    fig, ax = plt.subplots(figsize=(8,4))
    ax.pie(x=x, labels=label, autopct='%.0f%%', explode=[0,0,0.1,0])
    return fig

def plot_weather(df:pd.DataFrame):
    df = df.copy()
    weather1 = df[df['weathersit']==1]
    weather1 = weather1['weathersit'].count()
    weather2 = df[df['weathersit']==2]
    weather2 = weather2['weathersit'].count()
    weather3 = df[df['weathersit']==3]
    weather3 = weather3['weathersit'].count()
    weather4 = df[df['weathersit']==4]
    weather4 = weather4['weathersit'].count()

    label = ["weather 1","weather 2","weather 3","weather 4"]
    x = [weather1, weather2, weather3, weather4]

    fig, ax = plt.subplots(figsize=(8,4))
    ax.pie(x=x, labels=label, autopct='%.0f%%', explode=[0.1,0,0,0])
    return fig

def bar_weather(df:pd.DataFrame):
    df = df.copy()
    weather1 = df[df['weathersit']==1]
    weather1 = weather1['weathersit'].count()
    weather2 = df[df['weathersit']==2]
    weather2 = weather2['weathersit'].count()
    weather3 = df[df['weathersit']==3]
    weather3 = weather3['weathersit'].count()
    weather4 = df[df['weathersit']==4]
    weather4 = weather4['weathersit'].count()

    label = ["weather 1","weather 2","weather 3","weather 4"]
    y = [weather1, weather2, weather3, weather4]

    fig,ax = plt.subplots(figsize=(8,4))
    ax.bar(height=y, x=label)
    return fig

def lineChart_bike(df:pd.DataFrame):
    df = df.copy()
    amount = df['cnt_day']
    date = df['dteday']

    fig,ax = plt.subplots()
    ax.plot(date, amount)
    return fig

df_merge = preprocess(df_day, df_hour)

st.title("Proyek Akhir Belajar Analisis Data dengan Python")
st.subheader("Muhammad Adnan Bayu Firdaus ML-56")

with st.container():
    st.header("Dataframe")
    st.dataframe(data=df_merge, width=500, height=150)

with st.container():
    st.header("People's Favorite Season to Rent a Bike")
    out = plot_season(df_merge)
    st.pyplot(out)

with st.container():
    st.header("People's Favorite Weather to Rent a Bike")
    col1, col2 = st.columns(2)
    with col1:
        out = plot_weather(df_merge)
        st.pyplot(out)
    with col2:
        out = bar_weather(df_merge)
        st.pyplot(out)

with st.container():
    st.header("Rent Bike Trend in 2011-2012")
    out = lineChart_bike(df_merge)
    st.pyplot(out)