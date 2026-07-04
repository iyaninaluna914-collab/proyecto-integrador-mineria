import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="EDA - Análisis Exploratorio",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Análisis Exploratorio de Datos (EDA)")

# =========================
# CARGA DE DATOS
# =========================
df = pd.read_csv("../data/processed/dataset_limpio.csv")

st.write("Vista general del dataset:")
st.dataframe(df.head())

st.divider()

# =========================
# 1. UNIVARIADO - EDAD
# =========================
st.subheader("📌 1. Distribución de Edad")

fig1, ax1 = plt.subplots()

df["age"].hist(bins=20, ax=ax1)

ax1.set_title("Distribución de edad")
ax1.set_xlabel("Edad")
ax1.set_ylabel("Frecuencia")

st.pyplot(fig1)

st.divider()

# =========================
# 2. UNIVARIADO - PLAN
# =========================
st.subheader("📌 2. Distribución de Planes de Suscripción")

fig2, ax2 = plt.subplots()

df["subscription_plan"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90,
    colormap="Set3",
    ax=ax2
)

ax2.set_ylabel("")
ax2.set_title("Planes de suscripción")

st.pyplot(fig2)

st.divider()

# =========================
# 3. BIVARIADO - EDAD vs USO
# =========================
st.subheader("📌 3. Edad vs Tiempo de Uso")

fig3, ax3 = plt.subplots(figsize=(8,5))

sns.regplot(
    data=df,
    x="age",
    y="monthly_watch_time_mins",
    scatter_kws={"alpha": 0.5},
    ax=ax3
)

ax3.set_title("Relación entre Edad y Uso")
ax3.set_xlabel("Edad")
ax3.set_ylabel("Minutos de uso")

st.pyplot(fig3)

st.divider()

# =========================
# 4. BIVARIADO - EDAD PROMEDIO POR GÉNERO
# =========================
st.subheader("📌 4. Edad promedio por género favorito")

edad_genero = df.groupby("favorite_genre")["age"].mean().sort_values()

fig4, ax4 = plt.subplots(figsize=(10,5))

sns.barplot(
    x=edad_genero.index,
    y=edad_genero.values,
    palette="viridis",
    ax=ax4
)

ax4.set_title("Edad promedio según género favorito")
ax4.set_xlabel("Género")
ax4.set_ylabel("Edad promedio")

plt.xticks(rotation=45)

st.pyplot(fig4)

st.divider()

# =========================
# 5. MULTIVARIADO
# =========================
st.subheader("📌 5. Análisis Multivariado")

df_clean = df.copy()

# limpieza planes
df_clean["subscription_plan"] = (
    df_clean["subscription_plan"]
    .astype(str)
    .str.lower()
    .str.strip()
)

mapeo = {
    "standard": "Standard",
    "std": "Standard",
    "basic": "Basic",
    "basico": "Basic",
    "premium": "Premium",
    "premiun": "Premium",
}

df_clean["subscription_plan"] = df_clean["subscription_plan"].map(mapeo).fillna(df_clean["subscription_plan"])

df_clean = df_clean[
    (df_clean["age"] > 0) &
    (df_clean["age"] <= 90) &
    (df_clean["monthly_watch_time_mins"] < 10000)
]

fig5, ax5 = plt.subplots(figsize=(10,6))

sns.scatterplot(
    data=df_clean,
    x="age",
    y="monthly_watch_time_mins",
    hue="subscription_plan",
    palette="Set2",
    alpha=0.7,
    ax=ax5
)

sns.regplot(
    data=df_clean,
    x="age",
    y="monthly_watch_time_mins",
    scatter=False,
    color="black",
 ax=ax5
)

ax5.set_title("Edad vs Uso por Plan")
ax5.set_xlabel("Edad")
ax5.set_ylabel("Minutos de uso")

st.pyplot(fig5)

st.success("✅ EDA completado correctamente")