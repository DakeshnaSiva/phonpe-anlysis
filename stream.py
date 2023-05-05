import streamlit as st
import pandas as pd
import plotly.express as px


df = pd.read_excel('D:\dakeshna\Django Python\phonepe.xlsx')

st.set_page_config(page_title='My Dashboard')
st.title('My Dashboard')


state = st.sidebar.selectbox('Select a state', df['state'].unique())

filtered_df = df[df['state'] == state]


fig = px.bar(filtered_df, x='transaction_type', y='transaction_count', color='year',
             title='Transaction Count by Transaction Type')
st.plotly_chart(fig)


fig = px.line(filtered_df, x='year', y='transaction_amount', title='Transaction Amount Over Time')
st.plotly_chart(fig)

fig = px.scatter(filtered_df, x='transaction_count', y='transaction_amount', color='year',
                 title='Transaction Count vs. Transaction Amount')
st.plotly_chart(fig)
