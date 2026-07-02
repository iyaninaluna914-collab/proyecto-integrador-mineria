import streamlit as st

# 1. Configuración de la página con diseño amplio
st.set_page_config(page_title="Dashboard Streaming - Portada", page_icon="🎬", layout="wide")

# ==========================================
# INTERFAZ PREMIUM (CSS CONTROLADO)
# ==========================================
st.markdown("""
    <style>
    .main-card {
        background-color: #f8f9fa;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
        border: 1px solid #e9ecef;
        margin-bottom: 25px;
    }
    .highlight-text {
        color: #1f77b4;
        font-weight: bold;
    }
    </style>
""", unsafe_allowed_html=True)


# ==========================================
# 2. ENCABEZADO PRINCIPAL (BANNER INFORMATIVO)
# ==========================================
col_logo, col_titulo = st.columns([1, 6])
with col_logo:
    st.markdown("<h1 style='text-align: center; font-size: 80px; margin: 0;'>🎬</h1>", unsafe_allowed_html=True)
with col_titulo:
    st.title("Proyecto Integrador - Minería de Datos I")
    st.subheader("Análisis de Usuarios y Patrones de Consumo en Plataformas de Streaming")

st.markdown("---")


# ==========================================
# 3. PRESENTACIÓN DEL EQUIPO (TARJETA VISUAL)
# ==========================================
st.markdown("<div class='main-card'>", unsafe_allowed_html=True)

col_info1, col_info2 = st.columns(2)
with col_info1:
    st.markdown("### 👥 Integrantes del Proyecto")
    st.markdown("""
    * 👩‍💻 **Luna, Yanina** — *Desarrollo de Pipeline ETL y Modelado Avanzado PCA*
    * 👩‍💻 **Luna, Karina** — *Análisis Exploratorio Visual (EDA) y Calidad de Datos*
    """)
with col_info2:
    st.markdown("### 🏫 Información de Cursada")
    st.markdown("""
    * 📅 **Fecha de Entrega:** Julio 2026
    * 🌅 **Comisión / Turno:** Turno Mañana
    * 🏫 **Asignatura:** Minería de Datos I
    """)

st.markdown("</div>", unsafe_allowed_html=True)


# ==========================================
# 4. RESUMEN EJECUTIVO DEL PROYECTO
# ==========================================
st.markdown("### 📝 Resumen Ejecutivo")
st.markdown("""
Este proyecto consiste en el **análisis exploratorio avanzado** y el perfilamiento estratégico de una base de datos 
perteneciente a una plataforma de streaming musical y de video. A lo largo del tablero interactivo, implementamos 
las fases metodológicas estándar de un proceso de ciencia de datos:

1. **Fase 1 (Dataset):** Auditoría estructural del archivo fuente y visualización de la muestra analítica.
2. **Fase 2 (EDA):** Examinación estadística de variables mediante análisis <span class='highlight-text'>Univariado</span>, <span class='highlight-text'>Bivariado</span> y <span class='highlight-text'>Multivariado</span>.
3. **Fase 3 (PCA):** Reducción de dimensionalidad lineal para descubrir la estructura de agrupamiento natural de los usuarios.
""", unsafe_allowed_html=True)

st.markdown("---")


# ==========================================
# 5. ENLACES OFICIALES Y ACCESO AL CÓDIGO (GitHub Obligatorio)
# ==========================================
st.markdown("### 🔗 Entrega Oficial y Respaldo Técnico")
st.write("De acuerdo con los requerimientos académicos, podés auditar el código fuente, notebooks y transformaciones en nuestro repositorio:")

# Botón interactivo premium de Streamlit
st.link_button("📂 Acceder al Repositorio en GitHub", "https://github.com/iyanaluna914-collab/proyecto-integrador-mineria")

st.markdown(" ")
st.info("💡 **Guía de navegación:** Utilizá el menú de la barra lateral izquierda para desplazarte de manera interactiva por las diferentes pestañas del informe analítico.")
