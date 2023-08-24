import streamlit as st
st.set_page_config(page_title="Project_Cerberus", page_icon=":bar_chart:", layout="wide")
import streamlit_authenticator as stauth
import yaml
from yaml import SafeLoader
import dashboard
import symptoms
import locationwise
import getlist


hide_streamlit_style = """
                <style>
                footer {visibility: hidden;}
                </style>
                """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.markdown("""<style> 
                    .header-font { font-size:80px !important; }
                    .subheader-font { font-size:45px !important; }
                    .midheader-font { font-size:40px !important; }
                    .divheading-font { font-size:35px !important; }
                    .smallheader-font { font-size:25px !important; } 
        </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: yellow ;'></h1>", unsafe_allow_html=True)
col1, col2, col3, col4, col5 = st.columns([1, 2, 1, 6, 1])
from PIL import Image
image = Image.open('img/team_logo.png')
with col2:
    st.image(image, width=300 )
with col4:
    st.markdown('<p class="header-font" style="text-align: center; color: #2A0816 !important;">Project Cerberus</p>', unsafe_allow_html=True)
    st.markdown(
        '<p class="subheader-font" style="text-align: center; color: lightblue !important;">Your Personal Healthcare Assistant</p>',
        unsafe_allow_html=True)

# # --- USER AUTHENTICATION ---
# load hashed passwords
with open('auth\\config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")

if authentication_status:
    authenticator.logout("Logout", "sidebar")
    st.sidebar.image("img/hm_nvbar.jpg",width = 150)
    st.sidebar.title(f"Welcome {name}")


    def homedisp() :


        st.markdown("<h1></h1>", unsafe_allow_html=True)
        st.markdown("<h1></h1>", unsafe_allow_html=True)
        col1, col2, col3, col4 = st.columns([1, 3, 3, 1])
        with col2:
            st.markdown('<p class="midheader-font" style="text-align: left; color: #1E0922;">Our Motto:</p>',
                        unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 3, 1])
        with col2:
            st.markdown(
                '<p class="divheading-font" style="text-align: left; color: #1E0922;">Evolving Digital Healthcare Together</p>',
                unsafe_allow_html=True)


        st.markdown("<h1></h1>", unsafe_allow_html=True)
        st.markdown("<h1></h1>", unsafe_allow_html=True)
        col1, col2, col3, col4 = st.columns([1,3,3,1])
        with col2:
            st.markdown( '<p class="midheader-font" style="text-align: left; color: #1E0922;">Our Solutions:</p>',unsafe_allow_html=True)

        st.markdown("<h1></h1>", unsafe_allow_html=True)
        image = Image.open('img/live_analysis.jpg')
        col1, col2, col3, col4, col5 = st.columns([.8, 3, 0.5, 3, .8])
        with col2:
            st.markdown('<p class="divheading-font" style="text-align: left; color: #1E0922;">Live Vital Analysis</p>',
                        unsafe_allow_html=True)
            st.markdown(
                "<p class='smallheader-font' style='text-align: left; color: #1E0922;'> We are working towards the "
                "digital transformation of healthcare diagnosis with our state of the art expert hardware software "
                "combination. This expert system let's you monitor your vitals at your ease</p>",
                unsafe_allow_html=True)
            # sol1 = st.button("Explore more", key=1)
            # # if sol1:
        with col4:
            st.image(image)

        st.markdown("<h1></h1>", unsafe_allow_html=True)
        st.markdown("<h1></h1>", unsafe_allow_html=True)
        image = Image.open('img/hs_pred.jpg')
        col1, col2, col3, col4, col5 = st.columns([.8, 3, 0.5, 3, .8])
        with col4:
            st.markdown('<p class="divheading-font" style="text-align: left; color: #1E0922;">Health Score Prediction</p>',
                        unsafe_allow_html=True)
            st.markdown(
                "<p class='smallheader-font' style='text-align: left; color: #1E0922;'>Our innovative product allows you to achieve good health by marking your health on a marking scale, thus providing a vastly superior measure of understanding the level of your health .</p>",
                unsafe_allow_html=True)
            # sol2 = st.button("Explore more", key=2)
            # if sol2:
            #     rad = "Dashboard"
            #     # goto .labelcust
        with col2:
            st.image(image,width =490)

        st.markdown("<h1></h1>", unsafe_allow_html=True)
        st.markdown("<h1></h1>", unsafe_allow_html=True)
        image = Image.open('img/ds_pred.jpg')
        col1, col2, col3, col4, col5 = st.columns([.8, 3, 0.5, 3, .8])
        with col2:
            st.markdown(
                '<p class="divheading-font" style="text-align: left; color: #1E0922;">Disease Analysis using Symptoms</p>',
                unsafe_allow_html=True)
            st.markdown(
                "<p class='smallheader-font' style='text-align: left; color: #1E0922;'> Our software allows you to enter your symptoms and get a prediction of what disease you may be suffering from.</p>",
                unsafe_allow_html=True)
            # sol3 = st.button("Explore more", key=3)
            # if sol2:
            #     rad = "Dashboard"
            #     # goto.labelcust
        with col4:
            st.image(image, width=490)

        st.markdown("<h1></h1>", unsafe_allow_html=True)
        st.markdown("<h1></h1>", unsafe_allow_html=True)
        image = Image.open('img/locatdist.jpg')
        col1, col2, col3, col4, col5 = st.columns([.8, 3, 0.5, 3, .8])
        with col4:
            st.markdown(
                '<p class="divheading-font" style="text-align: left; color: #1E0922;">Disease Hotspots</p>',
                unsafe_allow_html=True)
            st.markdown(
                "<p class='smallheader-font' style='text-align: left; color: #1E0922;'> Our database shows communicable diseases and potential hotspots according to state data</p>",
                unsafe_allow_html=True)
            # sol4 = st.button("Explore more", key=4)
            # if sol2:
            #     rad = "Dashboard"
            #     # goto.labelcust
        with col2:
            st.image(image, width=490)

    rad = st.sidebar.radio("Navigation", ["Home", "Live Vital Analysis", "Dashboard", "Symptom Analysis","Disease Hotspots"])

    # label .labelcust
    if rad == "Home":
        homedisp()
    if rad == "Live Vital Analysis":
        getlist.retlist()
    if rad == "Dashboard":
        dashboard.dsh()
    if rad == "Symptom Analysis":
        symptoms.sympredapi()
    if rad == "Disease Hotspots":
        locationwise.showmaps()


