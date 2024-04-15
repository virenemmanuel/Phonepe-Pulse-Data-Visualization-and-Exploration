# [File handling library]
import streamlit as st
from streamlit_option_menu import option_menu 
import psycopg2
import plotly.express as px
import pandas as pd
import requests
import json
# import os
# import json



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


# creating function for Transaction_amount_count year

def Transaction_amount_count_Y(df,year):

    tran_amount_count_year = df[df["Years"] == year]
    tran_amount_count_year.reset_index(drop = True, inplace= True)

    tran_amount_count_year_group = tran_amount_count_year.groupby("States")[["Transaction_count","Transaction_amount"]].sum()
    tran_amount_count_year_group.reset_index(inplace=True)

    col1,col2 = st.columns(2)
    with col1:

        fig_amount = px.bar(tran_amount_count_year_group, x="States", y="Transaction_amount", title = f"{year} TRANSACTION AMOUNT",
                            color_discrete_sequence=px.colors.sequential.Aggrnyl, height=650,width=600)
        st.plotly_chart(fig_amount)

    with col2:
        fig_count = px.bar(tran_amount_count_year_group, x="States", y="Transaction_count", title = f"{year} TRANSACTION COUNT",
                            color_discrete_sequence=px.colors.sequential.OrRd_r, height=650,width=600)
        st.plotly_chart(fig_count)


    col1,col2 = st.columns(2)
    with col1:
        url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
        response = requests.get(url)
        data_1 = json.loads(response.content)
        states_name = []
        for feature in data_1["features"]:
            states_name.append(feature["properties"]["ST_NM"])

        states_name.sort()

    
        fig_india_1 = px.choropleth(tran_amount_count_year_group, geojson= data_1, locations= "States", featureidkey= "properties.ST_NM",
                                    color= "Transaction_amount", color_continuous_scale= "Rainbow", 
                                    range_color=(tran_amount_count_year_group["Transaction_amount"].min(),tran_amount_count_year_group["Transaction_amount"].max()),
                                    hover_name= "States", title = f"{year} TRANSACTION AMOUNT",fitbounds= "locations",
                                    height= 600,width= 600)
        fig_india_1.update_geos(visible = False)
        st.plotly_chart(fig_india_1)

    with col2:
        fig_india_2 = px.choropleth( tran_amount_count_year_group, geojson= data_1, locations= "States", featureidkey= "properties.ST_NM",
                                color= "Transaction_count", color_continuous_scale= "Rainbow", 
                                range_color=(tran_amount_count_year_group["Transaction_count"].min(),tran_amount_count_year_group["Transaction_count"].max()),
                                hover_name= "States", title = f"{year} TRANSACTION COUNT",fitbounds= "locations",
                                height= 600,width= 600)
        fig_india_2.update_geos(visible = False)
        st.plotly_chart(fig_india_2)

    return tran_amount_count_year


# creating function for Transaction_amount_count quater

def Transaction_amount_count_Y_Q(df, quarter):
    tran_amount_count_year = df[df["Quarter"] ==  quarter]
    tran_amount_count_year.reset_index(drop = True, inplace= True)

    tran_amount_count_year_group = tran_amount_count_year.groupby("States")[["Transaction_count","Transaction_amount"]].sum()
    tran_amount_count_year_group.reset_index(inplace=True)

    col1,col2 = st.columns(2)
    with col1:
        fig_amount = px.bar(tran_amount_count_year_group, x="States", y="Transaction_amount", title=f"{tran_amount_count_year['Years'].min()} YEAR {quarter} Quarter TRANSACTION AMOUNT",
                            color_discrete_sequence=px.colors.sequential.Aggrnyl)
        st.plotly_chart(fig_amount)

    with col2:
        fig_count = px.bar(tran_amount_count_year_group, x="States", y="Transaction_count", title=f"{tran_amount_count_year['Years'].min()} YEAR {quarter} Quarter TRANSACTION COUNT",
                            color_discrete_sequence=px.colors.sequential.OrRd_r)
        st.plotly_chart(fig_count)


    col1,col2 = st.columns(2)
    with col1:
        url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
        response = requests.get(url)
        data_1 = json.loads(response.content)
        states_name = []
        for feature in data_1["features"]:
            states_name.append(feature["properties"]["ST_NM"])

        states_name.sort()

        fig_india_1 = px.choropleth(   tran_amount_count_year_group, geojson= data_1, locations= "States", featureidkey= "properties.ST_NM",
                                    color= "Transaction_amount", color_continuous_scale= "Rainbow", 
                                    range_color=(tran_amount_count_year_group["Transaction_amount"].min(),tran_amount_count_year_group["Transaction_amount"].max()),
                                    hover_name= "States", title = f"{tran_amount_count_year['Years'].min()} YEAR {quarter} Quarter TRANSACTION AMOUNT",fitbounds= "locations",
                                    height= 600,width= 600)
        fig_india_1.update_geos(visible = False)
        st.plotly_chart(fig_india_1)

    with col2:
        fig_india_2 = px.choropleth(   tran_amount_count_year_group, geojson= data_1, locations= "States", featureidkey= "properties.ST_NM",
                                color= "Transaction_count", color_continuous_scale= "Rainbow", 
                                range_color=(tran_amount_count_year_group["Transaction_count"].min(),tran_amount_count_year_group["Transaction_count"].max()),
                                hover_name= "States", title = f"{tran_amount_count_year['Years'].min()} YEAR {quarter} Quarter TRANSACTION COUNT",fitbounds= "locations",
                                height= 600,width= 600)
        fig_india_2.update_geos(visible = False)
        st.plotly_chart(fig_india_2)

    return tran_amount_count_year
    

