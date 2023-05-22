# -*- coding: utf-8 -*-
"""
Created on Tue May 16 13:40:10 2023

@author: Vallarasu
"""

import pickle
import streamlit as st

#loading the saved models
dth_model = pickle.load(open('H:/DTH Curn Prediction/dth_model.sav' , 'rb'))


# page title
st.set_page_config(page_title="DTH Customer Churn Prediction", page_icon=":guardsman:")
st.title('DTH Customer Churn Prediction using ML')

# getting the input data from the user
col1, col2, col3 = st.columns(3)

with col1:
    Tenure = st.number_input('Number of Days Tenured')
with col2: 
    City_Tier = st.slider('Select a city Tier ',min_value=0, max_value=3, step=1)
with col3:    
    CC_Contacted_LY = st.number_input('CC_Contacted_LY value')
    
col4, col5, col6 = st.columns(3)
with col4:
    payment1 = st.radio("Payment Method",
                        ('Debit Card','Credit Card','Cash on Delivery','E wallet','UPI'))
    if payment1== 'Debit Card':
        Payment=1        
    elif payment1== 'Credit Card':
        Payment=2
    elif payment1== 'Cash on Delivery':
        Payment=3
    elif payment1== 'E wallet':
        Payment=4
    elif payment1== 'UPI':
        Payment=5
with col5:
    gender1 = st.radio("Gender",
    ('Male','Female'))
    if gender1== 'Male':
        Gender=0        
    elif gender1== 'Female':
        Gender=1
with col6:
    Service_Score = st.slider('Select a Service_Score ',min_value=0, max_value=4, step=1)
col7, col8, col9 = st.columns(3)
with col7:
    Account_user_count = st.slider('Select a Account_user_count',min_value=0, max_value=6, step=1)
with col8:
    segment = st.radio("Account_Segment",
    ('Super','Regular Plus','HNI','Super Plus','Regular','Regular Pro','Super Pro'))
    if segment== 'Super':
        account_segment=1        
    elif segment== 'Regular Plus':
        account_segment=2
    elif segment== 'HNI':
        account_segment=3
    elif segment== 'Super Plus':
        account_segment=4
    elif segment== 'Regular':
        account_segment=5
    elif segment== 'Regular Pro':
        account_segment=6
    elif segment== 'Super Pro':
        account_segment=7
with col9:
    CC_Agent_Score = st.slider('Select a CC_Agent_Score',min_value=0, max_value=5, step=1)
col10, col11, col12 = st.columns(3)
with col10:
    marital = st.radio("Marital_Status",
    ('Single','Married','Divorced'))
    if marital== 'Single':
        Marital_Status=0        
    elif marital== 'Married':
        Marital_Status=1
    elif marital== 'Divorced':
        Marital_Status=2
with col11:
    rev_per_month = st.number_input('Rev_per_Month')
with col12: 
    complain = st.radio("Complain_Ly",
    ('0','1'))
    if complain== '0':
        Complain_ly=0        
    elif complain== '1':
        Complain_ly=1
col13, col14, col15 = st.columns(3)
with col13:
    rev_growth_yoy = st.slider('Select a Rev_Growth_yoy',min_value=10, max_value=25, step=1)
with col14:
    coupon_used_for_payment = st.slider('Select a Coupon_used_for_Payment',min_value=0, max_value=15, step=1)
with col15:
    Day_Since_CC_connect = st.slider('Select a Day_Since_CC_connect',min_value=0, max_value=20, step=1)
col16, col17 = st.columns(2)
with col16:
    cashback = st.number_input('Cashback')
with col17:
    device = st.radio("Login Device",
    ('Computer','Mobile'))
    if device == 'Computer':
        Login_device=0        
    elif device == 'Mobile':
        Login_device=1
        
# code for Prediction
dth_diagnosis = ''

# creating a button for Prediction
if st.button('DTH Customer Churn Result'):
    dth_prediction = dth_model.predict([[Tenure,City_Tier,CC_Contacted_LY,Payment,Gender,Service_Score,Account_user_count,account_segment,CC_Agent_Score,Marital_Status,rev_per_month,Complain_ly,rev_growth_yoy,coupon_used_for_payment,Day_Since_CC_connect,cashback,Login_device]])
    
    if (dth_prediction[0] == 1):
        dth_diagnosis = 'The Cutomer is Predicted to be Churned'
        st.warning(dth_diagnosis)
    elif (dth_prediction[0] == 0):
        dth_diagnosis = 'The Customer is Predicted to be Not Churned'
        st.success(dth_diagnosis)
