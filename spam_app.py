# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 19:30:04 2022

@author: tamil
"""

import streamlit as st
#from utils import PrepProcessor , columns

import numpy as np
import pandas as pd

import joblib

model = joblib.load('spam_project')

st.title('📩 EMAIL SPAM PREDICTION 📩')
message = st.text_input('ENTER THE MESSAGE')

def predict_spam():
     rows = np.array([message])
     prediction = model.predict(rows)

     if prediction[0] == 0:
         st.success('YOUR EMAIL IS NOT SPAM 😄')
     elif prediction[0] == 1:
         st.error('YOUR EMAIL IS A SPAM 🚨')

st.button('PREDICT',on_click = predict_spam)
