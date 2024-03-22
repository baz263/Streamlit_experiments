import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
import pandas as pd


def get_data(sheet_name):
    # Authenticate and open the Google Sheet
    credentials_dict = st.secrets['gcp_service_account']
    credentials = service_account.Credentials.from_service_account_info(credentials_dict, scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive",
    ])
    gc= gspread.client(auth=credentials)
    wks = gc.open(sheet_name).sheet1

    data= wks.get_all_values()
    column_names = data[0]
    df = pd.DataFrame(data[1:], columns=column_names)
    return df

data= get_data('nearest_asteroid')

st.dataframe(data)
