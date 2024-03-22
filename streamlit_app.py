import streamlit as st
import gspread
from google.oauth2.service_account import Credentials
import pandas as pd

st.write('cunt')
scopes = ['https://docs.google.com/spreadsheets/d/19eKVNRzY_h56ASeLxu-aR_dTOkHbzrA6Msg57F1_ebs/edit?usp=sharing']
skey = st.secrets['gcp_service_account']
credentials = Credentials.from_service_account_info(skey, scopes=scopes)
client = gspread.authorize(credentials)

def load_data(url, sheet_name='Sheet1'):
    sh = client.open_by_url(url)
    df = pd.DataFrame(sh.worksheet(sheet_name).get_all_records())
    return df


