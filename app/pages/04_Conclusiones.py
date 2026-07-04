import streamlit as st

# =========================
# CONFIGURACIÓN
# =========================
st.set_page_config(
    page_title="Conclusiones del Proyecto",
    page_icon="🎯",
    layout="wide"
)

# =========================
# TÍTULO
# =========================
st.title("🎯 Conclusiones y Cierre del Proyecto")

st.markdown("""
Este apartado resume los principales hallazgos obtenidos a lo largo del pipeline de Minería de Datos,
incluyendo ETL, análisis exploratorio (EDA) y reducción de dimensionalidad (PCA).
""")

st.markdown("---")

# =========================
# SECCIÓN 1 - ETL
# =========================
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🛠️ 1. Impacto de la Limpieza (ETL)")
    st.markdown("""
    El proceso de limpieza permitió unificar categorías inconsistentes, eliminar duplicados y tratar valores nulos.
    Esto mejoró significativamente la calidad del dataset, asegurando resultados más confiables en el análisis posterior.
    """)

# =========================
# SECCIÓN 2 - CORRELACIONES
# =========================
with col2:
    st.markdown("### 📈 2. Interpretación de Correlaciones")
    st.markdown("""
    El análisis de correlación mostró que variables como el tiempo de uso y los tickets de soporte
    no presentan una relación lineal fuerte con la edad de los usuarios, lo que indica independencia entre estas variables.
    """)

st.markdown("---")

# =========================
# SECCIÓN 3 - PCA
# =========================
st.markdown("### 🧬 3. Valor Estratégico del PCA")

st.markdown("""
El análisis de componentes principales permitió reducir la dimensionalidad del dataset,
visualizando el comportamiento de los usuarios en un espacio simplificado (PC1 y PC2).

Esto facilitó la identificación de patrones generales de consumo y posibles segmentos de usuarios,
lo que resulta útil para estrategias de recomendación y segmentación.
""")

st.markdown("---")

# =========================
# CIERRE FINAL
# =========================
st.success("🏁 Fin del proyecto. Se completaron todas las etapas: ETL, EDA y PCA de manera satisfactoria.")