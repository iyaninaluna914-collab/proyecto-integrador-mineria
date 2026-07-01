import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de la página
st.set_page_config(page_title="02 EDA - Análisis Exploratorio", page_icon="📈", layout="wide")

st.title("📈 Análisis Exploratorio de Datos (EDA)")
st.markdown("""
En este módulo realizamos un diagnóstico estadístico y visual del dataset para identificar patrones, 
comportamientos anómalos o correlaciones ocultas entre el perfil demográfico del usuario y sus hábitos de consumo.
""")
st.markdown("---")

try:
    # Cargar datos desde la ruta estándar
    df = pd.read_csv("data/processed/dataset_limpio.csv")
    sns.set_theme(style="whitegrid")

    # Creamos las tres pestañas organizadas según la complejidad del análisis
    tab1, tab2, tab3 = st.tabs([
        "📊 Análisis Univariado (Una Variable)", 
        "📉 Análisis Bivariado (Dos Variables)", 
        "🧮 Análisis Multivariado (Múltiples Variables)"
    ])

    # ==========================================
    # PESTAÑA 1: ANÁLISIS UNIVARIADO
    # ==========================================
    with tab1:
        st.subheader("Análisis Univariado: Comportamiento Individual de Variables")
        st.markdown("""
        El análisis univariado nos permite estudiar la distribución, tendencia central y dispersión 
        de una sola variable a la vez, aislando su comportamiento.
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 1. Distribución de la Edad")
            fig1, ax1 = plt.subplots(figsize=(6, 4))
            sns.histplot(data=df, x='age', bins=20, kde=True, color='#1f77b4', ax=ax1)
            plt.title("Histograma de Edades de Usuarios")
            plt.xlabel("Edad")
            plt.ylabel("Frecuencia (Cantidad de Usuarios)")
            st.pyplot(fig1)
            st.markdown("""
            **💡 Hallazgo Analítico:** El histograma revela la concentración de usuarios según su edad. Se observa una distribución de tipo 
            unimodal donde la mayor masa de clientes se agrupa en un rango específico de edad, permitiendo 
            identificar nuestro segmento demográfico principal (Target).
            """)
            
        with col2:
            st.markdown("#### 2. Distribución de Planes de Suscripción")
            # Normalizamos un poco el texto para que el gráfico univariado se vea más limpio
            df_sub = df.copy()
            df_sub['subscription_plan'] = df_sub['subscription_plan'].astype(str).str.title().str.strip()
            
            fig2, ax2 = plt.subplots(figsize=(6, 4))
            sns.countplot(data=df_sub, x='subscription_plan', palette='Blues_r', order=df_sub['subscription_plan'].value_counts().index, ax=ax2)
            plt.title("Distribución por Tipo de Plan")
            plt.xlabel("Plan de Suscripción")
            plt.ylabel("Cantidad de Usuarios")
            plt.xticks(rotation=45)
            st.pyplot(fig2)
            st.markdown("""
            **💡 Hallazgo Analítico:** Este gráfico de barras expone la preferencia comercial de los usuarios. Permite evaluar el volumen de 
            clientes en planes económicos (Basic) frente a los de mayor valor (Premium), clave para proyecciones de ingresos.
            """)

    # ==========================================
    # PESTAÑA 2: ANÁLISIS BIVARIADO
    # ==========================================
    with tab2:
        st.subheader("Análisis Bivariado: Relación entre dos Variables")
        st.markdown("""
        El análisis bivariado busca explorar la interacción o dependencia mutua entre dos variables distintas, 
        evaluando cómo cambian los hábitos según otra métrica.
        """)
        
        # Gráfico 3: Edad vs Tiempo de Uso (Scatter)
        st.markdown("#### 1. Relación entre Edad y Tiempo de Visualización Mensual")
        fig3, ax3 = plt.subplots(figsize=(10, 5))
        sns.scatterplot(data=df, x='age', y='monthly_watch_time_mins', alpha=0.6, color='#2ca02c', ax=ax3)
        plt.title("Dispersión: Edad vs. Tiempo de Uso Mensual")
        plt.xlabel("Edad")
        plt.ylabel("Minutos de Visualización Mensuales")
        st.pyplot(fig3)
        st.markdown("""
        **💡 Hallazgo Analítico:** Al cruzar la edad con el tiempo de consumo mediante un gráfico de dispersión (Scatterplot), podemos verificar si 
        los usuarios más jóvenes pasan más tiempo en la plataforma que los adultos. La presencia de líneas horizontales 
        densas o patrones agrupados sugiere comportamientos estandarizados de consumo o anomalías en la captura de datos (Outliers).
        """)
        st.markdown("---")
        
        # Gráfico 4: Género vs Tiempo de Uso (Barras/Boxplot alternativo)
        st.markdown("#### 2. Consumo Mensual según el Género Favorito")
        fig4, ax4 = plt.subplots(figsize=(12, 5))
        # Limpieza rápida para el eje X
        df_gen = df.copy()
        df_gen['favorite_genre'] = df_gen['favorite_genre'].astype(str).str.upper().str.strip()
        
        sns.countplot(data=df_gen, x='favorite_genre', palette='viridis', order=df_gen['favorite_genre'].value_counts().index, ax=ax4)
        plt.title("Volumen de Usuarios por Categoría de Género Favorito")
        plt.xlabel("Género Favorito")
        plt.ylabel("Cantidad de Usuarios")
        plt.xticks(rotation=90)
        st.pyplot(fig4)
        st.markdown("""
        **💡 Hallazgo Analítico:** Esta visualización bivariada contrasta las diferentes categorías de contenido elegidas por la audiencia. Permite 
        conocer con precisión qué géneros específicos retienen más la atención y cuáles tienen un rendimiento marginal en la plataforma.
        """)

    # ==========================================
    # PESTAÑA 3: ANÁLISIS MULTIVARIADO
    # ==========================================
    with tab3:
        st.subheader("Análisis Multivariado: Matriz de Correlación Numérica")
        st.markdown("""
        El análisis multivariado examina simultáneamente múltiples variables para descubrir estructuras complejas 
        de correlación lineal o dependencias en el sistema de datos.
        """)
        
        # Seleccionamos solo las numéricas como se ve en tu heatmap original
        cols_numericas = ['user_id', 'age', 'monthly_watch_time_mins', 'customer_support_tickets']
        # Nos aseguramos de que existan en el dataframe
        num_df = df[[col for col in cols_numericas if col in df.columns]].dropna()
        
        if not num_df.empty:
            fig5, ax5 = plt.subplots(figsize=(8, 6))
            matriz_corr = num_df.corr()
            
            # Dibujamos tu Heatmap clásico
            sns.heatmap(matriz_corr, annot=True, cmap='coolwarm', fmt=".4f", linewidths=0.5, vmin=-1, vmax=1, ax=ax5)
            plt.title("Matriz de Correlación de Pearson")
            st.pyplot(fig5)
            
            st.markdown("""
            **💡 Hallazgo Analítico del Mapa de Calor (Heatmap):** * Los valores oscilan entre **-1** (correlación negativa perfecta) y **+1** (correlación positiva perfecta), siendo **0** la ausencia total de relación lineal.
            * En nuestra matriz, los valores cercanos a cero (ej. `0.0029` o `-0.0037`) demuestran que **no existe una relación lineal fuerte** entre la edad del usuario, los minutos consumidos y la cantidad de tickets de soporte técnico. 
            * Esto indica que el comportamiento de consumo y los problemas técnicos ocurren de manera independiente a la edad biológica del suscriptor.
            """)
        else:
            st.warning("No se encontraron variables numéricas suficientes para generar el Mapa de Calor.")

except Exception as e:
    st.error(f"Error al procesar el módulo EDA: {e}")