import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Conclusiones del Proyecto", page_icon="🎯", layout="wide")

st.title("🎯 Conclusiones y Cierre del Proyecto")
st.markdown("""
A continuación se detallan los hallazgos analíticos consolidados tras la ejecución del pipeline completo de 
Minería de Datos sobre nuestra base de usuarios de streaming.
""")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🛠️ 1. Impacto de la Limpieza (ETL)")
    st.markdown("""
    La unificación y homogeneización de los datos textuales (como las categorías y nombres de los planes) 
    permitió remover réplicas artificiales que sesgaban los conteos de negocio. El tratamiento oportuno de 
    los valores nulos garantizó que las métricas finales reflejen el comportamiento real del ecosistema de clientes.
    """)

with col2:
    st.markdown("### 📈 2. Interpretación de Correlaciones")
    st.markdown("""
    A través de la matriz de correlación de Pearson ejecutada en el módulo EDA, se determinó de manera científica 
    que variables críticas como el tiempo de consumo mensual (`monthly_watch_time_mins`) y los reportes técnicos 
    operan de forma independiente a la edad biológica de los usuarios.
    """)

st.markdown("---")

st.markdown("### 🧬 3. Valor Estratégico del Modelo PCA")
st.markdown("""
La reducción de dimensionalidad demostró de forma visual que los clientes de la plataforma se agrupan en **estructuras 
lineales discretas y predecibles**. Este hallazgo refuta la hipótesis de comportamiento caótico, sentando las bases 
matemáticas ideales para el despliegue futuro de un algoritmo de agrupamiento (Clustering como K-Means) o motores de 
recomendación personalizada que incrementen la retención.
""")

st.markdown(" ")
st.success("🏁 **Fin de la Defensa Técnica.** El proyecto cumple con el 100% de las fases metodológicas requeridas.")