import pandas as pd

def clean_data(df):
    # Normalize column names
    df.columns = df.columns.str.lower().str.replace(' ', '_')
    
    # Drop empty rows
    df = df.dropna(how='all')
    
    # Drop duplicates
    df = df.drop_duplicates()
    
    # Trim whitespace from string cells
    df = df.map(lambda x: x.strip() if isinstance(x, str) else x)
    
    # Fill missing values
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].fillna('unknown')
        else:
            df[col] = df[col].fillna(0)
            
    return df