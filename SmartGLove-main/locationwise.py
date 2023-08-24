import pandas as pd
import plotly.express as px
import streamlit as st

def showmaps():
    st.markdown("<h1 style='text-align: center; color: yellow ;'></h1>", unsafe_allow_html=True)
    st.header("For the following diseases :")
    col1, col2 = st.columns([5, 5])
    with col1:
        st.markdown("[AIDS](#1)")
        st.markdown("[Chicken Pox](#2)")
        st.markdown("[Common Cold](#3)")
        st.markdown("[Fungal Infection](#4)")
        st.markdown("[Gastroenteritis](#5)")
        st.markdown("[GERD](#6)")
    with col2:
        st.markdown("[Hepatitis](#7)")
        st.markdown("[Impetigo](#8)")
        st.markdown("[Pneumonia](#9)")
        st.markdown("[Tuberculosis](#10)")
        st.markdown("[Typhoid](#11)")

    # <editor-fold desc=" 1) AIDS">
    df = pd.read_csv("datasets\\AIDS.csv")
    fig1 = px.choropleth(
        df,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='state',
        color='active cases',
        color_continuous_scale='reds')
    fig1.update_geos(fitbounds="locations", visible=False)
    fig2 = px.pie(df, values='active cases', names='state')
    fig2.update_traces(textposition='inside', textinfo='value+label')
    st.markdown("<h6 style='color: skyblue;'></h6>", unsafe_allow_html=True)
    st.markdown("<h6 style='color: skyblue;'></h6>", unsafe_allow_html=True)
    st.header("For Disease 'AIDS' : ",anchor="1")
    col1, col2 = st.columns([6,4])
    with col1:
        st.plotly_chart(fig1)
    with col2:
        st.plotly_chart(fig2)
    # </editor-fold>

    # <editor-fold desc="2) Chicken Pox">
    df = pd.read_csv("datasets\\Chickenpox.csv")
    fig1 = px.choropleth(
        df,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='state',
        color='active cases',
        color_continuous_scale='puor')
    fig1.update_geos(fitbounds="locations", visible=False)
    fig2 = px.pie(df, values='active cases', names='state')
    fig2.update_traces(textposition='inside', textinfo='value+label')
    st.markdown("<h6 style='color: skyblue;'></h6>", unsafe_allow_html=True)
    st.markdown("<h6 style='color: skyblue;'></h6>", unsafe_allow_html=True)
    st.header("For Disease 'Chicken pox' :",anchor="2")
    col1, col2 = st.columns([6, 4])
    with col1:
        st.plotly_chart(fig1)
    with col2:
        st.plotly_chart(fig2)
    # </editor-fold>

    # <editor-fold desc="3) Common Cold">
    df = pd.read_csv("datasets\\Commoncold.csv")
    fig1 = px.choropleth(
        df,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='state',
        color='active cases',
        color_continuous_scale='icefire')
    fig1.update_geos(fitbounds="locations", visible=False)
    fig2 = px.pie(df, values='active cases', names='state')
    fig2.update_traces(textposition='inside', textinfo='value+label')
    st.markdown("<h6 style='color: skyblue;'></h6>", unsafe_allow_html=True)
    st.markdown("<h6 style='color: skyblue;'></h6>", unsafe_allow_html=True)
    st.header("For Disease 'Common Cold' :", anchor="3")
    col1, col2 = st.columns([6, 4])
    with col1:
        st.plotly_chart(fig1)
    with col2:
        st.plotly_chart(fig2)
    # </editor-fold>

    # <editor-fold desc="4) Fungal Infection">
    df = pd.read_csv("datasets\\fungalifection.csv")
    fig1 = px.choropleth(
        df,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='state',
        color='active cases',
        color_continuous_scale='gnbu')
    fig1.update_geos(fitbounds="locations", visible=False)
    fig2 = px.pie(df, values='active cases', names='state')
    fig2.update_traces(textposition='inside', textinfo='value+label')
    st.markdown("<h6 style='color: skyblue;'></h6>", unsafe_allow_html=True)
    st.markdown("<h6 style='color: skyblue;'></h6>", unsafe_allow_html=True)
    st.header("For Disease 'Fungal Infection' :", anchor="4")
    col1, col2 = st.columns([6, 4])
    with col1:
        st.plotly_chart(fig1)
    with col2:
        st.plotly_chart(fig2)
    # </editor-fold>

    # <editor-fold desc="5) Gastroenteritis">
    df = pd.read_csv("datasets\\Gastro.csv")
    fig1 = px.choropleth(
        df,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='state',
        color='active cases',
        color_continuous_scale='mrybm')
    fig1.update_geos(fitbounds="locations", visible=False)
    fig2 = px.pie(df, values='active cases', names='state')
    fig2.update_traces(textposition='inside', textinfo='value+label')
    st.markdown("<h6 style='color: skyblue;'></h6>", unsafe_allow_html=True)
    st.markdown("<h6 style='color: skyblue;'></h6>", unsafe_allow_html=True)
    st.header("For Disease 'Gastroenteritis' :", anchor="5")
    col1, col2 = st.columns([6, 4])
    with col1:
        st.plotly_chart(fig1)
    with col2:
        st.plotly_chart(fig2)
    # </editor-fold>

    # <editor-fold desc="6) GERD">
    df = pd.read_csv("datasets\\GERD.csv")
    fig1 = px.choropleth(
        df,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='state',
        color='active cases',
        color_continuous_scale='inferno')
    fig1.update_geos(fitbounds="locations", visible=False)
    fig2 = px.pie(df, values='active cases', names='state')
    fig2.update_traces(textposition='inside', textinfo='value+label')
    st.markdown("<h6 style='color: skyblue;'></h6>", unsafe_allow_html=True)
    st.markdown("<h6 style='color: skyblue;'></h6>", unsafe_allow_html=True)
    st.header("For Disease 'GERD' :", anchor="6")
    col1, col2 = st.columns([6, 4])
    with col1:
        st.plotly_chart(fig1)
    with col2:
        st.plotly_chart(fig2)
    # </editor-fold>

    # <editor-fold desc="7) Hepatitis">
    df = pd.read_csv("datasets\\Hepatitis.csv")
    fig1 = px.choropleth(
        df,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='state',
        color='active cases',
        color_continuous_scale='plasma')
    fig1.update_geos(fitbounds="locations", visible=False)
    fig2 = px.pie(df, values='active cases', names='state')
    fig2.update_traces(textposition='inside', textinfo='value+label')
    st.markdown("<h6 style='color: skyblue;'></h6>", unsafe_allow_html=True)
    st.markdown("<h6 style='color: skyblue;'></h6>", unsafe_allow_html=True)
    st.header("For Disease 'Hepatitis A/B/C/D/E' :", anchor="7")
    col1, col2 = st.columns([6, 4])
    with col1:
        st.plotly_chart(fig1)
    with col2:
        st.plotly_chart(fig2)
    # </editor-fold>

    # <editor-fold desc="8) Impetigo">
    df = pd.read_csv("datasets\\Impetigo.csv")
    fig1 = px.choropleth(
        df,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='state',
        color='active cases',
        color_continuous_scale='oxy')
    fig1.update_geos(fitbounds="locations", visible=False)
    fig2 = px.pie(df, values='active cases', names='state')
    fig2.update_traces(textposition='inside', textinfo='value+label')
    st.markdown("<h6 style='color: skyblue;'></h6>", unsafe_allow_html=True)
    st.markdown("<h6 style='color: skyblue;'></h6>", unsafe_allow_html=True)
    st.header("For Disease 'Impetigo' :", anchor="8")
    col1, col2 = st.columns([6, 4])
    with col1:
        st.plotly_chart(fig1)
    with col2:
        st.plotly_chart(fig2)
    # </editor-fold>

    # <editor-fold desc="9) Pneumonia">
    df = pd.read_csv("datasets/Pneumonia.csv")
    fig1 = px.choropleth(
        df,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='state',
        color='active cases',
        color_continuous_scale='sunsetdark')
    fig1.update_geos(fitbounds="locations", visible=False)
    fig2 = px.pie(df, values='active cases', names='state')
    fig2.update_traces(textposition='inside', textinfo='value+label')
    st.markdown("<h6 style='color: skyblue;'></h6>", unsafe_allow_html=True)
    st.markdown("<h6 style='color: skyblue;'></h6>", unsafe_allow_html=True)
    st.header("For Disease 'Pneumonia' :", anchor="9")
    col1, col2 = st.columns([6, 4])
    with col1:
        st.plotly_chart(fig1)
    with col2:
        st.plotly_chart(fig2)
    # </editor-fold>

    # <editor-fold desc="10) Tuberculosis">
    df = pd.read_csv("datasets\\Tb.csv")
    fig1 = px.choropleth(
        df,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='state',
        color='active cases',
        color_continuous_scale='twilight')
    fig1.update_geos(fitbounds="locations", visible=False)
    fig2 = px.pie(df, values='active cases', names='state')
    fig2.update_traces(textposition='inside', textinfo='value+label')
    st.markdown("<h6 style='color: skyblue;'></h6>", unsafe_allow_html=True)
    st.markdown("<h6 style='color: skyblue;'></h6>", unsafe_allow_html=True)
    st.header("For Disease 'Tuberculosis' :", anchor="10")
    col1, col2 = st.columns([6, 4])
    with col1:
        st.plotly_chart(fig1)
    with col2:
        st.plotly_chart(fig2)
    # </editor-fold>

    # <editor-fold desc="11) Typhoid">
    df = pd.read_csv("datasets\\Typhoid.csv")
    fig1 = px.choropleth(
        df,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='state',
        color='active cases',
        color_continuous_scale='oranges')
    fig1.update_geos(fitbounds="locations", visible=False)
    fig2 = px.pie(df, values='active cases', names='state')
    fig2.update_traces(textposition='inside', textinfo='value+label')
    st.markdown("<h6 style='color: skyblue;'></h6>", unsafe_allow_html=True)
    st.markdown("<h6 style='color: skyblue;'></h6>", unsafe_allow_html=True)
    st.header("For Disease 'Typhoid' :", anchor="4")
    col1, col2 = st.columns([6, 4])
    with col1:
        st.plotly_chart(fig1)
    with col2:
        st.plotly_chart(fig2)
    # </editor-fold>

