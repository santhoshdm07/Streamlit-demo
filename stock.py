# import streamlit as st
# import yfinance as yf

# st.title("Stock Price Analyser")

# ticker_data = yf.Ticker("PYPL")

# ticker_df = ticker_data.history(period = "1d", start = "2023-10-01", end = "2024-10-01")

# st.write("Here is the raw day wise stock prices")

# st.dataframe(ticker_df)





import streamlit as st
import yfinance as yf

st.title("Stock Price Analyser")

# Define the ticker symbol
ticker_symbol = "MSFT"

# Fetch stock data from Yahoo Finance
ticker_data = yf.Ticker(ticker_symbol)

# Get historical data
ticker_df = ticker_data.history(period="1d", start="2023-10-01", end="2024-10-01")

# Check if data is empty
if ticker_df.empty:
    st.write(f"No data found for {ticker_symbol}. Please check the symbol or the date range.")
else:
    st.write(f"Here is the raw day-wise stock prices for {ticker_symbol}")
    st.dataframe(ticker_df)
