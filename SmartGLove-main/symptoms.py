import streamlit as st
from vitals import model2
import pandas as pd
import locationwise

def printoutput(symp,pred,location):
    # Reading CSV
    df = pd.read_csv("datasets\\dis_detail.csv")
    st.markdown("<h1 style='text-align: center; color: yellow ;'></h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: yellow ;'></h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1,4,1])
    with col2:
        df = df.loc[df.Disease == pred]
        st.write("🤒 **Disease Diagnosed**: ", df.iloc[0, 0])
        st.write(":page_with_curl: **Description** :", df.iloc[0, 1])
        if (df.iloc[0, 2] == 1):
            switch(pred, location)
            st.write("Disease Detected is a **communicable disease** ")
            st.write("🗣️ **Method of communication** : ", df.iloc[0, 3])
        st.write("🙇 You may also experience the **symptoms**:")
        arr2 = df.iloc[0, 4].split(",")
        for i in arr2:
            if (str(i).strip() not in symp):
                st.write("->",i.strip())
        st.write(":mask: Please take the following **precautions** :")
        for i in range(4):
            if (pd.isnull(df.iloc[0, 5 + i])):
                continue
            else:
                st.write(i + 1, ") ", df.iloc[0, 5 + i])
        st.write(":calling: For more information follow the **link** : ", df.iloc[0, 9])

        if (df.iloc[0, 2] == 1):
            st.write("Please see location wise disease spread (Navbar -> Disease Spread)")
            # but2 = st.button("See Location Wise Disease Spread", key=9)
            # print(but2)
            # if not but2:
            #     locationwise.showmaps()

def switch(arg,location) :
    if arg == "AIDS":
        dff = pd.read_csv("datasets\\AIDS.csv")
        dff.loc[dff.state == location, 'active cases'] += 1
        dff.to_csv("datasets\\AIDS.csv", index=False)
    elif arg == "Chicken pox":
        dff = pd.read_csv("datasets\\Chickenpox.csv")
        dff.loc[dff.state == location, 'active cases'] += 1
        dff.to_csv("datasets\\Chickenpox.csv", index=False)
    elif arg == "Common Cold":
        dff = pd.read_csv("datasets\\Commoncold.csv")
        dff.loc[dff.state == location, 'active cases'] += 1
        dff.to_csv("datasets\\Commoncold.csv", index=False)
    elif arg == "Fungal infection":
        dff = pd.read_csv("datasets\\fungalifection.csv")
        dff.loc[dff.state == location, 'active cases'] += 1
        dff.to_csv("datasets\\fungalifection.csv", index=False)
    elif arg == "Gastroenteritis":
        dff = pd.read_csv("datasets\\Gastro.csv")
        dff.loc[dff.state == location, 'active cases'] += 1
        dff.to_csv("datasets\\Gastro.csv", index=False)
    elif arg == "GERD":
        dff = pd.read_csv("datasets\\GERD.csv")
        dff.loc[dff.state == location, 'active cases'] += 1
        dff.to_csv("datasets\\GERD.csv", index=False)
    elif arg == "hepatitis A" or arg =="Hepatitis B" or arg =="Hepatitis C" or arg =="Hepatitis D" or arg =="Hepatitis E":
        dff = pd.read_csv("datasets/Hepatitis.csv")
        dff.loc[dff.state == location, 'active cases'] += 1
        dff.to_csv("datasets\\Hepatitis.csv", index=False)
    elif arg == "Impetigo":
        dff = pd.read_csv("datasets\\Impetigo.csv")
        dff.loc[dff.state == location, 'active cases'] += 1
        dff.to_csv("datasets\\Impetigo.csv", index=False)
    elif arg == "Pneumonia":
        dff = pd.read_csv("datasets/Pneumonia.csv")
        dff.loc[dff.state == location, 'active cases'] += 1
        dff.to_csv("datasets\\Pneumonia.csv", index=False)
    elif arg == "Tuberculosis":
        dff = pd.read_csv("datasets\\Tb.csv")
        dff.loc[dff.state == location, 'active cases'] += 1
        dff.to_csv("datasets\\Tb.csv", index=False)
    elif arg == "Typhoid":
        dff = pd.read_csv("datasets\\Typhoid.csv")
        dff.loc[dff.state == location, 'active cases'] += 1
        dff.to_csv("datasets\\Typhoid.csv", index=False)

def sympredapi():
    st.markdown("<h1 style='text-align: center; color: yellow ;'></h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: yellow ;'></h1>", unsafe_allow_html=True)

    # Reading CSV
    df = pd.read_csv("datasets\\dis_detail.csv")

    # Store the initial value of widgets in session state
    if "visibility" not in st.session_state:
        st.session_state.visibility = "visible"
        st.session_state.disabled = False

    ls = ["itching",
          "skin_rash",
          "nodal_skin_eruptions",
          "continuous_sneezing",
          "shivering",
          "chills",
          "joint_pain",
          "stomach_pain",
          "acidity",
          "ulcers_on_tongue",
          "muscle_wasting",
          "vomiting",
          "burning_micturition",
          "spotting_urination",
          "fatigue",
          "weight_gain",
          "anxiety",
          "cold_hands_and_feets",
          "mood_swings",
          "weight_loss",
          "restlessness",
          "lethargy",
          "patches_in_throat",
          "irregular_sugar_level",
          "cough",
          "high_fever",
          "sunken_eyes",
          "breathlessness",
          "sweating",
          "dehydration",
          "indigestion",
          "headache",
          "yellowish_skin",
          "dark_urine",
          "nausea",
          "loss_of_appetite",
          "pain_behind_the_eyes",
          "back_pain",
          "constipation",
          "abdominal_pain",
          "diarrhoea",
          "mild_fever",
          "yellow_urine",
          "yellowing_of_eyes",
          "acute_liver_failure",
          "fluid_overload",
          "swelling_of_stomach",
          "swelled_lymph_nodes",
          "malaise",
          "blurred_and_distorted_vision",
          "phlegm",
          "throat_irritation",
          "redness_of_eyes",
          "sinus_pressure",
          "runny_nose",
          "congestion",
          "chest_pain",
          "weakness_in_limbs",
          "fast_heart_rate",
          "pain_during_bowel_movements",
          "pain_in_anal_region",
          "bloody_stool",
          "irritation_in_anus",
          "neck_pain",
          "dizziness",
          "bruising",
          "obesity",
          "swollen_legs",
          "swollen_blood_vessels",
          "puffy_face_and_eyes",
          "enlarged_thyroid",
          "brittle_nails",
          "swollen_extremeties",
          "excessive_hunger",
          "extra_marital_contacts",
          "drying_and_tingling_lips",
          "slurred_speech",
          "knee_pain",
          "hip_joint_pain",
          "muscle_weakness",
          "stiff_neck",
          "swelling_joints",
          "movement_stiffness",
          "spinning_movements",
          "loss_of_balance",
          "unsteadiness",
          "weakness_of_one_body_side",
          "loss_of_smell",
          "bladder_discomfort",
          "foul_smell_ofurine",
          "continuous_feel_of_urine",
          "passage_of_gases",
          "internal_itching",
          "toxic_look_(typhos)",
          "depression",
          "irritability",
          "muscle_pain",
          "altered_sensorium",
          "red_spots_over_body",
          "belly_pain",
          "abnormal_menstruation",
          "dischromic_patches",
          "watering_from_eyes",
          "increased_appetite",
          "polyuria",
          "family_history",
          "mucoid_sputum",
          "rusty_sputum",
          "lack_of_concentration",
          "visual_disturbances",
          "receiving_blood_transfusion",
          "receiving_unsterile_injections",
          "coma",
          "stomach_bleeding",
          "distention_of_abdomen",
          "history_of_alcohol_consumption",
          "fluid_overload",
          "blood_in_sputum",
          "prominent_veins_on_calf",
          "palpitations",
          "painful_walking",
          "pus_filled_pimples",
          "blackheads",
          "scurring",
          "skin_peeling",
          "silver_like_dusting",
          "small_dents_in_nails",
          "inflammatory_nails",
          "blister",
          "red_sore_around_nose",
          "yellow_crust_ooze",
          "prognosis",
          "None"]
    locats = [
        "Andaman & Nicobar",
        "Andhra Pradesh",
        "Arunachal Pradesh",
        "Assam",
        "Bihar",
        "Chandigarh",
        "Chhattisgarh",
        "Dadra and Nagar Haveli and Daman and Diu",
        "Delhi",
        "Goa",
        "Gujarat",
        "Haryana",
        "Himachal Pradesh",
        "Jammu & Kashmir",
        "Jharkhand",
        "Karnataka",
        "Kerala",
        "Ladakh",
        "Madhya Pradesh",
        "Maharashtra",
        "Manipur",
        "Meghalaya",
        "Mizoram",
        "Nagaland",
        "Odisha",
        "Puducherry",
        "Punjab",
        "Rajasthan",
        "Sikkim",
        "Tamil Nadu",
        "Telangana",
        "Tripura",
        "Uttarakhand",
        "Uttar Pradesh",
        "West Bengal"]

    for i in range(len(ls)):
        ls[i] = ls[i].replace('_', ' ')

    col1, col2, col3 = st.columns([1, 4, 1])
    with col2:
        location = st.selectbox(
            "Please select your location",
            locats, key=10,
            label_visibility=st.session_state.visibility,
            disabled=st.session_state.disabled, )

    st.markdown("<h1 style='text-align: center; color: yellow ;'></h1>", unsafe_allow_html=True)
    col1, col2, col3, col4, col5, col6, col7 = st.columns([.5, 4, .5, 4, .5, 4, .5])
    with col2:
        option1 = st.selectbox(
            "Enter symptom 1",
            ls, key=1,
            label_visibility=st.session_state.visibility,
            disabled=st.session_state.disabled, )
    with col4:
        option2 = st.selectbox(
            "Enter symptom 2",
            ls, key=2,
            label_visibility=st.session_state.visibility,
            disabled=st.session_state.disabled, )
    with col6:
        option3 = st.selectbox(
            "Enter symptom 3",
            ls, key=3,
            label_visibility=st.session_state.visibility,
            disabled=st.session_state.disabled, )

    but = col4.button("Submit",key=8)
    if but:
        symp = [str(option1), str(option2), str(option3)]
        for i in range(3):
            symp[i] = symp[i].replace(' ', '_')
        pred = model2.symptommodel(symp)
        pred = pred[0]
        printoutput(symp,pred,location)





