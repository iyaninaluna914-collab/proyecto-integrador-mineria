import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# =========================
# CONFIGURACIÓN
# =========================
st.set_page_config(
    page_title="PCA - Reducción de Dimensionalidad",
    page_icon="🧬",
    layout="wide"
)

st.title("🧬 Reducción de Dimensionalidad: PCA")

st.markdown("""
El **Análisis de Componentes Principales (PCA)** permite reducir la complejidad del dataset
resumiendo la información en dos componentes principales (PC1 y PC2).
""")

st.markdown("---")

# =========================
# CARGA DE DATOS
# =========================
try:
    df = pd.read_csv("data/processed/dataset_limpio.csv")
    sns.set_theme(style="whitegrid")

    st.subheader("🛠️ Preparación de datos")

    st.write("""
    Se seleccionan variables numéricas y se aplica estandarización para asegurar que todas
    las variables tengan la misma escala antes del PCA.
    """)

    # =========================
    # VARIABLES NUMÉRICAS
    # =========================
    cols_numericas = [
        "age",
        "monthly_watch_time_mins",
        "customer_support_tickets"
    ]

    cols_validas = [c for c in cols_numericas if c in df.columns]

    if len(cols_validas) >= 2:

        # =========================
        # PREPARACIÓN
        # =========================
        X = df[cols_validas].dropna()

        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        # =========================
        # PCA
        # =========================
        pca = PCA(n_components=2, random_state=42)
        componentes = pca.fit_transform(X_scaled)

        df_pca = pd.DataFrame(componentes, columns=["PC1", "PC2"])

        # agregar plan si existe
        if "subscription_plan" in df.columns:
            df_pca["Plan"] = df.loc[X.index, "subscription_plan"].astype(str).str.title()
        else:
            df_pca["Plan"] = "Usuario"

        # =========================
        # GRAFICO PCA
        # =========================
        st.subheader("📊 Proyección PCA (PC1 vs PC2)")

        fig, ax = plt.subplots(figsize=(10, 5))

        sns.scatterplot(
            data=df_pca,
            x="PC1",
            y="PC2",
            hue="Plan",
            palette="viridis",
            alpha=0.7,
            ax=ax
        )

        ax.set_title("PCA del comportamiento de usuarios")
        ax.set_xlabel("Componente Principal 1 (PC1)")
        ax.set_ylabel("Componente Principal 2 (PC2)")
        ax.grid(True, linestyle="--", alpha=0.4)

        st.pyplot(fig)

        # =========================
        # VARIANZA EXPLICADA
        # =========================
        st.subheader("📉 Varianza explicada")

        varianza_total = np.sum(pca.explained_variance_ratio_) * 100

        st.write(f"Varianza explicada total: **{varianza_total:.2f}%**")

        fig2, ax2 = plt.subplots()

        ax2.bar(
            ["PC1", "PC2"],
            pca.explained_variance_ratio_,
            color="royalblue"
        )

        ax2.set_title("Varianza explicada por componente")
        ax2.set_ylabel("Proporción de varianza")

        st.pyplot(fig2)

        # =========================
        # INTERPRETACIÓN
        # =========================
        st.subheader("💡 Interpretación")

        st.write("""
        El PCA permite reducir la dimensionalidad del dataset manteniendo la mayor parte de la información.

        - PC1 concentra la mayor variabilidad del comportamiento de los usuarios.
        - PC2 complementa la información capturada por el primer componente.
        - La proyección permite identificar posibles agrupamientos de usuarios según su comportamiento.
        """)

    else:
        st.warning("Se necesitan al menos 2 variables numéricas para aplicar PCA.")

except Exception as e:
    st.error(f"Error al ejecutar PCA: {e}")