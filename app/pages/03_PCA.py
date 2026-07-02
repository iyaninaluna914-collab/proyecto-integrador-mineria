import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Configuración de la página oficial
st.set_page_config(page_title="Reducción de Dimensionalidad - PCA", page_icon="🧬", layout="wide")

st.title("🧬 Reducción de Dimensionalidad: PCA")
st.markdown("""
El **Análisis de Componentes Principales (PCA)** simplifica la complejidad matemática del dataset, 
reduciendo los datos a dos dimensiones esenciales (PC1 y PC2) mientras retiene la mayor cantidad de varianza posible.
""")
st.markdown("---")

try:
    # Carga segura del dataset limpio
    df = pd.read_csv("data/processed/dataset_limpio.csv")

    st.subheader("🛠️ Preparación Matemática de los Datos")
    st.markdown("""
    Las variables cualitativas fueron codificadas y el set numérico fue **estandarizado** (media = 0, varianza = 1) para evitar distorsiones de escala en los componentes primarios.
    """)

    cols_numericas = ['age', 'monthly_watch_time_mins', 'customer_support_tickets']
    valid_cols = [col for col in cols_numericas if col in df.columns]

    if len(valid_cols) >= 2:
        X = df[valid_cols].dropna()
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)

        # Aplicación del Algoritmo PCA
        pca = PCA(n_components=2, random_state=42)
        X_pca = pca.fit_transform(X_scaled)

        df_pca = pd.DataFrame(X_pca, columns=['PC1', 'PC2'])
        
        if 'subscription_plan' in df.columns:
            df_pca['Plan'] = df.loc[X.index, 'subscription_plan'].astype(str).str.title()
        else:
            df_pca['Plan'] = 'Usuario'

        st.subheader("📊 Espacio Proyectado de Componentes Principales (PC1 vs PC2)")
        
        fig_pca, ax_pca = plt.subplots(figsize=(10, 5))
        sns.scatterplot(
            data=df_pca, 
            x='PC1', 
            y='PC2', 
            hue='Plan' if 'subscription_plan' in df.columns else None,
            palette='viridis', 
            alpha=0.8, 
            ax=ax_pca
        )
        
        plt.title('Proyección PCA del Comportamiento de Streaming', fontsize=12, pad=10)
        plt.xlabel('Componente Principal 1 (PC1)')
        plt.ylabel('Componente Principal 2 (PC2)')
        
        # CORRECCIÓN CLAVE: Usamos plt.grid (Matplotlib), NO st.grid
        plt.grid(True, linestyle='--', alpha=0.5)
        
        # Renderizado seguro en Streamlit
        st.pyplot(fig_pca)

        st.markdown("---")
        st.subheader("💡 Interpretación de los Patrones Visuales")
        st.markdown("""
        * **Formación de Patrones Diagonales Paralelos:** Las estructuras lineales separadas en bloques oblicuos demuestran que variables de peso categórico dividen rígidamente a la población en sub-grupos homogéneos.
        * **Identificación de Grupos:** El espacio vacío entre las franjas corrobora que los usuarios pertenecen a **perfiles de comportamiento discretos y bien estructurados**, útiles para segmentación y recomendación comercial.
        """)
        
        st.success(f"✅ Varianza explicada acumulada por componentes: {np.sum(pca.explained_variance_ratio_)*100:.2f}%")
        
    else:
        st.warning("Se necesitan al menos 2 variables numéricas para calcular el PCA.")

except Exception as e:
    st.error(f"Error al inicializar el módulo matemático de PCA: {e}")