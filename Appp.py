# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 12:51:35 2020

@author: DELL
"""
import streamlit as st
import pickle

pickle_in=open('clf_D.pkl', 'rb')
clf=pickle.load(pickle_in)

def welcome():
    return "Welcome All"

def Job1_via_NYSC_Prediction(Gender, Course, School_Type,Qualification, Job_Search_Mode):
    prediction=clf.predict(['gender', 'course', 'Uni_Poly_Type', 'qualification', 'job_search_mode'])
    print(prediction)
    return 'The prediction value is '+str(prediction)

def main():
    st.title("Graduates First Job Predictor")
    html_temp="""
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Employment via NYSC or Not</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    Gender=st.text_input("Gender", "Type here")
    Course=st.text_input("Course", "Type here")
    School_Type=st.text_input("School", "Type here")
    Qualification=st.text_input("Qualification", "Type here")
    Job_Search_Mode=st.text_input("Job Search Mode", "Type here")
    result=""
    if st.button("Predict"):
        result=Job1_via_NYSC_Prediction(Gender, Course, School_Type, Qualification, Job_Search_Mode)
    st.success('Your job Prediction is {}'.format(result))
    if st.button("Prediction Note"):
        st.text("0-No job via NYSC, 1=Yes, you get a job via NYSC")
        
if __name__ == '__main__':
    from os import environ
    app.run(debug=False, port=environ.get("PORT", 5000))
