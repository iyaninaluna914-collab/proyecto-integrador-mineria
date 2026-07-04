import streamlit as st
import pandas as pd

# 1. Configuración de la página inicial con diseño amplio
st.set_page_config(page_title="Dashboard Streaming - Inicio", page_icon="🎬", layout="wide")

# ==========================================
# 2. CARGA DE DATOS PRINCIPAL
# ==========================================
try:
    df = pd.read_csv("data/processed/dataset_limpio.csv")
    st.session_state['df'] = df # Compartimos los datos con la pestaña de gráficos
    
    # ==========================================
    # 3. CABECERA CON DISEÑO Y BIENVENIDA
    # ==========================================
    st.title("🎬 Plataforma de Streaming: Panel Analítico Integrador")
    st.markdown("""
    Bienvenidos al portal de análisis inteligente del comportamiento de nuestros usuarios. Esta aplicación interactiva 
    procesa grandes volúmenes de datos brutos para identificar tendencias de consumo, segmentar audiencias y optimizar 
    la toma de decisiones estratégicas sobre el contenido de la plataforma.
    """)
    st.markdown("---")

    # ==========================================
    # 4. AGREGAMOS SECCIÓN DE MÉTRICAS CLAVE (KPIs Visuales)
    # ==========================================
    st.subheader("📊 Indicadores Clave del Negocio (Muestra Comercial)")
    
    # Creamos 3 columnas bonitas para mostrar números grandes
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(label="Total de Usuarios Analizados", value=f"{df.shape[0]:,}".replace(",", "."))
    
    with col2:
        if 'monthly_watch_time_mins' in df.columns:
            promedio_minutos = int(df['monthly_watch_time_mins'].mean())
            st.metric(label="Consumo Promedio Mensual", value=f"{promedio_minutos} min")
        else:
            st.metric(label="Consumo Promedio", value="N/A")
            
    with col3:
        if 'favorite_genre' in df.columns:
            genero_top = df['favorite_genre'].mode()[0].title()
            st.metric(label="Género Más Popular", value=genero_top)
        else:
            st.metric(label="Género Top", value="N/A")

    st.markdown("---")

    # ==========================================
    # 5. ESTRUCTURA Y VISTA PREVIA CON PESTAÑAS (Tabs)
    # ==========================================
    st.subheader("🔍 Exploración Estructurada de la Base de Datos")
    
    # Organizamos la info en pestañas para que no sature la vista
    tab1, tab2 = st.tabs(["📄 Vista Previa de Registros", "🛠️ Ficha Técnica de Variables"])
    
    with tab1:
        st.markdown("**Primeros registros limpios de la base de datos:**")
        # Mostramos la tabla ocupando el ancho completo de la pantalla
        st.dataframe(df.head(10), use_container_width=True)
    
    with tab2:
        st.markdown("**Descripción técnica del contenido del dataset:**")
        # Creamos una tabla manual explicativa bien formateada
        info_columnas = {
            "Nombre de Variable": list(df.columns),
            "Tipo de Dato": [str(df[col].dtype) for col in df.columns],
            "Ejemplo de Registro": [str(df[col].iloc[0]) for col in df.columns]
        }
        st.table(pd.DataFrame(info_columnas))

    st.markdown("---")

    # ==========================================
    # 6. BANNER INFORMATIVO HACIA EL EDA
    # ==========================================
    # Usamos un bloque de información destacado para invitar a ir a los gráficos
    st.info("💡 **Próximo Paso Analítico:** Para examinar las gráficas de distribución, análisis de dispersión (Boxplots) y los perfiles cruzados por edad, navegá al menú lateral izquierdo y seleccioná la pestaña **02 EDA**.")

except Exception as e:
    st.error("⚠️ Error crítico: No se pudieron mapear los datos del proyecto.")
    st.markdown(f"""
    **Instrucciones de soporte:**
    1. Asegurate de que el archivo `dataset_limpio.csv` esté dentro de la ruta: `data/processed/` en tu repositorio.
    2. Detalle del error arrojado por el sistema: `{e}`
    """)