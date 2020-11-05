import streamlit as st
import pandas as pd
import numpy as np


@st.cache(allow_output_mutation=True, suppress_st_warning=True)
def load_transactions(filename):
    """Load the transactions

    Args:
        filename (BytesIO): A file like subclass from the uploader widget

    Returns:
        pd.DataFrame: The transactions uploaded by the user as a dataframe
    """
    
    filename.seek(0) # reset the buffer
    try: 
        df = pd.read_csv(filename, sep = ';', decimal=',')
    except pd.errors.ParserError: 
        df = pd.read_excel(filename)    
    except pd.errors.EmptyDataError:
        st.info("No data was found in your Excel file")
        st.stop()
    
    return df


@st.cache(allow_output_mutation=True)
def preprocessing(df):
    """ Preprocess the data and create features

    Args:
        df (pd.DataFrame): The transactions loaded by the user 
    
    Returns:
        pd.DataFrame: The preprocessed dataframe
    """
    
    df['Datum']= pd.to_datetime(df['Datum'], format='%Y%m%d')
    df['Week'] = df['Datum'].dt.isocalendar().week
    df['Month'] = df['Datum'].dt.month
    df['Naam / Omschrijving'] = df['Naam / Omschrijving'].str.lower()
    return df 


@st.cache
def get_tag(df):
    """Adds tags to the transaction

    Args:
        df (pd.DataFrame): The transaction

    Returns:
        pd.DataFrame: Transaction dataframe with tags added
    """
    
    grocery_list = ['albert heijn', 'gall', 'avondwinkel', 'ah to go']
    restaurant_list = [ 'snackbar', 'kitchen', 'bistro', 'cafe', 'ramen', 
                        'mcdonalds', 'zeezicht', 'coffee', 'espresso', 'aloha amsterdam',
                        'restaurant', 'campus diemen', 'bergevoet', 'cafeb', 'troost', 
                        'ijssalon', 'kiosk', 'roziers broodj', 'albron', 'proeflokaal', 'febo']
    insurance_list = ['verzekering', 'allianz', 'zilveren kruis']
    tax_list = ['belasting']
    sport_list = ['fresh health fitness', 'tennis', 'padel', 'sport', 'decathlon']
    utilities = ['ziggo', 'tele2']
    salary = ['deloitte']
    leisure = ['kinepolis', 'cinema', 'bol.com', 'esther s cooke', 'cinerama']
    culture = ['de tropen amsterdam', 'ccvcarre']
    travel = ['ns reizigers']
    clothes = ['suitsupply', 'funkie house', 'jbruggeman']
    investing = ['peaks', 'test']

    df['Tag'] = np.select([ df['Naam / Omschrijving'].str.contains(" |".join(grocery_list)),
                            df['Naam / Omschrijving'].str.contains(" |".join(restaurant_list)),
                            df['Naam / Omschrijving'].str.contains(" |".join(insurance_list)),
                            df['Naam / Omschrijving'].str.contains(" |".join(tax_list)),
                            df['Naam / Omschrijving'].str.contains(" |".join(sport_list)),
                            df['Naam / Omschrijving'].str.contains(" |".join(utilities)),
                            df['Naam / Omschrijving'].str.contains(" |".join(leisure)),
                            df['Naam / Omschrijving'].str.contains(" |".join(travel)),
                            df['Naam / Omschrijving'].str.contains(" |".join(culture)),
                            df['Naam / Omschrijving'].str.contains(" |".join(clothes)),
                            df['Naam / Omschrijving'].str.contains(" |".join(investing)),
                            df['Naam / Omschrijving'].str.contains(" |".join(salary))],
                            ['Groceries', 'Restaurant', 'Insurance', 'Tax', 'Sport', 'Utilities', 
                            'leisure', 'travel', 'culture', 'clothes', 'Investing', 'Salary'], 
                            default='Other')
    return df