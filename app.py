# app.py

import streamlit as st
import pandas as pd
import plotly.express as px

from data_collector import download_data
from strategy import moving_average_crossover
from backtester import backtest

st.title("Algorithmic Trading Bot")

ticker = st.text_input("Ticker Symbol", "AAPL")
start_date = st.date_input("Start Date", value=pd.to_datetime("2020-01-01"))
end_date = st.date_input("End Date", value=pd.to_datetime("2023-01-01"))

if st.button("Run Strategy"):
    data = download_data(ticker, start_date, end_date)
    st.write("### Historical Data", data.tail())
    
    strategy_data = moving_average_crossover(data)
    st.write("### Strategy Data", strategy_data.tail())
    
    backtest_data = backtest(strategy_data)
    st.write("### Backtest Data", backtest_data.tail())

    fig = px.line(backtest_data, x=backtest_data.index, y=['Close', 'Short_MA', 'Long_MA', 'Balance'],
                  labels={'value': 'Price'}, title="Strategy and Balance Over Time")
    st.plotly_chart(fig)
