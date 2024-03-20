#!/usr/bin/env python
# coding: utf-8

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import seaborn as sns
import streamlit as st
import pickle
import re
from datetime import datetime

# Initialise the items in station state
if 'df' not in st.session_state:
    st.session_state['df'] = pd.DataFrame()
if 'df_pred' not in st.session_state:
    st.session_state['df_pred'] = pd.DataFrame()
if 'filename' not in st.session_state:
    st.session_state['filename'] = ''

# Get the scaler and model loading path
current_dir = os.path.dirname(os.path.realpath(__file__))
sc_path = os.path.join(current_dir, 'scaler.pkl')
features_path = os.path.join(current_dir, 'feature_columns.pkl')
model_path = os.path.join(current_dir, 'models', 'CatBoost.pkl')

# Load the model and scaler
sc = pickle.load(open(sc_path, 'rb'))
model = pickle.load(open(model_path, 'rb'))

# Set the page title
st.set_page_config(page_title='Customer Churn Prediction')

# Set the title
st.title('Customer Churn Prediction')

# Accept the uploaded dataset
st.header('Dataset')

data = st.file_uploader(label='**Upload the dataset for prediction:**')

# Read the upload file into a dataframe
if data:    
    df = pd.read_csv(data)
    st.session_state['filename'] = data.name  
    
    # Preprocess the data for prediction
    # Rename columns
    df.columns = [re.sub(r'([A-Z])', r' \1', col).lower().strip().replace(' ', '_') for col in df.columns]
    df.rename(columns={
        'customer_i_d': 'customer_id',
        'streaming_t_v': 'streaming_tv'
    }, inplace=True)

    # Fill the missing values in the services
    services = ['internet_service', 'online_security', 'online_backup', 'device_protection',
                'tech_support', 'streaming_tv', 'streaming_movies', 'multiple_lines']
    df[services] = df[services].fillna('not_subscribed')
    
    # Replace invalid values
    df['total_charges'].replace(' ', 0, inplace=True)
    
    # Convert the data types
    df['begin_date'] = pd.to_datetime(df['begin_date'], format='%m/%d/%Y')
    df['total_charges'] = df['total_charges'].astype(float)
    
    # Add `monthly_charges` to the 'total_charges'
    df['total_charges'] = df['total_charges'] + df['monthly_charges']

    # Find the total subscribed_days and years
    current_date = datetime.now()
    df['subscribed_days'] = (current_date - df['begin_date']).dt.days
    df['subscribed_years'] = current_date.year - df['begin_date'].dt.year

    # Calculate the `total_services`
    def assign_service_type(row):
        '''
        Assign the type of service subscribed by a customer.
        '''
        if row['internet_service'] != 'not_subscribed' and row['multiple_lines'] == 'not_subscribed':
            return 'internet_service'
        elif row['internet_service'] == 'not_subscribed' and row['multiple_lines'] != 'not_subscribed':
            return 'landline_communication'
        else:
            return 'both'

    df['subscribed_service'] = df.apply(assign_service_type, axis=1)

    # Calculate the `total_internet_services`    
    internet_services = ['online_security', 'online_backup', 'device_protection',
                         'tech_support', 'streaming_tv', 'streaming_movies']    
    
    def calc_total_internet_services(row):
        '''
        Calculate and return total number of subsribed internet services of a customer
        '''
        count = 0
    
        for service in internet_services:
            if row[service] == 'Yes':
                count += 1
    
        return count
        
    df['total_internet_services'] = df.apply(calc_total_internet_services, axis=1)

    # Show the dataset after preprocessing
    st.write(df)
    
    # Make the prediction    
    if st.button('Predict'):
        # Get the features for prediction
        df.drop(columns=['customer_id', 'begin_date'], inplace=True)
        
        # One-hot enconding and feature scaling
        X = pd.get_dummies(df, drop_first=True, dtype=int)
        
        numerical_features = ['monthly_charges', 'total_charges', 'subscribed_days', 'subscribed_years', 'total_internet_services']
        X[numerical_features] = sc.fit_transform(X[numerical_features])
        
        # Recreate the features to comply with the model
        feature_columns = pickle.load(open(features_path, 'rb'))
        X_final = pd.DataFrame(columns=feature_columns)
        
        for col in X_final.columns:
            if col in X.columns:
                X_final[col] = X[col]
            else:
                X_final[col] = 0
        
        df_pred = df.copy()
        df_pred['churn'] = model.predict(X_final)        

        # Save the dataframes
        st.session_state['df'] = df
        st.session_state['df_pred'] = df_pred
        
# Get the saved dataframes
df = st.session_state['df_pred']
df_pred = st.session_state['df_pred']

