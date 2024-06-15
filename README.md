AUTHOR:- BIRENDRA EMANUEL EKKA

Project Title :- Phonepe Pulse Data Visualization and Exploration:
                 A User-Friendly Tool Using Streamlit and Plotly

Domain:- Fintech

Problem Statement: The Phonepe pulse Github repository contains a large amount of data related to
                   various metrics and statistics. The goal is to extract this data and process it to obtain
                   nsights and information that can be visualized in a user-friendly manner.

1. Extracted data from the Phonepe pulse Github repository through scripting and
    cloneing.
2. Transform the data into a suitable format and performed necessary cleaning
    and pre-processing steps.
3. Inserting the transformed data into a MySQL database for efficient storage and
    retrieval.
4. Creating a live geo visualization dashboard using Streamlit and Plotly in Python
    to display the data in an interactive and visually appealing manner.
5. Fetched the data from the MySQL database to display in the dashboard.

6. Provided 10 different dropdown options for users to select different
    facts and figures to display on the dashboard.


Technologies: Github Cloning, Python, Pandas, MySQL,
             mysql-connector-python, Streamlit, and Plotly.
             
streamlit as st: 
This imports the Streamlit library, which is used for creating web applications with Python. 
The alias st is used for convenient access to Streamlit's functions.

streamlit_option_menu import option_menu: 
This imports the option_menu function from the streamlit_option_menu package, 
which is used to create a menu with multiple options in a Streamlit app.

psycopg2: 
This is a PostgreSQL adapter for Python, 
allowing the application to connect to and interact with a PostgreSQL database.

plotly.express as px: 
This imports the Plotly Express module, 
a high-level interface to Plotly for creating quick and easy visualizations.

pandas as pd: 
This imports the pandas library, which provides data structures and data analysis tools,
particularly useful for handling tabular data.

requests: 
This library is used for making HTTP requests to interact with APIs and retrieve data from the web.

json: 
This module is used for parsing JSON (JavaScript Object Notation) data,
 allowing the application to handle JSON-formatted data.

PIL import Image: 
This imports the Image class from the Python Imaging Library (PIL), 
which provides tools for opening, manipulating, and saving image files.

Dataframe creation:-The code snippet establishes a connection to a PostgreSQL database and retrieves data from 
                    several tables related to PhonePe transaction and user data. 
                    The data is then converted into pandas DataFrames for further analysis and visualization.
                     
1.Establish Database Connection:

2.Create a Cursor Object:

3.Fetch Data from aggregated_insurance Table:

4.Fetch Data from aggregated_transaction Table:

5.Fetch Data from aggregated_user Table:

6.Fetch Data from map_insurance Table:

7.Fetch Data from map_transaction Table:

8.Fetch Data from map_user Table:

9.Fetch Data from top_insurance Table:

10.Fetch Data from top_transaction Table:
