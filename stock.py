import yfinance as yf
import streamlit as st

import datetime
import pandas as pd

st.write("""
# Simple Sh*t Poopy Ass
Shown are the stock **closing price** and ***volume*** of Google!
""")
Snp500=pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]
tickers=st.multiselect('Multiselect', Snp500['Symbol'])
# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol


startdate = st.date_input(label='start input',value=(datetime.date(2019,7,6)))
enddate = st.date_input(label='end input',value=(datetime.date.today()))
firstable=True
haveResult=False
for s in tickers:

    tickerDf = yf.Ticker(s).history(period='1d', start=startdate, end=enddate)
    # Open	High	Low	Close	Volume	Dividends	Stock Splits
    if firstable==True:
        outputdf = tickerDf[['Close']].rename(columns={'Close': s})
        outputdff = tickerDf[['Volume']].rename(columns={'Volume': s})
        firstable=False
    else:
        outputdf[s]=tickerDf['Close']
        outputdff[s]=tickerDf['Volume']
    haveResult=True
if haveResult:
    st.line_chart(outputdf)
    st.line_chart(outputdff)
st.balloons()
