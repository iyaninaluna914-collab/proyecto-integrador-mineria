import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/processed/dataset_limpio.csv")

st.title("📊 EDA")

# UNIVARIADO
st.subheader("Edad")
fig, ax = plt.subplots()
df["age"].hist(bins=20, ax=ax)
st.pyplot(fig)

st.subheader("Plan de suscripción")
st.bar_chart(df["subscription_plan"].value_counts())

# BIVARIADO
st.subheader("Edad vs tiempo de uso")
fig, ax = plt.subplots()
sns.scatterplot(data=df, x="age", y="monthly_watch_time_mins", ax=ax)
st.pyplot(fig)

st.subheader("Género favorito vs tiempo de uso")
fig, ax = plt.subplots()
df.groupby("favorite_genre")["monthly_watch_time_mins"].mean().plot(kind="bar", ax=ax)
st.pyplot(fig)

# MULTIVARIADO
st.subheader("Correlación")
fig, ax = plt.subplots()
sns.heatmap(df.corr(numeric_only=True), annot=True, ax=ax)
st.pyplot(fig)
