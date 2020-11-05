import streamlit as st
import pandas as pd
import numpy as np
import helpers


def main():

    # Write title and subheader
    st.title("Insight in your transactions")
    st.subheader("Load your transaction file to get insights into your monthly spending")

    # Widget that allows user to upload csv and excel file 
    filename = st.file_uploader("Load your data", ['csv', 'xlsx'])

    if filename is not None: 
        
        # Load data
        df = helpers.load_transactions(filename)

        # Preprocess Data
        df = helpers.preprocessing(df)
        
        # Get the tags
        df = helpers.get_tag(df)
        
        # Select columns
        data = df[['Naam / Omschrijving', 'Tag', 'Bedrag (EUR)', 'Af Bij']]
        
        # Look at transactions that are not yet tagged (other) 
        st.write(data[data['Tag'].str.contains("Other")])
        
        # Sum the amount per category
        st.write(df.groupby(['Month', 'Tag'])['Bedrag (EUR)'].agg('sum'))


if __name__ == '__main__':
    main()