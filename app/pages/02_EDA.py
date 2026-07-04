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
univariadas, bivariadas y multivariadas.
""")

st.markdown("---")

# =========================
# CARGA DE DATOS
# =========================
df = pd.read_csv("data/processed/dataset_limpio.csv")

sns.set_theme(style="whitegrid")

# =========================
# TABS
# =========================
tab1, tab2, tab3 = st.tabs([
    "📊 Univariado",
    "📉 Bivariado",
    "🧮 Multivariado"
])

# =====================================================
# TAB 1 - UNIVARIADO
# =====================================================
with tab1:

    st.subheader("Distribución de variables individuales")

    col1, col2 = st.columns(2)

    # 📊 Edad (HISTOGRAMA)
    with col1:

        st.markdown("### 📌 Distribución de Edad")

        fig1, ax1 = plt.subplots(figsize=(6,4))

        ax1.hist(df["age"], bins=20, color="skyblue", edgecolor="black")

        ax1.set_title("Distribución de edad")
        ax1.set_xlabel("Edad")
        ax1.set_ylabel("Frecuencia")

        st.pyplot(fig1)

    # 📊 Plan de suscripción (PIE)
    with col2:

        st.markdown("### 📌 Plan de Suscripción")

        fig2, ax2 = plt.subplots(figsize=(6,4))

        df["subscription_plan"].value_counts().plot(
            kind="pie",
            autopct="%1.1f%%",
            startangle=90,
            cmap="Set3",
            ax=ax2
        )

        ax2.set_title("Distribución de planes")
        ax2.set_ylabel("")

        st.pyplot(fig2)

# =====================================================
# TAB 2 - BIVARIADO
# =====================================================
with tab2:

    st.subheader("Relación entre dos variables")

    # 📊 Edad vs Tiempo de uso (REGRESSION PLOT)
    st.markdown("### 📌 Edad vs Tiempo de Uso")

    fig3, ax3 = plt.subplots(figsize=(8,5))

    sns.regplot(
        data=df,
        x="age",
        y="monthly_watch_time_mins",
        scatter_kws={"alpha": 0.5},
        ax=ax3
    )

    ax3.set_title("Relación entre Edad y Tiempo de Uso")
    ax3.set_xlabel("Edad")
    ax3.set_ylabel("Minutos de uso mensual")

    st.pyplot(fig3)

# =====================================================
# TAB 3 - MULTIVARIADO
# =====================================================
with tab3:

    st.subheader("Análisis Multivariado")

    # 📊 Edad promedio por género favorito
    edad_genero = df.groupby("favorite_genre")["age"].mean().sort_values()

    fig4, ax4 = plt.subplots(figsize=(10,5))

    sns.barplot(
        x=edad_genero.index,
        y=edad_genero.values,
        palette="viridis",
        ax=ax4
    )

    ax4.set_title("Edad promedio según género favorito")
    ax4.set_xlabel("Género favorito")
    ax4.set_ylabel("Edad promedio")

    plt.xticks(rotation=45)

    st.pyplot(fig4)