import streamlit as st
from streamlit_gsheets import GSheetsConnection

conn = st.connection('gsheets', type=GSheetsConnection)
data = conn.read(spreadsheet='nearest_asteroid', worksheet='Sheet1')
st.dataframe(data)

