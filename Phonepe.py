# [File handling library]
import streamlit as st
from streamlit_option_menu import option_menu 
import psycopg2
import plotly.express as px
# import os
# import json
import pandas as pd


#Dataframe creation

#sql connection
mydb = psycopg2.connect (host = "localhost",
                         user = "postgres",
                         password = "roomno13",
                         database = "phonepe_data",
                         port = "5432")
cursor = mydb.cursor()

#Aggregated_insurance_df
cursor.execute("SELECT * FROM aggregated_insurance")
mydb.commit()
table1 = cursor.fetchall()

Aggregated_insurance = pd.DataFrame(table1,columns=("States","Years","Quarter","Transaction_type","Transaction_count","Transaction_amount"))


#Aggregated_transacation_df
cursor.execute("SELECT * FROM aggregated_transaction")
mydb.commit()
table2 = cursor.fetchall()

Aggregated_transacation = pd.DataFrame(table2,columns=("States","Years","Quarter","Transaction_type","Transaction_count","Transaction_amount"))


#Aggregated_user_df
cursor.execute("SELECT * FROM aggregated_user")
mydb.commit()
table3 = cursor.fetchall()

Aggregated_user= pd.DataFrame(table3,columns=("States","Years","Quarter","Brands","Transaction_count","Percentage"))


#Map_insurance_df
cursor.execute("SELECT * FROM map_insurance")
mydb.commit()
table4 = cursor.fetchall()

Map_insurance= pd.DataFrame(table4,columns=("States","Years","Quarter","Districts","Transaction_count","Transaction_amount"))


#Map_transaction_df
cursor.execute("SELECT * FROM map_transaction")
mydb.commit()
table5 = cursor.fetchall()

Map_transaction= pd.DataFrame(table5,columns=("States","Years","Quarter","Districts","Transaction_count","Transaction_amount"))


#Map_user_df
cursor.execute("SELECT * FROM map_user")
mydb.commit()
table6 = cursor.fetchall()

Map_user= pd.DataFrame(table6,columns=("States","Years","Quarter","Districts","RegisteredUsers","AppOpens"))


#Top_Insurance_df
cursor.execute("SELECT * FROM top_insurance")
mydb.commit()
table7 = cursor.fetchall()

Top_Insurance= pd.DataFrame(table7,columns=("States","Years","Quarter","Pincodes","Transaction_count","Transaction_amount"))


#Top_transaction _df
cursor.execute("SELECT * FROM top_transaction")
mydb.commit()
table8 = cursor.fetchall()

Top_transaction = pd.DataFrame(table8,columns=("States","Years","Quarter","Pincodes","Transaction_count","Transaction_amount"))


#Top_user _df
cursor.execute("SELECT * FROM top_user")
mydb.commit()
table9 = cursor.fetchall()

Top_user = pd.DataFrame(table9,columns=("States","Years","Quarter","Pincodes","RegisteredUsers"))


# creating function for Transaction_amount_count

def Transaction_amount_count_Y(df,year):

    tran_amount_count_year = df[df["Years"] == year]
    tran_amount_count_year.reset_index(drop = True, inplace= True)

    tran_amount_count_year_group = tran_amount_count_year.groupby("States")[["Transaction_count","Transaction_amount"]].sum()
    tran_amount_count_year_group.reset_index(inplace=True)

    fig_amount = px.bar(tran_amount_count_year_group, x="States", y="Transaction_amount", title=f"{year} TRANSACTION AMOUNT",
                        color_discrete_sequence=px.colors.sequential.Aggrnyl)
    st.plotly_chart(fig_amount)

    fig_count = px.bar(tran_amount_count_year_group, x="States", y="Transaction_count", title=f"{year} TRANSACTION COUNT",
                        color_discrete_sequence=px.colors.sequential.Blackbody_r)
    st.plotly_chart( fig_count)


#Streamlit part

st.set_page_config(layout="wide")
st.title("PHONEPE DATA VISUALIZATION AND EXPLORATION")

with st.sidebar:

    select = option_menu("Main Menu",["HOME", "DATA EXPLORATION", "TOP CHARTS"])

    if select == "HOME":
        pass

    elif select == "DATA EXPLORATION":

        tab1, tab2, tab3 = st.tabs(["Aggregated Analysis", "Map Analysis", "Top Analysis"])

        with tab1:
            method = st.radio("Select The Method",["Insurance Analysis", "Transaction Analysis", "User Analysis"])

            if method == "Insurance Analysis":
                years = st.slider("Select The Year",Aggregated_insurance["Years"].min(),Aggregated_insurance["Years"].max())
                Transaction_amount_count_Y(Aggregated_insurance,years)

            elif method == "Transaction Analysis":
                pass

            elif method == "User Analysis":
                pass

        with tab2:
            method_2 = st.radio("Select The Method",["Map Insurance", "Map Transaction", "Map User"])

            if method_2 == "Map Insurance":
                pass

            elif method_2 == "Map Transaction":
                pass

            elif method_2 == "Map User":
                pass

        with tab3:

            method_3 = st.radio("Select The Method",["Top Insurance", "Top Transaction", "Top User"])

            if method_3 == "Top Insurance":
                pass

            elif method_3 == "Top Transaction":
                pass

            elif method_3 == "Top User":
                pass

    elif select == "TOP CHARTS":
        pass