import time
from datetime import datetime
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import serial.tools.list_ports

att = [[0, 0, 0]]
placeholder = st.empty()

def showcharts(att):
    fig1 = go.Figure(go.Indicator(
        mode="gauge+number",
        value=att[0][2],
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Temperature", 'font': {'size': 50}},
        gauge={
            'axis': {'range': [86, 110], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "#00563f"},
            'bgcolor': "red",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [86, 95], 'color': '#fff600'},
                {'range': [95, 99], 'color': '#ffae42'},
                {'range': [99, 104], 'color': '#ff720a'}],
        }))
    fig1.update_layout(paper_bgcolor="#f7e5f6", font={'color': "#cf43c5", 'family': "Times New Roman"})

    fig2 = go.Figure(go.Indicator(
        mode="gauge+number",
        value=att[0][0],
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
        value=att[0][1],
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
    fig3.update_layout(paper_bgcolor="#D7E3DA", font={'color': "#0c230d", 'family': "Times New Roman"})
    col1, col2, col3 = placeholder.columns([3, 3, 3])
    with col1:
        st.plotly_chart(fig1)
    with col2:
        st.plotly_chart(fig2)
    with col3:
        st.plotly_chart(fig3)

def retlist():
    st.markdown("<h1 style='text-align: center; color: #1E0922;'>Showing Live Data</h1>", unsafe_allow_html=True)
    st.markdown("<h1></h1>", unsafe_allow_html=True)
    st.markdown("<h1></h1>", unsafe_allow_html=True)
    time.sleep(2)
    ports = serial.tools.list_ports.comports()
    serialIns = serial.Serial()
    portlist = []

    for onePort in ports:
        portlist.append(str(onePort))
        print(str(portlist))

    serialIns.baudrate = 115200
    serialIns.port = 'COM7'
    serialIns.open()
    listvitals = []
    f = 62
    i = 0
    bp=[]
    temp=[]
    spo=[]
    tame=[]
    while f:
        if serialIns.in_waiting:
            packet = serialIns.readline()
            # print(packet.decode('utf-8'))
            vals = str(packet.decode('utf-8', errors='ignore'))

            lval = vals.split('x')
            lval = lval[0].strip('\r\n')
            i = (i+1)%3
            listvitals.append(lval)
            if i == 2 and f <= 60:
                    now = datetime.now()
                    att[0][0] = int(float(listvitals[0]))
                    att[0][1] = int(float(listvitals[1]))
                    att[0][2] = int(float(listvitals[2]))
                    bp.append(att[0][0])
                    spo.append(att[0][1])
                    temp.append(att[0][2])

                    current_time = now.strftime("%H:%M:%S")
                    tame.append(current_time)

                    showcharts(att)
                    time.sleep(1)
                    print(listvitals[i]," ",i)
                    listvitals.clear()
            if f==61:
                listvitals.clear()
            f -= 1

    st.markdown("<h1 style='text-align: center; color: #1E0922;'>Log Table</h1>", unsafe_allow_html=True)
    fig = go.Figure(data=[go.Table(
        columnwidth = [500,500,500,500],
        header=dict(values=['TIME','HR', 'SPO2','TEMP'], fill_color='#5ae60f', font=dict(color='black'), font_size = 20),
        cells=dict(values=[tame, bp, spo, temp], fill_color='lavender', font=dict(color='black'), font_size = 14, height=30))
        ])
    st.plotly_chart(fig, use_container_width=True)