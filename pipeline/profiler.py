def profile_data(df):
    """Displays a preview, dimensions, and missing-value counts of the dataset."""
    print("\n--- [STAGE: DATA PROFILING] ---")
    
    print("\n1. First 5 Rows (Head):")
    print(df.head())
    
    print("\n2. Dataset Shape (Rows, Columns):")
    print(df.shape)
    
    print("\n3. Missing Values per Column:")
    print(df.isnull().sum())
    
    return df