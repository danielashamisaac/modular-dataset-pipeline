def clean_data(df):
    """Fills missing values based on specified column rules and returns the cleaned DataFrame."""
    print("\n--- [STAGE: DATA CLEANING (JANITOR)] ---")
    
    # Fill missing text columns with 'Unknown'
    df["customer"] = df["customer"].fillna("Unknown")
    df["city"] = df["city"].fillna("Unknown")
    
    # Fill missing numeric columns with 0
    df["orders"] = df["orders"].fillna(0)
    df["amount"] = df["amount"].fillna(0)
    
    print("Missing values successfully cleaned according to rules.")
    return df