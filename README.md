# 📊 Proyecto Integrador - Minería de Datos 1

---

## 📌 Información general
Proyecto de análisis de datos aplicado a usuarios de una plataforma de streaming.  
Se realizó un proceso completo de minería de datos que incluye limpieza, análisis exploratorio y reducción de dimensionalidad.

---

## 🎯 Objetivo del proyecto
Aplicar técnicas de Minería de Datos 1 para analizar el comportamiento de usuarios, identificar patrones relevantes y reducir la dimensionalidad del dataset utilizando PCA.

---

## 📁 Dataset
Se utilizó un dataset de usuarios con variables como edad, plan de suscripción, tiempo de visualización, género favorito y tickets de soporte.

El dataset original fue limpiado mediante:
- Eliminación de duplicados
- Tratamiento de valores nulos
- Normalización de variables categóricas

El dataset final se encuentra en `data/processed/`.

---

## 🗂️ Estructura del repositorio
- data/ → datasets original y procesado  
- notebooks/ → análisis paso a paso  
- app/ → aplicación Streamlit  
- reports/ → informe final  
- logs/ → registro ETL  
- README.md → documentación del proyecto  

---

## 🧹 Preparación y calidad de datos
Se realizó un proceso de limpieza que incluyó:
- Identificación y eliminación de duplicados
- Imputación de valores nulos con media o moda según variable
- Normalización de categorías con diferentes formatos o idiomas
- Generación del dataset final procesado

---

## 📊 Resumen del análisis exploratorio (EDA)
Se realizaron análisis univariados, bivariados y multivariados.

Se observaron patrones en:
- Distribución de edad
- Uso de la plataforma según tiempo de visualización
- Diferencias entre planes de suscripción
- Relaciones entre variables numéricas

---

## 📉 Reducción de dimensionalidad (PCA)
Se aplicó PCA sobre variables numéricas escaladas.

El análisis permitió reducir la dimensión del dataset a 2 componentes principales, facilitando la visualización de patrones generales sin pérdida significativa de información.

---

## 🌐 Visualización interactiva
La aplicación Streamlit permite explorar:
- Dataset
- Análisis exploratorio (EDA)
- PCA
- Conclusiones del proyecto

Deploy: (agregar link de Streamlit cuando lo subas)

---

## ▶️ Cómo ejecutar localmente
```bash
streamlit run app/Home.py