if data and ('churn' in df_pred.columns) and ('customer_id' not in df.columns):
    # Show the prediction
    st.header('Prediction')
    st.write(df_pred)

    # Create a button for downlaoding the prediction result
    download_filename = st.session_state['filename'].split('.')[0] + '_prediction.csv'
    st.download_button(label='Download Prediction', data=df_pred.to_csv(index=False), mime='text/csv', file_name=download_filename)

    # Prediction Result Analysis per characteristic
    st.header('Prediction Result Analysis')
    
    menu = list(df_pred.columns)
    menu.remove('churn')
    menu = [' '.join(word.capitalize() for word in x.split('_')) for x in menu]
    menu.insert(0, 'Choose the characteristic')
    menu.insert(1, 'Overall')
    choice = st.selectbox('**Characteristic**', menu)

    col1, col2 = st.columns(2)

    # Overall churn
    if choice.lower() == 'overall':
        result = df_pred['churn'].value_counts().to_frame()
        result.index = result.index.map({0: 'Stay', 1:'Leave'})
        
        with col1:            
            plt.figure(figsize=(3, 2))
            sns.barplot(x=result.index, y=result['count'], hue=result.index, palette=['steelblue', 'tomato'])
            plt.title('Customer Churn', fontsize=9, fontweight='bold')
            plt.xlabel('')
            plt.ylabel('Number of customers', fontsize=8, fontweight='bold')
            plt.xticks(fontsize=8, fontweight='bold')
            plt.yticks(fontsize=7, )
            plt.show()
            st.pyplot(plt)
        with col2:
            table = result.copy()
            table.rename_axis('', inplace=True)            
            table['percentage'] = round(table['count'] / table['count'].sum() * 100, 2)
            for _ in range(2):
                st.write('#')
            st.table(table.style.format("{:.2f}"))

    # Churn rate for categorical features
    elif choice.lower() in ['type', 'paperless billing', 'payment method', 'gender', 'senior citizen',
                            'partner', 'dependents', 'internet service', 'online security', 'online backup',
                            'device protection', 'tech support', 'streaming tv', 'streaming movies',
                            'multiple lines', 'subscribed service']:
        feature = '_'.join(choice.lower().split(' '))             
        
        with col1: 
            plt.figure(figsize=(3, 3))
            palette = ['steelblue', 'tomato']
            sns.histplot(data=df_pred, x=feature, hue='churn', multiple='fill', discrete=True, 
                         palette=palette, legend=True)
            title = f'Customer Churn Rate ({choice})'
            plt.title(title, fontweight='bold', y=1.05)
            plt.xlabel('')    
            plt.ylabel('Percentage', fontweight='bold')
            plt.yticks(np.linspace(0, 1, 6), np.arange(0, 101, 20))
            if choice.lower() == 'payment method':
                plt.xticks(rotation=20)
            
            legend_labels = ['Stay', 'Leave']
            legend_handles = [Line2D([0], [0], color=palette[0], lw=3),
                              Line2D([0], [0], color=palette[1], lw=3)]
            plt.legend(legend_handles, legend_labels, loc='upper left', bbox_to_anchor=(1, 1))
            plt.show()
            
            st.pyplot(plt)
        with col2:
            for group in df_pred[feature].unique():                
                table = df_pred[df_pred[feature] == group]
                table = table['churn'].value_counts().to_frame()
                table.rename_axis('', inplace=True)
                table.index = table.index.map({0: 'Stay', 1:'Leave'})
                table['percentage'] = round(table['count'] / table['count'].sum() * 100, 2)
                
                st.write(f'{choice} ({group})')
                st.table(table.style.format("{:.2f}"))

    # Boxplots for numerical features
    elif choice.lower() in ['monthly charges', 'total charges', 'subscribed days',
                               'subscribed years', 'total internet services']:
        feature = '_'.join(choice.lower().split(' ')) 
        
        with col1:
            plt.figure(figsize=(2, 2))
            sns.boxplot(data=df_pred, x='churn', y=feature, hue='churn', legend=False,
                        palette=['steelblue', 'tomato'])
            plt.title(choice, fontsize=7, fontweight='bold')
            plt.xlabel('')
            plt.ylabel(choice, fontsize=6, fontweight='bold')
            plt.xticks([0, 1], ['Stay', 'Leave'], fontsize=6)
            plt.yticks(fontsize=6)
            plt.show()
            
            st.pyplot(plt)
        with col2:
            table = pd.concat([
                df_pred.query('churn == 0')[feature].describe(),
                df_pred.query('churn == 1')[feature].describe()
            ], axis=1).round(2)
            table.drop(index=['std', '25%', '75%'], inplace=True)
            table.rename(index={'50%': 'median'}, inplace=True)
            table.columns = ['Stay', 'Leave']

            st.write('#')
            st.table(table.style.format("{:.2f}"))
    else:
        st.empty()
