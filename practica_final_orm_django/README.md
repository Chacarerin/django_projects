# 🗄️ Práctica Final ORM

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![PostgreSQL](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)

Este subproyecto funciona como una prueba de fuego de las capacidades de abstracción de datos. Aísla completamente la lógica de base de datos de la capa visual para enfocarse empíricamente en consultas relacionales complejas y agregaciones.

## 📌 Contenidos Principales
- **Arquitectura Relacional Avanzada:** Demostración técnica de esquemas que integran relaciones uno-a-uno (`OneToOneField`), uno-a-muchos (`ForeignKey`) y muchos-a-muchos (`ManyToManyField`).
- **Análisis Aritmético (Aggregations/Annotations):** Cálculos agrupados y derivación de campos al vuelo (sumatorias, promedios, conteos) delegados directamente al motor de la base de datos para máxima eficiencia.
- **Consultas Lógicas Computacionales (Q Objects):** Construcción programática de predicados condicionales (AND, OR, NOT) que superan las limitaciones de los filtros tradicionales de diccionarios.

## ⚙️ Tecnologías y Frameworks Aplicados
- **Django ORM (Avanzado):** Utilizado para demostrar que operaciones equivalentes a *INNER JOIN*, *GROUP BY* y *HAVING* en SQL puro pueden ser resueltas mediante una sintaxis Pythonica legible y tipada.

---
*Desarrollado por Rubén Schnettler.*
