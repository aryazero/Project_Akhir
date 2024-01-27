# -*- coding: utf-8 -*-

import pickle
import streamlit as st

model = pickle.load(open('diabetes_model.sav', 'rb'))

st.title('Prediksi Diabetes \n Arya Ramdhan Dwi Cahya 210040203')

Pregnancies = st.text_input ('Jumlah kehamilan')

Glucose = st.text_input ('Kadar Gula darah (mg/dL)')

BloodPressure = st.text_input ('Tekanan darah (mmHg)')

SkinThickness = st.text_input ('Tebal Kulit')

Insulin = st.text_input ('Kadar Insulin (mmol/L)')

BMI = st.text_input ('Input nilai BMI')

DiabetesPredigreeFunction = st.text_input ('Input Nilai DPF')

Age = st.text_input ('Input Usia')

diab_diagnosis = ''

if st.button('Prediksi Diabetes') :
    diab_prediction = model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPredigreeFunction, Age]])

    if(diab_prediction[0] == 1):
        diab_diagnosis = 'Pasien terkena Diabet'
    else :
        diab_diagnosis = 'Pasien tidak terkena Diabet'
    
    st.success(diab_diagnosis)

