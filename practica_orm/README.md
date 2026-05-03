# 🛠️ Práctica Básica ORM

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)

Entorno controlado (*Sandbox*) diseñado con un propósito formativo inicial: experimentar atómicamente con las sentencias que el ORM de Django ofrece para interactuar con la persistencia de datos.

## 📌 Contenidos Principales
- **Ciclo de Migraciones:** Ejecución analítica de la traducción de clases Python (`models.py`) a instrucciones DDL de SQL mediante el ciclo `makemigrations` y `migrate`.
- **Entorno Interactivo (Django Shell):** Uso de la consola interactiva integrada para instanciar, consultar y manipular registros de prueba sin el peso computacional de arrancar el servidor web.
- **Filtros Sintácticos (Lookups):** Estudio exhaustivo de sufijos de búsqueda (`__exact`, `__icontains`, `__gt`) para condicionar resultados.

## ⚙️ Tecnologías y Frameworks Aplicados
- **Django Base Database API:** Se pone a prueba el motor genérico que asegura que el código escrito aquí funcionará invariablemente sin importar el motor relacional configurado por detrás (SQLite, Postgres, MySQL).

---
*Desarrollado por Rubén Schnettler.*
