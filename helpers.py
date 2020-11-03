import streamlit as st
import pandas as pd


@st.cache(allow_output_mutation=True)
def load_data():
    df = pd.read_csv("data/data.csv", sep = ';', decimal=',')
    return df

@st.cache
def preprocessing(df):
    """ Preprocess the data and create features

    Args:
        df (pd.DataFrame): The transactions loaded by the user 
    """
    df['Datum']= pd.to_datetime(df['Datum'], format='%Y%m%d')
    df['Week'] = df['Datum'].dt.week
    df['Month'] = df['Datum'].dt.month
    df['Naam / Omschrijving'] = df['Naam / Omschrijving'].str.lower()
    return df 