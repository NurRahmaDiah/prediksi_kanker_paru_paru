import pickle
import streamlit  as st

model = pickle.load(open('prediksi_kanker.sav', 'rb'))

st.title('APLIKASI PREDIKSI KANKER PARU-PARU')

GENDER = st.selectbox('KELAMIN : ',["PRIA", "WANITA"])
if GENDER == "PRIA" : 
    GENDER = 1 
else : 
    GENDER = 2
AGE = st.number_input('USIA :')

SMOKING = st.selectbox('MEROKOK :',["Tidak", "Ya"])
if SMOKING == "Ya" : 
    SMOKING = 1 
else : 
    SMOKING = 2
YELLOW_FINGERS = st.selectbox('PENYAKIT KUNING : ',["Tidak", "Ya"])
if YELLOW_FINGERS == "Ya" : 
    YELLOW_FINGERS = 1 
else : 
    YELLOW_FINGERS = 2
ANXIETY = st.selectbox('ANXIETY: ',["Tidak", "Ya"])
if ANXIETY == "Ya" : 
    ANXIETY = 1 
else : 
    ANXIETY = 2
PEER_PRESSURE = st.selectbox('PEER PRESSURE: ',["Tidak", "Ya"])
if PEER_PRESSURE == "Ya" : 
    PEER_PRESSURE = 1 
else : 
    PEER_PRESSURE = 2
CHRONIC_DISEASE = st.selectbox('CHRONIC DISEASE: ',["Tidak", "Ya"])
if CHRONIC_DISEASE == "Ya" : 
    CHRONIC_DISEASE = 1 
else : 
    CHRONIC_DISEASE = 2
FATIGUE = st.selectbox('FATIGUE: ',["Tidak", "Ya"])
if FATIGUE == "Ya" : 
    FATIGUE = 1 
else : 
    FATIGUE = 2
ALLERGY = st.selectbox('ALLERGY: ',["Tidak", "Ya"])
if ALLERGY == "Ya" : 
    ALLERGY = 1 
else : 
    ALLERGY = 2
WHEEZING = st.selectbox('WHEEZING: ',["Tidak", "Ya"])
if WHEEZING == "Ya" : 
    WHEEZING = 1 
else : 
    WHEEZING = 2
ALCOHOL_CONSUMING = st.selectbox('ALCOHOL_CONSUMING: ',["Tidak", "Ya"])
if ALCOHOL_CONSUMING == "Ya" : 
    ALCOHOL_CONSUMING = 1 
else : 
    ALCOHOL_CONSUMING = 2
COUGHING = st.selectbox('COUGHING: ',["Tidak", "Ya"])
if COUGHING == "Ya" : 
    COUGHING = 1 
else : 
    COUGHING = 2
SHORTNESS_OF_BREATH = st.selectbox('SHORTNESS_OF_BREATH: ',["Tidak", "Ya"])
if SHORTNESS_OF_BREATH == "Ya" : 
    SHORTNESS_OF_BREATH = 1 
else : 
    SHORTNESS_OF_BREATH = 2
SWALLOWING_DIFFICULTY = st.selectbox('SWALLOWING_DIFFICULTY: ',["Tidak", "Ya"])
if SWALLOWING_DIFFICULTY == "Ya" : 
    SWALLOWING_DIFFICULTY = 1 
else : 
    SWALLOWING_DIFFICULTY = 2
CHEST_PAIN = st.selectbox('CHEST_PAIN : ',["Tidak", "Ya"])
if CHEST_PAIN == "Ya" : 
    CHEST_PAIN = 1 
else : 
    CHEST_PAIN = 2
predict = ''

if st.button('Prediksi'):
    predict = model.predict (
        [[GENDER,AGE,SMOKING,YELLOW_FINGERS,ANXIETY,PEER_PRESSURE,CHRONIC_DISEASE,FATIGUE,ALLERGY,WHEEZING,ALCOHOL_CONSUMING,COUGHING,SHORTNESS_OF_BREATH,SWALLOWING_DIFFICULTY,CHEST_PAIN]]
    )
    if predict[0] == 1:
         st.warning("Pasien memiliki kemungkinan besar untuk mengidap Kanker Paru-Paru")
    else:
        st.success("Pasien tidak memiliki kemungkinan untuk mengidap Kanker Paru-Paru")