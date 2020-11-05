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

        # Sum the amount per category per month        
        grouped_data = df.groupby(['Month', 'Tag'])['Bedrag (EUR)'].agg('sum')
        
        st.subheader("Transactions grouped by month")
        st.write(grouped_data)
        
        # Look at transactions that are not yet tagged (other) 
        st.subheader("Transactions without a tag")
        st.write(data[data['Tag'].str.contains("Other")])
        


if __name__ == '__main__':
    main()