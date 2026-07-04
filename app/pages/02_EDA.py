import pandas as pd

# =========================
# CARGA DE DATOS LIMPIOS
# =========================

def load_data():
    df = pd.read_csv("data/processed/dataset_limpio.csv")
    return df