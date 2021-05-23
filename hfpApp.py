"""
Created on Mon Mar 15 21:23:47 2021
@author: DELL
"""
import streamlit as st
def heart_failure_Prediction(tstr, nmv,rbp, Age, cp, sex, spe, sdierr, rer, sc):
        
    if tstr=='Normal':
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
            if cp=='Typical Angina' or cp=='Atypical Angina' or cp=='Non Angina':
                result='NO HEART FAILURE'
                print(result)
            else:
                if sex=="female":
                    if spe=='Upsloping':
                        result='NO HEART FAILURE'
                        print(result)
                    else:
                        result='WARNING!!! HEART FAILURE PREDICTED!!!'
                        print(result)
                else:
                    result='WARNING!!! HEART FAILURE PREDICTED!!!'
                    print(result)
    else:
        if cp=='Typical Angina' or cp=='Atypical Angina' or cp=='Non Angina':
            if nmv<=0:
                result='NO HEART FAILURE'
                print(result)
            else:
                if spe=='Upsloping':
                    if rer=='Normal' or rer=='Having ST Wave Abnormality':
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
                if rer=='Normal' or rer=='Having ST Wave Abnormality':
                    if sdierr<=0.3:
                        if rbp<=136:
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
    st.title("Heart Failure Predictor Using AdaBoost J48 Model")
    html_temp="""
    <div style="background-color:tomato;padding:8px">
    <h2 style="color:white;text-align:center;"> Heart Failure Predictor </h2>

    
          
            
    

          
    
    
  
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    Age=st.number_input("Age: ", 0.0, 120.0, step=1.0)
    sex = st.selectbox("Sex: ", ('male', 'female'))
    cp=st.selectbox("cp: ", ('Typical Angina', 'Atypical Angina', 'Non Angina', 'Asymptomatic') )    
    sc=st.number_input("sc: ", 0.0, 500.0, step=1.0)
    tstr= st.selectbox("tstr: ",('Normal', 'Fixed Defect', 'Reversible Defect'))
    rer=st.selectbox("rer: ", ('Normal', 'Having ST Wave Abnormality', 'Showing Probable or Definite Left Ventricular hypertrophy by Estes Criteria'))
    nmv=st.number_input("nmv: ",0.0, 3.0, step=1.0)
    rbp=st.number_input("rbp: ", 0.0, 200.0, step=1.0)        
    spe=st.selectbox("spe: ",('Upsloping', 'Flat', 'Downsloping'))
    sdierr=st.number_input("sdierr: ", 0.0, 6.2, step=0.1)
    
    
    
    result=""
    if st.button("Predict"):
        result=heart_failure_Prediction(tstr, nmv, rbp, Age, cp, sex, spe, sdierr, rer, sc)
    st.success(result)
    if st.button("Prediction Note"):
        st.text("This is a thesis work for Gold Ogeyi Ochim from the Federal University of Agriculture Makurdi")
    if st.button("Guide"):
        st.text("Chest pain type: 1-Typical angina, 2-Atypical anginal, 3-Non anginal, 4-Asymptomatic")
        st.text("Thalium stress Test Result Value: 3-Normal, 6-fixed defect, 7-Reversible defect" )
        st.text("Resting Electrocardiographic Result:  0-Normal, 1-Having ST Wave Abnormality, 2-Showing Probable or definite left ventricular hypertrophy by Estes' criteria")
        st.text("Number of major vessels: 0-3")
        st.text("Resting blood pressure: 0-200 ")
        st.text("The slope of the peak exercise ST segment: 1-Upslopping, 2- Flat, 3-Down slopping")
        st.text("ST depression induced by exercise relative to rest: 0-6.2")       
        
        
if __name__=='__main__':
    main()