# aggregated tran transcation type 
def Aggre_tran_Transaction_type(df,state):

    tran_amount_count_year = df[df["States"] == state]
    tran_amount_count_year.reset_index(drop = True, inplace= True)

    tran_amount_count_year_group = tran_amount_count_year.groupby("Transaction_type")[["Transaction_count","Transaction_amount"]].sum()
    tran_amount_count_year_group.reset_index(inplace=True)

    col1,col2 = st.columns(2)
    with col1:
        fig_pie_1 = px.pie(data_frame=tran_amount_count_year_group, names="Transaction_type",values="Transaction_amount",
                        width = 600,title=f"{state.upper()} TRANSACTION AMOUNT", hole= 0.5)

        st.plotly_chart(fig_pie_1)
    with col2:
        fig_pie_2 = px.pie(data_frame=tran_amount_count_year_group, names="Transaction_type",values="Transaction_count",
                        width = 600,title=f"{state.upper()} TRANSACTION COUNT", hole= 0.5)

        st.plotly_chart(fig_pie_2)


# Aggregated_user_analysis_1
def Aggregated_user_plot_1(df,year):
    aggregated_user_year= df[df["Years"]==2018]
    aggregated_user_year.reset_index(drop=True, inplace= True)

    aggregated_user_year_group = pd.DataFrame(aggregated_user_year.groupby("Brands")["Transaction_count"].sum())
    aggregated_user_year_group.reset_index(inplace=True)

    fig_bar_1 = px.bar(aggregated_user_year_group,x="Brands",y="Transaction_count",title=f"{year} BRANDS and TRANSACTION COUNT",
                    width=1000, color_discrete_sequence= px.colors.sequential.haline_r, hover_name="Brands")
    st.plotly_chart(fig_bar_1)

    return aggregated_user_year

#Aggregated user analysis_2
def Aggregated_user_plot_2(df,quarter):
    aggregated_user_year_quarter= df[df["Quarter"]==quarter]
    aggregated_user_year_quarter.reset_index(drop=True, inplace= True)


    aggregated_user_year_quarter_group = pd.DataFrame(aggregated_user_year_quarter.groupby("Brands")["Transaction_count"].sum())
    aggregated_user_year_quarter_group.reset_index(inplace=True)

    fig_bar_1 = px.bar(aggregated_user_year_quarter_group,x="Brands",y="Transaction_count",title=f"Quarter-{quarter} BRANDS and TRANSACTION COUNT",
                    width=1000, color_discrete_sequence= px.colors.sequential.algae, hover_name="Brands")
    st.plotly_chart(fig_bar_1)

    return aggregated_user_year_quarter


#Aggregated_user analysis 3
def Aggregated_user_plot_3(df,states):
    aggregated_user_year_q_s = df[df["States"] == states]
    aggregated_user_year_q_s.reset_index(drop=True, inplace=True)

    fig_line_1 = px.line(aggregated_user_year_q_s, x="Brands", y= "Transaction_count",hover_data= ['Percentage'],
                        title=f"{states.upper()}: BRANDS, TRANSACTION COUNT, PERCENTAGE",width = 1000, markers=True)
    st.plotly_chart(fig_line_1)


