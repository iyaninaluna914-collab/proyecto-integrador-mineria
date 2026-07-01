import streamlit as st
import pandas as pd

# 1. Configuración de la página con diseño amplio
st.set_page_config(page_title="Dashboard Streaming - Portada", page_icon="🎬", layout="wide")

# ==========================================
# EXTRA: DISEÑO DE INTERFAZ PREMIUM (CSS)
# ==========================================
# Este bloque cambia el diseño plano de Streamlit por tarjetas modernas con sombras
st.markdown("""
    <style>
    /* Estilo para las tarjetas de métricas */
    [data-testid="stMetricBlock"] {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
        border: 1px solid #e9ecef;
        transition: transform 0.2s;
    }
    [data-testid="stMetricBlock"]:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.1);
    }
    /* Estilo para los títulos de pestañas */
    button[data-baseweb="tab"] {
        font-size: 16px;
        font-weight: 600;
    }
    </style>
""", unsafe_allowed_html=True)


# ==========================================
# 2. ENCABEZADO PRINCIPAL (BANNER INFORMATIVO)
# ==========================================
# Usamos columnas para centrar y dar aire al diseño
col_logo, col_titulo = st.columns([1, 5])
with col_logo:
    st.markdown("<h1 style='text-align: center; font-size: 80px; margin: 0;'>📊</h1>", unsafe_allowed_html=True)
with col_titulo:
    st.title("Proyecto Integrador: Minería de Datos I")
    st.subheader("Análisis Inteligente y Perfilado en Plataformas de Streaming")

st.markdown("---")


# ==========================================
# 3. PRESENTACIÓN DEL EQUIPO (TARJETA VISUAL)
# ==========================================
# Diseñamos un bloque prolijo para los datos de entrega
with st.container():
    col_info1, col_info2 = st.columns(2)
    with col_info1:
        st.markdown("### 👥 Integrantes del Proyecto")
        st.markdown("""
        * 👩‍💻 **Luna, Yanina** — *Desarrollo de Pipeline ETL y Modelado PCA*
        * 👩‍💻 **Luna, Karina** — *Análisis Exploratorio (EDA) y Documentación Estructurada*
        """)
    with col_info2:
        st.markdown("### 🏫 Contexto Académico")
        st.markdown("""
        * 📅 **Fecha de Entrega:** Julio 2026
        * 🌅 **Comisión:** Turno Mañana
        * 🔍 **Estado del Arte:** Pipeline Automatizado y Desplegado en la Nube
        """)

st.markdown("---")


# ==========================================
# 4. CARGA DE DATOS Y ENTRADA DE KPIs
# ==========================================
try:
    df = pd.read_csv("data/processed/dataset_limpio.csv")
    st.session_state['df'] = df 

    st.markdown("### 📈 Indicadores Clave de la Muestra Comercial")
    st.write("Métricas de negocio procesadas en tiempo real a partir del set de datos limpio:")
    
    # Renderizamos las tarjetas con el nuevo estilo CSS que aplicamos arriba
    kpi1, kpi2, kpi3 = st.columns(3)
    
    with kpi1:
        st.metric(
            label="👥 Volumen de Usuarios", 
            value=f"{df.shape[0]:,}".replace(",", "."),
            help="Cantidad total de registros únicos validados en el dataset."
        )
    
    with kpi2:
        if 'monthly_watch_time_mins' in df.columns:
            promedio_minutos = int(df['monthly_watch_time_mins'].mean())
            st.metric(
                label="⏳ Consumo Promedio", 
                value=f"{promedio_minutos} min/mes",
                help="Tiempo medio de permanencia de los usuarios frente a la pantalla."
            )
            
    with kpi3:
        if 'favorite_genre' in df.columns:
            genero_top = df['favorite_genre'].mode()[0].upper()
            st.metric(
                label="🎬 Categoría Líder", 
                value=genero_top,
                help="Género cinematográfico o televisivo con mayor engagement."
            )

    st.markdown("---")

    # ==========================================
    # 5. EXPLORACIÓN ESTÉTICA DE LA DATA
    # ==========================================
    st.markdown("### 🔍 Estructura General del Dataset")
    
    tab_data, tab_variables = st.tabs(["📄 Vista de Registros Limpios", "🛠️ Matriz de Atributos"])
    
    with tab_data:
        st.markdown("A continuación se exponen las primeras filas del dataframe procesado listo para el modelado:")
        st.dataframe(df.head(6), use_container_width=True)
    
    with tab_variables:
        st.markdown("Diccionario de datos simplificado para la defensa del proyecto:")
        info_columnas = {
            "Variable Analizada": list(df.columns),
            "Tipo de Dimensión": [str(df[col].dtype).replace('object', 'Categoría / Texto').replace('int64', 'Numérica Entera').replace('float64', 'Numérica Continua') for col in df.columns],
            "Muestra Técnica": [str(df[col].iloc[0]) for col in df.columns]
        }
        st.table(pd.DataFrame(info_columnas))

    # Banner inferior de navegación
    st.markdown(" ")
    st.info("💡 **Guía de navegación:** Utilizá el menú desplegable de la barra lateral izquierda para explorar las etapas secuenciales del proyecto: **02 Calidad y Limpieza**, **03 EDA (Gráficos)** y el modelo avanzado de **04 PCA**.")

except Exception as e:
    st.error("⚠️ Error de sincronización: No se encontraron los datos del repositorio.")
    st.write(f"Detalle técnico: {e}")
    # ==========================================
# 6. ENLACES OFICIALES Y ACCESO AL CÓDIGO
# ==========================================
st.markdown("---")
st.markdown("### 🔗 Entrega Oficial del Proyecto")
st.write("Podés acceder al código fuente completo, los notebooks de desarrollo y el historial de cambios en nuestro repositorio público:")

# Opción A: Un botón grande y llamativo que simula un botón de comando
st.link_button("📂 Ir al Repositorio de GitHub", "https://github.com/iyanaluna914-collab/proyecto-integrador-mineria")

# Opción B: Por si acaso, un enlace de texto clásico bien formateado abajo
st.markdown("""
* 🌐 **Link directo:** [https://github.com/iyanaluna914-collab/proyecto-integrador-mineria](https://github.com/iyanaluna914-collab/proyecto-integrador-mineria)
* 🛠️ **Rama principal:** `main`
""")