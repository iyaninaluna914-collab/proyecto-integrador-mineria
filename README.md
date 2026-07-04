Proyecto Integrador – Minería de Datos 1
📌 Información general

Proyecto de análisis de datos aplicado a usuarios de una plataforma de streaming.
Se realizó un proceso completo de minería de datos que incluye limpieza, análisis exploratorio (EDA) y reducción de dimensionalidad mediante PCA.

🎯 Objetivo del proyecto

Aplicar técnicas de Minería de Datos para analizar el comportamiento de usuarios, identificar patrones relevantes y reducir la dimensionalidad del dataset utilizando PCA, con el fin de facilitar la interpretación de la información.

📁 Dataset

Se utilizó un dataset de usuarios que contiene variables como:

Edad
Plan de suscripción
Tiempo de visualización mensual
Género favorito
País

El dataset original presentaba inconsistencias como valores nulos, duplicados y categorías no estandarizadas.

Luego del proceso de limpieza, se generó un dataset procesado ubicado en data/processed/.

🗂️ Estructura del repositorio
data/ → datasets original y procesado
notebooks/ → análisis paso a paso
app/ → aplicación Streamlit
reports/ → informe final en PDF
logs/ → registros del proceso ETL
README.md → documentación del proyecto
🧹 Preparación y calidad de datos

Se realizó un proceso de limpieza que incluyó:

Eliminación de duplicados
Tratamiento de valores nulos
Estandarización de variables categóricas (países, planes, géneros)
Corrección de valores atípicos en variables numéricas
Normalización de formatos de texto

Esto permitió mejorar la calidad del dataset y asegurar la consistencia de los datos para el análisis.

📊 Análisis exploratorio de datos (EDA)

Se realizaron análisis univariados, bivariados y multivariados.

Se identificaron patrones en:

Distribución de edades
Tiempo de uso de la plataforma
Preferencias de contenido según género
Diferencias entre planes de suscripción
Relación entre variables numéricas
📉 Reducción de dimensionalidad (PCA)

Se aplicó PCA sobre variables numéricas previamente escaladas.

El análisis permitió reducir el dataset a dos componentes principales, facilitando la visualización de patrones generales sin pérdida significativa de información.

🌐 Visualización interactiva

La aplicación Streamlit permite explorar:

Dataset completo
Análisis exploratorio (EDA)
Resultados de PCA
Conclusiones del proyecto

🔗 Deploy: 
streamlit run app/Home.py