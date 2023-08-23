import os
import pandas as pd
import json
import streamlit as st
import plotly.express as px

path=r'D:\dakeshna\Phone_pay link\link\pulse\data\aggregated\transaction\country\india\state'
dir_list_agg = os.listdir(path)
fin_df = pd.DataFrame()
for state in dir_list_agg:
    path1 = path + "//" + state
    dir_list2 = os.listdir(path1)
    for year in dir_list2:
        path2 = path1 + "//" + year
        dir_list3 = os.listdir(path2)
        for qtr in dir_list3:
            path3 = path2 + "//" + qtr
            data=open(path3,'r')
            Agg_D=json.load(data)
            columns={'State':[],'Year':[],'Quater':[],'Transactiontype':[],'TransactionCount':[],'TransactionAmount':[]}
            for m in Agg_D['data']['transactionData']:
                Name=m['name']
                count=m['paymentInstruments'][0]['count']
                amount=m['paymentInstruments'][0]['amount']
                columns['Transactiontype'].append(Name)
                columns['TransactionCount'].append(count)
                columns['TransactionAmount'].append(amount)
                columns['State'].append(state)
                columns['Year'].append(year)
                columns['Quater'].append(int(qtr.strip('.json')))
                C_Data=pd.DataFrame(columns)
                fin_df = pd.concat([fin_df,C_Data])

df = fin_df

st.set_page_config(page_title='Phonepe Dashboard')
st.title('My Dashboard')

state = st.sidebar.selectbox('Select a State', df['State'].unique())
year = st.sidebar.selectbox('Select a Year', df['Year'].unique())
quater = st.sidebar.selectbox('Select a Quater', df['Quater'].unique())

filtered_df = df[df['State'] == state]
filtered_df = filtered_df[filtered_df['Year'] == year]
filtered_df = filtered_df[filtered_df['Quater'] == quater]

fig = px.bar(filtered_df, x='Transactiontype', y='TransactionCount', color='Year',
             title='Transaction Count by Transaction Type')
st.plotly_chart(fig)


fig = px.line(filtered_df, x='Year', y='TransactionAmount', title='Transaction Amount Over Time')
st.plotly_chart(fig)

fig = px.scatter(filtered_df, x='TransactionCount', y='TransactionAmount', color='Year',
                 title='Transaction Count vs. Transaction Amount')
st.plotly_chart(fig)
