import pandas as pd
from cleaner import clean_data

def run_project():
    try:
        # Load the messy CSV file
        df = pd.read_csv('sample_input.csv')
        
        # Apply cleaning logic
        cleaned_df = clean_data(df)
        
        # Save to output file
        cleaned_df.to_csv('cleaned_output.csv', index=False)
        
        print("Success! The CSV file has been cleaned.")
        print(f"Original rows: {len(df)}")
        print(f"Cleaned rows: {len(cleaned_df)}")
        
    except FileNotFoundError:
        print("Error: 'sample_input.csv' not found. Please ensure the file exists.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    run_project()