# MAP insurance districts 
def Map_insurance_District(df,state):

    tran_amount_count_year = df[df["States"] == state]
    tran_amount_count_year.reset_index(drop = True, inplace= True)

    tran_amount_count_year_group = tran_amount_count_year.groupby("Districts")[["Transaction_count","Transaction_amount"]].sum()
    tran_amount_count_year_group.reset_index(inplace=True)

   
    fig_bar_1 = px.bar(tran_amount_count_year,x= "Transaction_amount", y= "Districts", orientation="h",height=600,
                        title =f"{state.upper()} DISTRICT AND TRANSACTION AMOUNT",color_discrete_sequence= px.colors.sequential.Mint_r)
    st.plotly_chart(fig_bar_1)

    
    fig_bar_2 = px.bar(tran_amount_count_year_group, x="Transaction_count", y="Districts", orientation="h",height=600,
                    title=f"{state.upper()} DISTRICTS AND TRANSACTION COUNT",color_discrete_sequence= px.colors.sequential.Bluyl_r)
    st.plotly_chart(fig_bar_2)


# MAP USER PLOT 1
def map_user_plot_1(df,year):
    Map_user_year= df[df["Years"]==year]
    Map_user_year.reset_index(drop=True,inplace= True)


    Map_user_year_group = Map_user_year.groupby("States")[["RegisteredUsers","AppOpens"]].sum()
    Map_user_year_group.reset_index(inplace=True)

    fig_line_1 = px.line(Map_user_year_group, x="States", y= ["RegisteredUsers","AppOpens"],
                        title= f"{year} STATES REGISTERED USERS APPOPENS",width = 1000, height=800, markers=True)
    st.plotly_chart(fig_line_1)

    return Map_user_year


