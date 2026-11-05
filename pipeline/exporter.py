def export_data(df, output_path="output/cleaned_orders.csv"):
    """Exports the cleaned DataFrame to a CSV file without the index column."""
    print("\n--- [STAGE: DATA EXPORT] ---")
    df.to_csv(output_path, index=False)
    print(f"Cleaned dataset successfully saved to {output_path}")