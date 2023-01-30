import streamlit as st
import yfinance as yf
import plotly.express as pe
import pandas as pd
import datetime
import time
from stocknews import StockNews

st.title('Stock Information Dashboard')
st.info('This app is used to display information on a stock. You can gather more information on a stock by selecting their symbol, start date, and end date. \
More information is displayed in the tabs Stock Company Info, Stock Data, and Stock News.')
st.sidebar.header('Stock Selection')
# Going to use webscraping to do this part
ticker_list = pd.read_csv('ticker.csv')
ticker = st.sidebar.selectbox('Ticker', ticker_list )
start_date = st.sidebar.date_input('Start Date', datetime.date(2022, 1, 1))
end_date = st.sidebar.date_input('End Date')
st.sidebar.info('Please select a stock ticker symbol from the dropdown menu and the start and end date to get information on the stock.')
ticker_symbol = yf.Ticker(ticker)
ticker_df = ticker_symbol.history(period='1d', start=start_date, end=end_date)

stock_info, ticker_data, news = st.tabs(['Stock Company Info', 'Stock Data', 'Stock News'])

with stock_info:
    string_name = ticker_symbol.info['longName']
    st.header(string_name)
    string_summary = ticker_symbol.info['longBusinessSummary']
    st.info(string_summary)

with ticker_data:
    data = yf.download(ticker, start=start_date, end=end_date)
    line_chart = pe.line(data, x = data.index, y = data['Adj Close'], title = ticker)
    st.plotly_chart(line_chart)
    st.header('Ticker Data')
    st.write(ticker_df)

    # Seperator
    st.write('---------------------------------------')
    
    st.info("If you want to see more info expand the tabs below")
    with st.expander("Financial Statements"):
        balance_sheet = ticker_symbol.balance_sheet
        income_statement = ticker_symbol.income_stmt
        cash_flow = ticker_symbol.cashflow
        st.header('Yearly Balance Sheet')
        st.write(balance_sheet)
        st.header('Yearly Income Statement')
        st.write(income_statement)
        st.header('Yearly Cash Flow Statement')
        st.write(cash_flow)

    with st.expander("Earnings Report"):
        earnings = ticker_symbol.earnings
        qrtly_earnings = ticker_symbol.quarterly_earnings
        st.header('Yearly Earnings')
        st.write(earnings)
        st.header('Quarterly Earnings')
        st.write(qrtly_earnings)

with news:
    st.header(f'News of {ticker}')
    stock_news = StockNews(ticker, save_news=False)
    df_news = stock_news.read_rss()
    for i in range(5):
        articles = st.subheader(f'Articles {i+1}')
        st.write(df_news['published'][i])
        st.write(df_news['title'][i])
        st.write(df_news['summary'][i])





    



