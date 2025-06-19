import pandas as pd

def load_training_data():
    '''
    Loads and prepares the historical data for Store 1 from the raw CSV files.
    this is used by streamlit to get the history for plotting    
    '''
    sales = pd.read_csv('data/train.csv')
    stores = pd.read_csv('data/stores.csv')
    features = pd.read_csv('data/features.csv')

    # merge the dataframes 

    df = pd.merge(sales, stores, on='Store', how='left')
    df = pd.merge(df, features, on=['Store', 'Date', 'IsHoliday'], how='left')

    df['Date'] = pd.to_datetime(df['Date'])

    df_prophet = df.rename(columns={
        'Date':'ds',
        'Weekly_Sales':'y'
    })

    store1_df = df_prophet[df_prophet['Store']==1][['ds','y']].copy()

    return store1_df



