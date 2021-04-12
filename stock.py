import yfinance as yf
import streamlit as st
import datetime

st.write("""
# Simple Sh*t Poopy Ass
Shown are the stock **closing price** and ***volume*** of Google!
""")

# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol

tickerSymbol = st.text_input('Area for textual entry')

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker

startdate = st.date_input(label='start input',value=(datetime.date(2019,7,6)))
enddate = st.date_input(label='end input',value=(datetime.date.today()))

tickerDf = tickerData.history(period='1d', start=startdate, end=enddate)
# Open	High	Low	Close	Volume	Dividends	Stock Splits
st.write("""
## Closing Price
""")
st.line_chart(tickerDf.Close)
st.write("""
## Volume Price
""")
st.line_chart(tickerDf.Volume)
st.balloons()
