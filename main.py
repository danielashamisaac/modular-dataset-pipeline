from pipeline.ingestion import load_data
from pipeline.profiler import profile_data
from pipeline.janitor import clean_data
from pipeline.exporter import export_data

def main():
    print("Starting Modular Dataset Pipeline...")
    
    # 1. Ingestion: Load raw data
    df_raw = load_data()
    
    # 2. Profiler: Inspect raw data metrics
    profile_data(df_raw)
    
    # 3. Janitor: Clean missing values
    df_cleaned = clean_data(df_raw)
    
    # 4. Profiler (Post-Cleaning check): Verify missing values are gone
    print("\n--- [VERIFICATION: POST-CLEANING PROFILE] ---")
    print(df_cleaned.isnull().sum())
    
    # 5. Exporter: Save the result
    export_data(df_cleaned)
    
    print("\nPipeline execution completed successfully!")

if __name__ == "__main__":
    main()