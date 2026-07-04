import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =========================
# CONFIGURACIÓN
# =========================
st.set_page_config(
    page_title="02 EDA - Análisis Exploratorio",
    page_icon="📈",
    layout="wide"
)

st.title("📈 Análisis Exploratorio de Datos (EDA)")
st.markdown("""
Este módulo analiza el comportamiento de los usuarios mediante visualizaciones
univariadas, bivariadas y multivariadas para identificar patrones relevantes.
""")

st.markdown("---")

# =========================
# CARGA DE DATOS
# =========================
try:
    df = pd.read_csv("data/processed/dataset_limpio.csv")
    sns.set_theme(style="whitegrid")

    # ======================================================
    # TABS
    # ======================================================
    tab1, tab2, tab3 = st.tabs([
        "📊 Univariado",
        "📉 Bivariado",
        "🧮 Multivariado"
    ])

    # =========================
    # TAB 1 - UNIVARIADO
    # =========================
    with tab1:
        st.subheader("Distribución de variables individuales")

        col1, col2 = st.columns(2)

        # -------- Edad --------
        with col1:
            st.markdown("### 📌 Edad de usuarios")
            fig1, ax1 = plt.subplots(figsize=(6,4))

            sns.histplot(df["age"], bins=20, kde=True, ax=ax1)
            ax1.set_title("Distribución de Edad")
            ax1.set_xlabel("Edad")
            ax1.set_ylabel("Frecuencia")

            st.pyplot(fig1)

            st.write("""
            Se observa la distribución de edades de los usuarios,
            identificando el segmento etario principal de la plataforma.
            """)

        # -------- Plan --------
        with col2:
            st.markdown("### 📌 Plan de suscripción")

            df["subscription_plan"] = df["subscription_plan"].astype(str).str.title().str.strip()

            fig2, ax2 = plt.subplots(figsize=(6,4))

            sns.countplot(
                data=df,
                x="subscription_plan",
                order=df["subscription_plan"].value_counts().index,
                ax=ax2
            )

            ax2.set_title("Distribución de Planes")
            ax2.set_xlabel("Plan")
            ax2.set_ylabel("Usuarios")

            st.pyplot(fig2)

            st.write("""
            Se observa la distribución de usuarios según su tipo de plan,
            permitiendo analizar preferencias de suscripción.
            """)

    # =========================
    # TAB 2 - BIVARIADO
    # =========================
    with tab2:
        st.subheader("Relación entre variables")

        # -------- Edad vs uso --------
        st.markdown("### 📌 Edad vs Tiempo de uso")

        fig3, ax3 = plt.subplots(figsize=(10,5))

        sns.scatterplot(
            data=df,
            x="age",
            y="monthly_watch_time_mins",
            alpha=0.5,
            ax=ax3
        )

        ax3.set_title("Edad vs Tiempo de Uso Mensual")
        ax3.set_xlabel("Edad")
        ax3.set_ylabel("Minutos de uso")

        st.pyplot(fig3)

        st.write("""
        Se analiza la relación entre la edad del usuario y el tiempo de consumo mensual,
        observando patrones de comportamiento.
        """)

        st.markdown("---")

        # -------- Género --------
        st.markdown("### 📌 Género favorito")

        df["favorite_genre"] = df["favorite_genre"].astype(str).str.upper().str.strip()

        fig4, ax4 = plt.subplots(figsize=(10,5))

        sns.countplot(
            data=df,
            x="favorite_genre",
            order=df["favorite_genre"].value_counts().index,
            ax=ax4
        )

        ax4.set_title("Géneros favoritos")
        ax4.set_xlabel("Género")
        ax4.set_ylabel("Usuarios")
        plt.xticks(rotation=90)

        st.pyplot(fig4)

    # =========================
    # TAB 3 - MULTIVARIADO
    # =========================
    with tab3:
        st.subheader("Relaciones múltiples")

        cols = [c for c in [
            "age",
            "monthly_watch_time_mins",
            "customer_support_tickets"
        ] if c in df.columns]

        if len(cols) > 1:

            fig5, ax5 = plt.subplots(figsize=(8,6))

            sns.heatmap(
                df[cols].corr(),
                annot=True,
                cmap="coolwarm",
                ax=ax5
            )

            ax5.set_title("Matriz de correlación")

            st.pyplot(fig5)

            st.write("""
            Se analiza la correlación entre variables numéricas del dataset.
            Los valores cercanos a 0 indican poca relación lineal.
            """)

        else:
            st.warning("No hay suficientes variables numéricas para el análisis.")

except Exception as e:
    st.error(f"Error al cargar el dataset: {e}")