
import streamlit as st
import duckdb
import pandas as pd
import plotly.graph_objects as go


st.set_page_config(page_title="📊 Stock Dashboard", layout="wide")
st.title("📈 Real-Time Stock Prices Dashboard")


try:
    con = duckdb.connect("data_pipeline.duckdb", read_only=True)
    df = con.execute("SELECT * FROM stock_prices").fetchdf()

    st.success("✅ Loaded stock_prices table")

    
    df["Datetime"] = pd.to_datetime(df["Datetime"])
    df.sort_values(by=["symbol", "Datetime"], inplace=True)

    
    symbol_list = df["symbol"].unique().tolist()
    selected_symbol = st.selectbox("Select a stock symbol", symbol_list)

    symbol_df = df[df["symbol"] == selected_symbol].copy()

    
    symbol_df["% Change"] = symbol_df["Close"].pct_change() * 100

    
    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader(f"📋 Data Preview: {selected_symbol}")
        st.dataframe(symbol_df.tail(10).style.format({"% Change": "{:.2f}"}))

    with col2:
        st.subheader(f"📊 OHLC Candlestick: {selected_symbol}")
        fig = go.Figure(data=[go.Candlestick(
            x=symbol_df["Datetime"],
            open=symbol_df["Open"],
            high=symbol_df["High"],
            low=symbol_df["Low"],
            close=symbol_df["Close"]
        )])
        fig.update_layout(xaxis_rangeslider_visible=False, height=500)
        st.plotly_chart(fig, use_container_width=True)

    
    st.subheader("📉 % Change Over Time")
    st.line_chart(symbol_df.set_index("Datetime")["% Change"])

except Exception as e:
    st.error(f"❌ Error loading data: {e}")
