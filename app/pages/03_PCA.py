import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

st.title("📉 PCA")

df = pd.read_csv("data/processed/dataset_limpio.csv")

cols = ["age", "monthly_watch_time_mins", "customer_support_tickets"]

X = df[cols]

# Escalamiento
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# PCA
pca = PCA(n_components=2)
components = pca.fit_transform(X_scaled)

df_pca = pd.DataFrame(components, columns=["PC1", "PC2"])

# gráfico
fig, ax = plt.subplots()
ax.scatter(df_pca["PC1"], df_pca["PC2"])
st.pyplot(fig)

st.subheader("Varianza explicada")
st.write(pca.explained_variance_ratio_.sum())
   
