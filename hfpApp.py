# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 21:23:47 2021

@author: DELL
"""

import streamlit as st


def heart_failure_Prediction(tstr, nmv,rbp, Age, cp, sex, spe, sdierr, rer, sc):
        
    if tstr<=3:
        if nmv<=0:
            if rbp<=156:
                result='NO HEART FAILURE'
                print(result)
            else:
                if Age<=62:
                    result='WARNING!!! HEART FAILURE PREDICTED!!!'
                    print(result)
                else:
                    result='NO HEART FAILURE'
                    print(result)
        else:
            if cp<=3:
                result='NO HEART FAILURE'
                print(result)
            else:
                if sex<=0:
                    if spe<=1:
                        result='NO HEART FAILURE'
                        print(result)
                    else:
                        result='WARNING!!! HEART FAILURE PREDICTED!!!'
                        print(result)
                else:
                    result='WARNING!!! HEART FAILURE PREDICTED!!!'
                    print(result)
    else:
        if cp<=3:
            if nmv<=0:
                result='NO HEART FAILURE'
                print(result)
            else:
                if spe<=1:
                    if rer<=1:
                        result='NO HEART FAILURE'
                        print(result)
                    else:
                        result='WARNING!!! HEART FAILURE PREDICTED!!!'
                        print(result)
                else:
                    result='WARNING!!! HEART FAILURE PREDICTED!!!'
                    print(result)
        else:
            if sdierr<=0.5:
                if rer<=1:
                    if sdierr<=0.3:
                        if rer<=136:
                            if sc<=233:
                                result='NO HEART FAILURE'
                                print(result)
                            else:
                                result='WARNING!!! HEART FAILURE PREDICTED!!!'
                                print(result)
                        else:
                            result='WARNING!!! HEART FAILURE PREDICTED!!!'
                            print(result)
                    else:
                        result='NO HEART FAILURE'
                        print(result)
                else:
                    result='WARNING!!! HEART FAILURE PREDICTED!!!'
                    print(result)
            else:
                result='WARNING!!! HEART FAILURE PREDICTED!!!'
                print(result)
                
    return result

def main():
    st.title("Heart Failure Predictor")
    html_temp="""
    <div style="background-color:tomato;padding:8px">
    <h2 style="color:white;text-align:center;"> Heart Failure Predictor </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    Age=st.number_input("Age: ")
    sex=st.number_input('Sex: ', "1-Male, 0=Female")
    cp=st.number_input('Chest Pain Type: ',"1-Typical angina, 2-Atypical anginal, 3-Non anginal, 4-Asymptomatic" )
    sc=st.number_input('Serum Cholestrol: ')
    tstr= st.number_input('Thalium stress Test Result Value: ',"3-Normal, 6-fixed defect, 7-Reversible defect" )
    rer=st.number_input('Resting Electrocardiographic Result: ', "0-Normal, 1-having ST-Wave abnormality, 2-showing probable or definite left ventricular hypertrophy by Estes' criteria")
    nmv=st.number_input('Number of major vessels: ',"0-3")
    rbp=st.number_input('Resting blood pressure: ')        
    spe=st.number_input('The slope of the peak exercise ST segment: ',"1-Upslopping, 2- Flat, 3-Down slopping")
    sdierr=st.number_input('ST depression induced by exercise relative to rest: ', "0-6.2")
    
    
    
    result=""
    if st.button("Predict"):
        result=heart_failure_Prediction(tstr, nmv, rbp, Age, cp, sex, spe, sdierr, rer, sc)
    st.success(result)
    if st.button("Prediction Note"):
        st.text("This is a thesis work for Gold Ogeyi Ochim from the Federal University of Agriculture Makurdi")

if __name__=='__main__':
    main()
