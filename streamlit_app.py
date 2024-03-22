import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
from google.oauth2 import service_account


def get_data(sheet_name):
    # Authenticate and open the Google Sheet
    credentials_dict = st.secrets['gcp_service_account']
    credentials = service_account.Credentials.from_service_account_info(credentials_dict, scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive",
    ])
    gc= gspread.Client(auth=credentials)
    wks = gc.open(sheet_name).sheet1

    data= wks.get_all_values()
    column_names = data[0]
    df = pd.DataFrame(data[1:], columns=column_names)
    return df

data= get_data('nearest_asteroid')
st.write('Solar flares in the last week')
st.dataframe(data)

# def get_data(sheet_name):
#     # Authenticate and open the Google Sheet
#     credentials_dict = st.secrets['gcp_service_account']
#     credentials = service_account.Credentials.from_service_account_info(credentials_dict, scopes=[
#         "https://www.googleapis.com/auth/spreadsheets",
#         "https://www.googleapis.com/auth/drive",
#     ])
#     gc = gspread.Client(auth=credentials)  # Change gspread.client to gspread.Client
#     gc.login()  # Optional: You can call login() to authenticate if needed
#     wks = gc.open(sheet_name).sheet1

#     data = wks.get_all_values()
#     column_names = data[0]
#     df = pd.DataFrame(data[1:], columns=column_names)
#     return df

# data = get_data('nearest_asteroid')
# st.write('boob')
# st.dataframe(data)