import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# =========================
# CONFIGURACIÓN DE LA PÁGINA
# =========================
st.set_page_config(
    page_title="EDA - Análisis Exploratorio",
    page_icon="📊",
    layout="wide"
)

# Estilo global limpio para los gráficos
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams.update({'figure.facecolor': '#ffffff', 'axes.facecolor': '#ffffff'})

st.title("📊 Análisis Exploratorio de Datos (EDA)")
st.markdown("Bienvenido al módulo de análisis exploratorio. Aquí podrás comprender la estructura, distribuciones y relaciones de las variables clave del negocio.")

# =========================
# CARGA Y LIMPIEZA DE DATOS
# =========================
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.normpath(os.path.join(CURRENT_DIR, "..", "data", "processed", "dataset_limpio.csv"))

try:
    df = pd.read_csv(DATA_PATH)
except FileNotFoundError:
    df = pd.read_csv("data/processed/dataset_limpio.csv")

# Filtros globales críticos para asegurar que las edades y minutos estén perfectos en todos los gráficos
df = df[
    (df["age"] > 0) & 
    (df["age"] <= 90) & 
    (df["monthly_watch_time_mins"] < 10000)
]

# =========================
# METRICAS DEL PROCESO DE DATOS
# =========================
st.markdown("### 📈 Control de Calidad del Dataset")
kpi1, kpi2, kpi3 = st.columns(3)
with kpi1:
    st.metric(label="Registros Iniciales", value="8,160")
with kpi2:
    st.metric(label="Registros Duplicados Eliminados", value="126", delta="-126", delta_color="inverse")
with kpi3:
    # Muestra el total neto exacto de tu limpieza de duplicados
    st.metric(label="Total Registros Analizados", value="8,034")

st.markdown("#### 🔍 Vista previa de los datos finalizados")
st.dataframe(df.head(5), use_container_width=True)

st.write("---")

# =========================
# SECCIÓN 1: UNIVARIADO
# =========================
st.markdown("## 🎯 Análisis Univariado")
st.caption("Inspección individual de las variables más importantes.")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📌 1. UNIVARIADO - EDAD")
    fig1, ax1 = plt.subplots(figsize=(6, 4))
    df["age"].hist(bins=20, ax=ax1, color="#4A90E2", edgecolor="white")
    ax1.set_title("Distribución de Edad", fontsize=12, fontweight='bold')
    ax1.set_xlabel("Edad")
    ax1.set_ylabel("Frecuencia")
    st.pyplot(fig1)

with col2:
    st.subheader("📌 2. UNIVARIADO - PLAN")
    fig2, ax2 = plt.subplots(figsize=(6, 4))
    df["subscription_plan"].value_counts().plot(
        kind="pie",
        autopct="%1.1f%%",
        startangle=90,
        colormap="Pastel1",
        ax=ax2
    )
    ax2.set_ylabel("")
    ax2.set_title("Proporción de Planes de Suscripción", fontsize=12, fontweight='bold')
    st.pyplot(fig2)

st.write("---")

# =========================
# SECCIÓN 2: BIVARIADO
# =========================
st.markdown("## 🔄 Análisis Bivariado")
st.caption("Evaluación de la interacción entre dos variables simultáneamente.")

col3, col4 = st.columns(2)

with col3:
    st.subheader("📌 3. BIVARIADO - EDAD vs USO")
    fig3, ax3 = plt.subplots(figsize=(6, 4))
    sns.regplot(
        data=df,
        x="age",
        y="monthly_watch_time_mins",
        scatter_kws={"alpha": 0.4, "color": "#2ECC71"},
        line_kws={"color": "#E74C3C", "linewidth": 2},
        ax=ax3
    )
    ax3.set_title("Relación entre Edad y Uso Mensual", fontsize=12, fontweight='bold')
    ax3.set_xlabel("Edad")
    ax3.set_ylabel("Minutos de uso")
    st.pyplot(fig3)

with col4:
    st.subheader("📌 4. BIVARIADO - EDAD PROMEDIO POR GÉNERO")
    fig4, ax4 = plt.subplots(figsize=(6, 4))
    edad_genero = df.groupby("favorite_genre")["age"].mean().sort_values()
    
    sns.barplot(
        x=edad_genero.index,
        y=edad_genero.values,
        palette="Blues_r",
        ax=ax4
    )
    ax4.set_title("Edad Promedio según Género Favorito", fontsize=12, fontweight='bold')
    ax4.set_xlabel("Género Favorito")
    ax4.set_ylabel("Edad Promedio")
    ax4.tick_params(axis='x', rotation=45)
    st.pyplot(fig4)

st.write("---")

# =========================
# SECCIÓN 3: MULTIVARIADO
# =========================
st.markdown("## 🔮 Análisis Multivariado")
st.caption("Visualización de múltiples dimensiones para encontrar patrones complejos.")

st.subheader("📌 5. MULTIVARIADO")

df_clean = df.copy()
df_clean["subscription_plan"] = (
    df_clean["subscription_plan"]
    .astype(str)
    .str.lower()
    .str.strip()
)

mapeo = {
    "standard": "Standard", "std": "Standard",
    "basic": "Basic", "basico": "Basic",
    "premium": "Premium", "premiun": "Premium",
}
df_clean["subscription_plan"] = df_clean["subscription_plan"].map(mapeo).fillna(df_clean["subscription_plan"])

# Gráfico Multivariado a ancho completo
fig5, ax5 = plt.subplots(figsize=(12, 5))
sns.scatterplot(
    data=df_clean,
    x="age",
    y="monthly_watch_time_mins",
    hue="subscription_plan",
    palette="Set2",
    alpha=0.6,
    ax=ax5
)
sns.regplot(
    data=df_clean,
    x="age",
    y="monthly_watch_time_mins",
    scatter=False,
    color="#333333",
    line_kws={"linestyle": "--", "linewidth": 2},
    ax=ax5
)

ax5.set_title("Edad vs Uso Mensual segmentado por Plan de Suscripción", fontsize=14, fontweight='bold')
ax5.set_xlabel("Edad")
ax5.set_ylabel("Minutos de uso")
st.pyplot(fig5)

st.success("✅ EDA completado correctamente")