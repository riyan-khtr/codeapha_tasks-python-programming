
import streamlit as st
import pandas as pd
import csv
import plotly.express as px
#  PAGE CONFIG 
st.set_page_config(page_title="Stock Tracker", layout="wide")
st.title("Stock Portfolio Tracker")

#  STOCK PRICES 
stock_prices = {
    "apple": 180,
    "google": 140,
    "tesla": 250,
    "amazon": 130,
    "microsoft": 300
}

# SESSION STORAGE 
if "portfolio" not in st.session_state:
    st.session_state.portfolio = {}

#  INPUT SECTION 
st.subheader("Add Stocks")

col1, col2 = st.columns(2)

with col1:
    stock_name = st.text_input("Enter stock name").lower()

with col2:
    quantity = st.number_input("Enter quantity", min_value=0)

if st.button("Add to Portfolio"):
    if stock_name in stock_prices:
        st.session_state.portfolio[stock_name] = st.session_state.portfolio.get(stock_name, 0) + quantity
        st.success(f"{stock_name} added!")
    else:
        st.error("Stock not found in list")

 #  REMOVE STOCK
st.subheader("Remove Stock")
remove_stock=st.text_input("Enter stock name to remove").lower()
if st.button("Remove from Portfolio"):
    if remove_stock in st.session_state.portfolio:
        del st.session_state.portfolio[remove_stock]
        st.success(f"{remove_stock} removed!")
    else:
        st.error("Stock not found in portfolio")


# PORTFOLIO DISPLAY 
st.subheader("Your Portfolio")

data = []
total_investment = 0

for stock, qty in st.session_state.portfolio.items():
    value = stock_prices[stock] * qty
    total_investment += value
    data.append([stock, qty, stock_prices[stock], value])

df = pd.DataFrame(data, columns=["Stock", "Quantity", "Price", "Value"])
st.dataframe(df, use_container_width=True)
#TABLE 
st.subheader("portfolio overview")

if df.empty:
    st.info("no stocks added yet")
else:
    st.dataframe(df,use_container_width=True)

#  KPI 
st.metric("Total Investment", total_investment)

# CHARTS
if not df.empty:
    st.subheader("Analytics")
    col3, col4=st.columns(2)
    #pie chart
    with col3:
        fig = px.pie(df, names="Stock", values="Value")
        st.plotly_chart(fig, use_container_width=True)

        #bar cahrt
        with col4:
            fig2 = px.bar(df, x="Stock", y="Value")
            st.plotly_chart(fig2, use_container_width=True)
           

# SAVE FILE 
st.subheader("Export Portfolio")

col5, col6 = st.columns(2)

with col5:
    if st.button("Save  CSV"):
        df.to_csv("portfolio.csv", index=False)
        st.success("CSV saved!")

with col6:
    if st.button("Save TXT"):
        with open("portfolio.txt", "w") as f:
            for stock, qty in st.session_state.portfolio.items():
                value = stock_prices[stock] * qty
                f.write(f"{stock} | {qty} | {value}\n")
            f.write(f"\nTotal Investment: {total_investment}")
        st.success("Saved as portfolio.txt")