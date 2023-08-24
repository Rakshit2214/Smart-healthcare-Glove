from datetime import time
from time import *
import plotly.graph_objects as go
import streamlit as st
from vitals import model1
import time
import mcutopy

def vitaldsh(att):

    fig1 = go.Figure(go.Indicator(
        mode="gauge+number",
        value=att[0][0],
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Temperature", 'font': {'size': 50}},
        gauge={
            'axis': {'range': [80, 110], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "#00563f"},
            'bgcolor': "red",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [80, 95], 'color': '#fff600'},
                {'range': [95, 99], 'color': '#ffae42'},
                {'range': [99, 104], 'color': '#ff720a'}],
            }))
    fig1.update_layout(paper_bgcolor="#f7e5f6", font={'color': "#cf43c5", 'family': "Times New Roman"})

    fig2 = go.Figure(go.Indicator(
        mode="gauge+number",
        value=att[0][1],
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Heart Rate", 'font': {'size': 50}},
        gauge={
            'axis': {'range': [0, 220], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "#7cfc00"},
            'bgcolor': "#03045e",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 60], 'color': '#caf0f8'},
                {'range': [60, 100], 'color': '#00b4d8'},
                {'range': [100, 160], 'color': '#0077b6'}],
        }))
    fig2.update_layout(paper_bgcolor="#f9f8df", font={'color': "#5e5c12", 'family': "Times New Roman"})

    fig3 = go.Figure(go.Indicator(
        mode="gauge+number",
        value=att[0][2],
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Respiratory Rate", 'font': {'size': 50}},
        gauge={
            'axis': {'range': [0, 40], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "#ffffed"},
            'bgcolor': "#62021e",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 12], 'color': '#c5558e'},
                {'range': [12, 20], 'color': '#a42153'}],
        }))
    fig3.update_layout(paper_bgcolor="#a1d1b5", font={'color': "#061208", 'family': "Times New Roman"})

    fig4 = go.Figure(go.Indicator(
        mode="gauge+number",
        value=att[0][3],
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "BP systolic", 'font': {'size': 50}},
        gauge={
            'axis': {'range': [40, 180], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "#f5fcff"},
            'bgcolor': "#ddddc7",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [40, 90], 'color': '#3d065a'},
                {'range': [90, 120], 'color': '#b51a62'},
                {'range': [120, 140], 'color': '#70d4b4'}],
        }))
    fig4.update_layout(paper_bgcolor="#FAE6E3", font={'color': "#5E0034", 'family': "Times New Roman"})

    fig5 = go.Figure(go.Indicator(
        mode="gauge+number",
        value=att[0][4],
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "BP diastolic", 'font': {'size': 50}},
        gauge={
            'axis': {'range': [0, 120], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "#FAB73D"},
            'bgcolor': "#D2F2D4",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 60], 'color': '#0C230D'},
                {'range': [60, 80], 'color': '#256A28'},
                {'range': [80, 90], 'color': '#3DB042'}],
        }))
    fig5.update_layout(paper_bgcolor="#dbf3fa", font={'color': "darkblue", 'family': "Times New Roman"})

    fig6 = go.Figure(go.Indicator(
        mode="gauge+number",
        value=att[0][5],
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Sp02", 'font': {'size': 50}},
        gauge={
            'axis': {'range': [80, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "#F5F5DD"},
            'bgcolor': "#EEEB62",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [80, 95], 'color': '#9A650D'}],
        }))
    fig6.update_layout(paper_bgcolor="#D7E3DA", font={'color': "#0c230d", 'family': "Times New Roman"})

    st.markdown("<h1 style='text-align: center; color: yellow ;'></h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: yellow ;'></h1>", unsafe_allow_html=True)
    col1, col2, col3, col4, col5, col6, col7 = st.columns([.5, 4, .5, 4, .5, 4, .5])
    with col2:
        st.plotly_chart(fig1)
    with col4:
        st.plotly_chart(fig2)
    with col6:
        st.plotly_chart(fig3)
    col1, col2, col3, col4, col5, col6, col7 = st.columns([.5, 4, .5, 4, .5, 4, .5])
    with col2:
        st.plotly_chart(fig4)
    with col4:
        st.plotly_chart(fig5)
    with col6:
        st.plotly_chart(fig6)
    st.markdown("<h1 style='text-align: center; color: yellow ;'></h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: yellow ;'></h1>", unsafe_allow_html=True)
    num = model1.vitalmodel(att)
    # my_bar = st.progress(0)
    # for percent_complete in range(100):
    #     time.sleep(0.1)
    #     my_bar.progress(percent_complete + 2)
    if num == 3:
        st.markdown("<h1 style='text-align: center; color: green ;'>You are very healthy 😁</h1>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center; color: green ;'>Your health score is excellent, there is no need to worry </h3>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center; color: green ;'>Health Score : 3 / 3</h1>",unsafe_allow_html=True)
    elif num == 2:
        st.markdown("<h1 style='text-align: center; color: #f5661b ;'>You have average health 😕</h1>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center; color: #f5661b ;'>Your health score is not very good, Recommended Symptom Analysis </h3>",
            unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center; color: #f5661b ;'>Health Score : 2 / 3</h1>",unsafe_allow_html=True)
    elif num == 1:
        st.markdown("<h1 style='text-align: center; color: #ec5019 ;'>You have poor health 🙁</h1>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center; color: #ec5019 ;'>Your health score is bad, Strongly recommend Symptom Analysis</h3>",
            unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center; color: #ec5019 ;'>Health Score : 1 / 3</h1>",unsafe_allow_html=True)
    elif num == 0:
        st.markdown("<h1 style='text-align: center; color: red ;'>You have very poor health ☹️</h1>",unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: center; color: red ;'>Your health score is very bad, Strongly recommend Symptom Analysis </h3>",
            unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center; color: red ;'>Health Score : 0 / 3</h1>",unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1,4,1])
    with col2:
        st.markdown("<h1 style='text-align: center; color: yellow ;'></h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center; color: yellow ;'></h1>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align: left; color: black ;'>Detailed Report :</h3>",unsafe_allow_html=True)

        st.write("**Temperature** : ", att[0][0], "°F")
        if att[0][0] <= 95:
            st.write("Very low temperature, You may experience hypothermia")
        elif 99 >= att[0][0] > 95:
            st.write("Ideal temperature, You have a normal body temperature ")
        elif 104 >= att[0][0] > 99:
            st.write("High temperature, You have high fever")
        elif att[0][0] > 104:
            st.write("Extremely High temperature, You may experience hyperpyrexia, Consult a doctor immideately")

        st.write("**Heart Rate** : ", att[0][1], " bpm")
        if att[0][1] <= 60:
            st.write("Generally low Heart Rate, if heart rate is continuously less than 60 bpm you may have "
                     "bradycardia, please consult a doctor")
        elif 100 >= att[0][1] > 60:
            st.write("Ideal Heart Rate, You have a normal Heart Rate ")
        elif 160 >= att[0][1] > 100:
            st.write("Generally high Heart Rate, if you are not exercising and if heart rate is continuously more "
                     "than 100 bpm please consult a doctor")
        elif att[0][1] > 160:
            st.write("Extremely High Heart Rate, You may have tachycardia, Consult a doctor immediately")

        st.write("**Respiratory Rate** : ", att[0][2], " breaths per minute")
        if att[0][2] <= 12:
            st.write("Very low Respiratory Rate, You may have bradypnea, consult a doctor immediately")
        elif 20 >= att[0][2] > 12:
            st.write("Ideal Respiratory Rate, You have a normal Respiratory temperature ")
        elif att[0][2] > 20:
            st.write("Very high Respiratory Rate, You may have tachypnea, consult a doctor immediately")

        st.write("**BP Systolic** : ", att[0][3], " Hz")
        if att[0][3] <= 90:
            st.write("Very Low BP, You may experience hypotension, immediately consult a doctor")
        elif 120 >= att[0][3] > 90:
            st.write("Ideal BP, You Blood Pressure is normal")
        elif 140 >= att[0][3] > 120:
            st.write("High BP, You have pre-hypertension, recommended to consult a doctor")
        elif att[0][3] > 140:
            st.write("Very High BP, You have hypertension, consult a doctor immediately")

        st.write("**BP Diastolic** : ", att[0][4], " Hz")
        if att[0][4] <= 60:
            st.write("Very Low BP, You may experience hypotension, immediately consult a doctor")
        elif 80 >= att[0][4] > 60:
            st.write("Ideal BP, You Blood Pressure is normal")
        elif 90 >= att[0][4] > 80:
            st.write("High BP, You have pre-hypertension, recommended to consult a doctor")
        elif att[0][4] > 90:
            st.write("Very High BP, You have hypertension, consult a doctor immediately")

        st.write("**Oxygen Level** : ", att[0][5], "%")
        if att[0][5] <= 95:
            st.write("Low blood oxygen, consult a doctor immediately")
        else:
            st.write("Ideal blood oxygen, You have no reason to worry")

def dsh():
    att = [[0, 0, 0, 0, 0, 0]]
    st.markdown("<h1></h1>", unsafe_allow_html=True)
    st.markdown("<h1></h1>", unsafe_allow_html=True)
    col1, col2, col3, col4, col5 = st.columns([.8, 3, 0.5, 3, .8])
    with col2:
        but1 = st.button("Give Custom input(For non hardware integrated parameters)")
    with col4:
        but2 = st.button("Take Sample input(For non hardware integrated parameters)")
    st.markdown("<h1></h1>", unsafe_allow_html=True)
    st.markdown("<h1></h1>", unsafe_allow_html=True)
    if but1:
        bpsys = st.number_input('Enter BP Systolic : ', min_value=60, max_value=240, value=120, step=1)
        bpdias = st.number_input('Enter BP Diastolic : ', min_value=20, max_value=100, value=80, step=1)
        respr = st.number_input('Enter BP Systolic : ', min_value=10, max_value=25, value=17, step=1)
        # bpsys = st.number_input('Enter BP Systolic : ')
        # bpdias = st.number_input('Enter BP Diastolic : ')
        # respr = st.number_input('Enter Respiration Rate : ')
        att[0][2] = respr
        att[0][3] = bpsys
        att[0][4] = bpdias
        with col2:
            with st.spinner('Reading Vitals...'):
                att = mcutopy.takeinput(att)
                st.success('Values Read successfully!')
        vitaldsh(att)
    if but2:
        att[0][2] = 17
        att[0][3] = 115
        att[0][4] = 78
        col1, col2, col3 = st.columns([3, 3, 3])
        with col2:
            with st.spinner('Reading Vitals...'):
                att = mcutopy.takeinput(att)
                st.success('Values Read successfully!')
        vitaldsh(att)


    # col1, col2, col3= st.columns([3, 3, 3])
    # from PIL import Image
    # image = Image.open('img/robotic_hand.jpg')
    # with col3:
    #     st.image(image, width=50)
    # with col2:
    #


