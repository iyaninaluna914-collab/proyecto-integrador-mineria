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

        with col1:

            st.markdown("### 📌 Distribución de Edad")

            fig1, ax1 = plt.subplots(figsize=(6,4))

            sns.histplot(
                data=df,
                x="age",
                bins=20,
                kde=True,
                ax=ax1
            )

            ax1.set_title("Distribución de Edad")
            ax1.set_xlabel("Edad")
            ax1.set_ylabel("Frecuencia")

            st.pyplot(fig1)

            st.write("""
            La mayor concentración de usuarios se encuentra en edades intermedias,
            mostrando el perfil demográfico predominante de la plataforma.
            """)

        with col2:

            st.markdown("### 📌 Plan de Suscripción")

            df_plan = df.copy()

            df_plan["subscription_plan"] = (
                df_plan["subscription_plan"]
                .astype(str)
                .str.title()
                .str.strip()
            )

            fig2, ax2 = plt.subplots(figsize=(6,4))

            sns.countplot(
                data=df_plan,
                x="subscription_plan",
                order=df_plan["subscription_plan"].value_counts().index,
                ax=ax2
            )

            ax2.set_title("Distribución de Planes")
            ax2.set_xlabel("Plan")
            ax2.set_ylabel("Usuarios")

            st.pyplot(fig2)

            st.write("""
            Permite observar la distribución de usuarios según el plan contratado.
            """)

    # =====================================================
    # TAB 2 - BIVARIADO
    # =====================================================
    with tab2:

        st.subheader("Relación entre dos variables")

        st.markdown("### 📌 Edad vs Tiempo de Visualización")

        fig3, ax3 = plt.subplots(figsize=(10,5))

        sns.scatterplot(
            data=df,
            x="age",
            y="monthly_watch_time_mins",
            alpha=0.5,
            ax=ax3
        )

        ax3.set_title("Edad vs Tiempo de Uso")
        ax3.set_xlabel("Edad")
        ax3.set_ylabel("Minutos de Visualización")

        st.pyplot(fig3)

        st.write("""
        Este gráfico permite observar si existe alguna relación entre la edad del usuario
        y el tiempo que consume contenido en la plataforma.
        """)

        st.markdown("---")

        st.markdown("### 📌 Género Favorito")

        df_genero = df.copy()

        df_genero["favorite_genre"] = (
            df_genero["favorite_genre"]
            .astype(str)
            .str.upper()
            .str.strip()
        )

        fig4, ax4 = plt.subplots(figsize=(10,5))

        sns.countplot(
            data=df_genero,
            x="favorite_genre",
            order=df_genero["favorite_genre"].value_counts().index,
            ax=ax4
        )

        ax4.set_title("Distribución de Géneros Favoritos")
        ax4.set_xlabel("Género")
        ax4.set_ylabel("Usuarios")

        plt.xticks(rotation=90)

        st.pyplot(fig4)

        st.write("""
        Permite identificar cuáles son los géneros más elegidos por los usuarios.
        """)

    # =====================================================
    # TAB 3 - MULTIVARIADO
    # =====================================================
    with tab3:

        st.subheader("Análisis Multivariado")

        df_multi = df.copy()

        df_multi["subscription_plan"] = (
            df_multi["subscription_plan"]
            .astype(str)
            .str.lower()
            .str.strip()
        )

        mapeo_planes = {
            "basic": "Basic",
            "premium": "Premium",
            "standard": "Standard"
        }

        df_multi["subscription_plan"] = (
            df_multi["subscription_plan"]
            .replace(mapeo_planes)
        )

        fig5, ax5 = plt.subplots(figsize=(10,6))

        sns.scatterplot(
            data=df_multi,
            x="age",
            y="monthly_watch_time_mins",
            hue="subscription_plan",
            palette="Set2",
            alpha=0.7,
            s=60,
            ax=ax5
        )

        ax5.set_title(
            "Consumo Mensual según Edad y Tipo de Plan"
        )

        ax5.set_xlabel("Edad")
        ax5.set_ylabel("Tiempo de Visualización (minutos)")

        st.pyplot(fig5)

        st.write("""
        Este análisis multivariado combina tres variables:
        edad, tiempo de visualización mensual y plan de suscripción.
        Los colores permiten identificar posibles diferencias de comportamiento
        entre usuarios de distintos planes.
        """)

except Exception as e:
    st.error(f"Error al cargar el dataset: {e}")
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
