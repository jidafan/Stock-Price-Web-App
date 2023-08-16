# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 16:21:33 2023

@author: ScottieDFloppyPC
"""
#Import libraries
import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App using streamlit    
""")
######################
# Input Text Box
######################

#st.sidebar.header('Enter Stock Name')
st.header('Enter Stock Name')
ticker_input = "GOOG"

#sequence = st.sidebar.text_area("Sequence input", sequence_input, height=250)
ticker = st.text_area("Stock name", ticker_input, height=5)
ticker = ticker.splitlines()
ticker = ''.join(ticker) # Concatenates list to string

st.write("""
***
""")

#Prints the stock name
st.header('Stock Name')
ticker

tickerSymbol = ticker

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='id', start="2010-7-30", end='2023-7-30')
st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume
""")
st.line_chart(tickerDf.Volume)
