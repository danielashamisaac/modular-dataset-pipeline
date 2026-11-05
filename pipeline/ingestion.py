import pandas as pd

def load_data(file_path="data/orders_raw.csv"):
    """Loads the raw customer orders CSV into a Pandas DataFrame."""
    df = pd.read_csv(file_path)
    return df