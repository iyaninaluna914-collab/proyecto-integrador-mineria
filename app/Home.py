import streamlit as st

# 1. Configuración de la página con diseño amplio
st.set_page_config(page_title="Dashboard Streaming - Portada", page_icon="🎬", layout="wide")

# ==========================================
# 2. ENCABEZADO PRINCIPAL DE LA PORTADA
# ==========================================
col_logo, col_titulo = st.columns([1, 6])
with col_logo:
    st.markdown("<h1 style='text-align: center; font-size: 75px; margin: 0;'>🎬</h1>", unsafe_allowed_html=True)
with col_titulo:
    st.title("Proyecto Integrador - Minería de Datos I")
    st.subheader("Análisis Inteligente y Perfilado en Plataformas de Streaming")

st.markdown("---")

# ==========================================
# 3. DATOS DE LOS INTEGRANTES Y CURSADA
# ==========================================
# Usamos un contenedor nativo seguro para agrupar la información institucional
with st.container():
    col_info1, col_info2 = st.columns(2)
    
    with col_info1:
        st.markdown("### 👥 Integrantes del Equipo")
        st.write("• **Luna, Yanina** — *Desarrollo de Pipeline ETL y Modelado PCA*")
        st.write("• **Luna, Karina** — *Análisis Exploratorio (EDA) y Documentación Técnica*")
        
    with col_info2:
        st.markdown("### 🏫 Información Académica")
        st.write("• **Comisión / Turno:** Turno Mañana")
        st.write("• **Fecha de Entrega:** Julio 2026")
        st.write("• **Estado del Tablero:** Desplegado de forma automatizada")

st.markdown("---")

# ==========================================
# 4. RESUMEN EJECUTIVO Y OBJETIVOS
# ==========================================
st.markdown("### 📝 Resumen del Proyecto")
st.markdown("""
Este tablero analítico interactivo procesa los registros de comportamiento de nuestra base de usuarios con el objetivo 
de transformar datos brutos en conocimiento estratégico. A lo largo del menú lateral, se documenta el ciclo completo 
de ciencia de datos aplicado sobre la plataforma de streaming:
""")

# Bloques destacados nativos para explicar cada sección del menú lateral
col_p1, col_p2, col_p3 = st.columns(3)

with col_p1:
    st.markdown("#### 📄 1. Dataset")
    st.caption("Auditoría estructural de la base de datos limpia y diccionario técnico de variables comerciales.")

with col_p2:
    st.markdown("#### 📈 2. EDA")
    st.caption("Visualización estadística segmentada en análisis Univariado, Bivariado y correlaciones complejas.")

with col_p3:
    st.markdown("#### 🧬 3. PCA")
    st.caption("Reducción de dimensionalidad mediante aprendizaje no supervisado para detectar perfiles de consumo.")

st.markdown("---")

# ==========================================
# 5. ENLACES OBLIGATORIOS (GitHub)
# ==========================================
st.markdown("### 🔗 Acceso al Repositorio Oficial")
st.write("De acuerdo con los requerimientos de la cátedra, podés revisar el código de origen y las transformaciones en el siguiente enlace público:")

# Botón nativo estándar (100% seguro contra caídas)
st.link_button("📂 Ir al Repositorio de GitHub", "https://github.com/iyanaluna914-collab/proyecto-integrador-mineria")

st.markdown(" ")
st.info("💡 **Indicación:** Utilizá el panel de navegación izquierdo para explorar secuencialmente cada etapa de la defensa.")