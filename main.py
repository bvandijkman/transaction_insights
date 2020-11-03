import streamlit as st
import pandas as pd
import numpy as np
import helpers

st.title("Insight in your transactions")
st.subheader("Load your transaction file to get insights into your monthly spending")

filename = st.file_uploader("Load your data", ['csv', 'xlsx'])

if filename: 
    df = helpers.load_data(filename)

    df = helpers.preprocessing(df)

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
    allergy = ['allergiezorg', 'kruidvat', 'allergiezorg.nl']
    investing = ['peaks']

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
                            df['Naam / Omschrijving'].str.contains(" |".join(allergy)),
                            df['Naam / Omschrijving'].str.contains(" |".join(investing)),
                            df['Naam / Omschrijving'].str.contains(" |".join(salary))],
                            ['Groceries', 'Restaurant', 'Insurance', 'Tax', 'Sport', 'Utilities', 
                            'leisure', 'travel', 'culture', 'clothes', 'Allergy', 'Investing', 'Salary'], 
                            default='Other')

    st.write(df)

    data = df[['Naam / Omschrijving', 'Tag', 'Bedrag (EUR)', 'Af Bij']]
    st.write(data[data['Tag'].str.contains("Other")])
    st.write(len(data[data['Tag'].str.contains("Other")]))

    st.write(df.groupby(['Month', 'Tag'])['Bedrag (EUR)'].agg('sum'))


    