# MAP USER PLOT 2
def map_user_plot_2(df,quarter):
    Map_user_year_Q= df[df["Quarter"]==quarter]
    Map_user_year_Q.reset_index(drop=True,inplace= True)


    Map_user_year_Q_group = Map_user_year_Q.groupby("States")[["RegisteredUsers","AppOpens"]].sum()
    Map_user_year_Q_group.reset_index(inplace=True)

    fig_line_1 = px.line(Map_user_year_Q_group, x="States", y= ["RegisteredUsers","AppOpens"],
                        title= f"Years-{df['Years'].min()}, {quarter}-QUARTER REGISTERED USERS APPOPENS",width = 1000, height=800, markers=True,
                        color_discrete_sequence=px.colors.sequential.Rainbow_r)
    st.plotly_chart(fig_line_1)

    return Map_user_year_Q



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
        method = st.radio("Select The Method",["Aggregated Insurance","Aggregated Transaction","Aggregated User"])

        if method == "Aggregated Insurance":

            col1,col2 = st.columns(2)
            with col1:

                years = st.slider("Select The Year",Aggregated_insurance["Years"].min(),Aggregated_insurance["Years"].max(),Aggregated_insurance["Years"].min())
            tran_amount_count_year = Transaction_amount_count_Y(Aggregated_insurance,years)

            col1,col2 = st.columns(2)
            with col1:

                quarter = st.slider("Select The Quarter",tran_amount_count_year["Quarter"].min(),tran_amount_count_year["Quarter"].max(),
                                         tran_amount_count_year["Quarter"].min())
            
            Transaction_amount_count_Y_Q(tran_amount_count_year, quarter)



        elif method == "Aggregated Transaction":

             col1,col2 = st.columns(2)
             with col1:

                years = st.slider("Select The Year",Aggregated_transacation["Years"].min(),Aggregated_transacation["Years"].max(),Aggregated_transacation["Years"].min())
             Aggre_tran_amount_count_year = Transaction_amount_count_Y(Aggregated_transacation,years)

             col1,col2 = st.columns(2)
             with col1:
                 states = st.selectbox("Select The State", Aggre_tran_amount_count_year["States"].unique())

             Aggre_tran_Transaction_type(Aggre_tran_amount_count_year,states)


             col1,col2 = st.columns(2)
             with col1:

                quarter = st.slider("Select The Quarter", Aggre_tran_amount_count_year["Quarter"].min(), Aggre_tran_amount_count_year["Quarter"].max(),
                                          Aggre_tran_amount_count_year["Quarter"].min())
            
             Aggre_tran_amount_count_year_Q = Transaction_amount_count_Y_Q(Aggre_tran_amount_count_year, quarter) 

             col1,col2 = st.columns(2)
             with col1:
                 states = st.selectbox("Select The State_ty", Aggre_tran_amount_count_year_Q["States"].unique())

             Aggre_tran_Transaction_type(Aggre_tran_amount_count_year_Q,states)
            

        elif method == "Aggregated User":
             
             col1,col2 = st.columns(2)
             with col1:

                years = st.slider("Select The Year",Aggregated_user["Years"].min(),Aggregated_user["Years"].max(),Aggregated_user["Years"].min())
             Aggregated_user_Y = Aggregated_user_plot_1(Aggregated_user,years)

             col1,col2 = st.columns(2)
             with col1:

                quarter = st.slider("Select The Quarter",  Aggregated_user_Y["Quarter"].min(), Aggregated_user_Y["Quarter"].max(),
                                           Aggregated_user_Y["Quarter"].min())
            
                Aggregated_user_Y_Q = Aggregated_user_plot_2( Aggregated_user_Y, quarter) 

                
             col1,col2 = st.columns(2)
             with col1:
                 states = st.selectbox("Select The State",  Aggregated_user_Y_Q["States"].unique())

             Aggregated_user_plot_3( Aggregated_user_Y_Q,states)

        

    with tab2:
        method_2 = st.radio("Select The Method",["Map Insurance", "Map Transaction", "Map User"])

        if method_2 == "Map Insurance":
             
             col1,col2 = st.columns(2)
             with col1:

                years = st.slider("Select The Year_map",Map_insurance["Years"].min(),Map_insurance["Years"].max(),Map_insurance["Years"].min())
             Map_insur_tran_amount_count_year = Transaction_amount_count_Y(Map_insurance,years)

             col1,col2 = st.columns(2)
             with col1:
                 states = st.selectbox("Select The State_map_insurance", Map_insur_tran_amount_count_year["States"].unique())

             Map_insurance_District( Map_insur_tran_amount_count_year,states)

             col1,col2 = st.columns(2)
             with col1:

              quarter = st.slider("Select The Quarter_map",  Map_insur_tran_amount_count_year["Quarter"].min(),  Map_insur_tran_amount_count_year["Quarter"].max(),
                                         Map_insur_tran_amount_count_year["Quarter"].min())
        
             Map_insur_tran_amount_count_year_Q = Transaction_amount_count_Y_Q(Map_insur_tran_amount_count_year, quarter) 

             col1,col2 = st.columns(2)
             with col1:
                 states = st.selectbox("Select The State_ty",Map_insur_tran_amount_count_year_Q["States"].unique())

             Map_insurance_District(Map_insur_tran_amount_count_year_Q,states)


        elif method_2 == "Map Transaction":
            
             col1,col2 = st.columns(2)
             with col1:

                years = st.slider("Select The Year_map",Map_transaction["Years"].min(),Map_transaction["Years"].max(),Map_transaction["Years"].min())
             Map_transaction_tran_amount_count_year = Transaction_amount_count_Y(Map_transaction,years)

             col1,col2 = st.columns(2)
             with col1:
                 states = st.selectbox("Select The State_map_transaction", Map_transaction_tran_amount_count_year["States"].unique())

             Map_insurance_District(Map_transaction_tran_amount_count_year,states)

             col1,col2 = st.columns(2)
             with col1:

              quarter = st.slider("Select The Quarter_map_transaction",Map_transaction_tran_amount_count_year["Quarter"].min(), Map_transaction_tran_amount_count_year["Quarter"].max(),
                                         Map_transaction_tran_amount_count_year["Quarter"].min())
        
             Map_transaction_tran_amount_count_year_Q = Transaction_amount_count_Y_Q(Map_transaction_tran_amount_count_year, quarter) 

             col1,col2 = st.columns(2)
             with col1:
                 states = st.selectbox("Select The State_ty",Map_transaction_tran_amount_count_year_Q["States"].unique())

             Map_insurance_District(Map_transaction_tran_amount_count_year_Q,states)


        elif method_2 == "Map User":
            
             col1,col2 = st.columns(2)
             with col1:

                 years = st.slider("Select The Year_MU",Map_user["Years"].min(),Map_user["Years"].max(),Map_user["Years"].min())
             Map_user_Y = map_user_plot_1(Map_user,years)

             col1,col2 = st.columns(2)
             with col1:

                quarters = st.slider("Select The Quarter_MU_Q",Map_user_Y["Quarter"].min(),Map_user_Y["Quarter"].max(),Map_user_Y["Quarter"].min())
             Map_user_Y_Q = map_user_plot_2(Map_user_Y,quarters)

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