# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt

# At the top of app.py
import pandas as pd

# Load historical data
df2 = pd.read_csv("/content/drive/MyDrive/Data Science/Projects/P579 Oil price prediction/Crude oil.csv")  # or Excel
# Make sure it has columns: 'High', 'Low', 'Close/Last'
st.session_state.df2 = df2

# Load the dumped exponential model
@st.cache_resource
def load_model():
    return joblib.load('/content/exp_model_log_high_low.pkl')  # Replace with your dumped model filename

model = load_model()

st.title("Close/Last Prediction & Forecast Using Exponential Model")

# --- Step 1: Single Prediction ---
st.subheader("Predict Close/Last for a Given High & Low")
high_input = st.number_input("Enter High value:", min_value=0.0, value=100.0)
low_input = st.number_input("Enter Low value:", min_value=0.0, value=80.0)

if st.button("Predict Close Price"):
    # Prepare dataframe for prediction
    df_single = pd.DataFrame({'High':[high_input], 'Low':[low_input]})
    df_single['LogHigh'] = np.log(df_single['High'])
    df_single['LogLow'] = np.log(df_single['Low'])
    
    predicted_close = np.exp(model.predict(df_single[['LogHigh','LogLow']]))[0]
    st.markdown(
        f"""
        <div style="
            background-color: #d4edda; 
            color: #155724; 
            padding: 15px; 
            border-radius: 5px; 
            border: 1px solid #c3e6cb;
            font-size: 20px;
            font-weight: bold;">
            Predicted Close/Last: {predicted_close:.2f}
        </div>
        """, 
        unsafe_allow_html=True
    )


# --- Step 2: Forecast for N periods ---
st.subheader("Forecast Close/Last for Next N Months")
n_months = st.number_input("Enter number of months to forecast:", min_value=1, max_value=120, value=12)

if st.button("Show Forecast"):
    # Use historical High & Low from df2 (assumes df2 exists in your session)
    if 'df2' not in st.session_state:
        st.error("Historical data not loaded in session. Please load df2.")
    else:
        df_hist = st.session_state.df2[['High','Low']].copy()
        df_hist = df_hist.tail(n_months).reset_index(drop=True)  # Use last N months
        
        # Log-transform
        df_hist['LogHigh'] = np.log(df_hist['High'])
        df_hist['LogLow'] = np.log(df_hist['Low'])
        
        # Predict Close
        df_hist['Predicted_Close'] = np.exp(model.predict(df_hist[['LogHigh','LogLow']]))
        
        # Display forecast table
        st.subheader("Forecasted Close/Last for Next Months")
        df_display = df_hist[['High','Low','Predicted_Close']].copy()
        df_display.index = [f"Month {i+1}" for i in range(len(df_display))]
        st.dataframe(df_display)
        
        # Plot forecast
        st.subheader("Forecast Plot")
        plt.figure(figsize=(10,5))
        plt.plot(df_display.index, df_display['Predicted_Close'], marker='o', color='blue', label='Predicted Close')
        plt.title("Forecasted Close/Last")
        plt.xlabel("Month")
        plt.ylabel("Close/Last")
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.legend()
        st.pyplot(plt)
        plt.clf()


