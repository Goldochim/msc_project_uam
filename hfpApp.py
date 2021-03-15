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
        
    tstr= st.text_input('Thalium stress Test Result Value: ')
    nmv=st.text_input('number of major vessels: ')
    rbp=st.text_input('Resting blood pressure: ')
    Age=st.text_input('Age: ')
    cp=st.text_input('Chest Pain Type: ')
    sex=st.text_input('sex: ')
    spe=st.text_input('The slope of the peak exercise ST segment: ')
    sdierr=st.text_input('ST depression induced by exercise relative to rest: ')
    rer=st.text_input('Resting Electrocardiographic Result: ')
    sc=st.text_input('serum Cholestrol: ')
    
    result=""
    if st.button("Predict"):
        result=heart_failure_Prediction(tstr, nmv,rbp, Age, cp, sex, spe, sdierr, rer, sc)
    st.success(result)
    if st.button("Prediction Note"):
        st.text("This is a thesis work for Gold Ogeyi Ochim from the Federal University of Agriculture Makurdi")

if __name__=='__main__':
    main()