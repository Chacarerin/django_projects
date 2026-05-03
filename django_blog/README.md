# 📝 Django Blog

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)

Este proyecto materializa el desarrollo de un gestor de contenido (CMS ligero) estructurado como un blog. Constituye un excelente caso de estudio para asimilar la gestión avanzada de sesiones y la autorización dentro de la arquitectura de Django.

## 📌 Contenidos Principales
- **Sistema de Autenticación Integrado:** Integración profunda del módulo de autenticación nativo de Django, aislando lógicamente a los visitantes anónimos de los autores registrados.
- **Operaciones CRUD Orientadas a Objetos:** Mantenimiento transaccional de artículos (`Posts`).
- **Composición de Plantillas (Template Inheritance):** Estrategia de segmentación de código HTML (DRY - Don't Repeat Yourself) basada en la etiqueta `{% extends %}`, promoviendo una base estructural común (Header/Footer).
- **Abstracción de Formularios:** Uso del componente `ModelForms` para derivar automáticamente la validación del lado del servidor a partir de las restricciones impuestas por la base de datos (e.g. validación de formato de correos, longitud máxima).

## ⚙️ Tecnologías y Frameworks Aplicados
- **Django Middleware & Auth:** Se hace uso extensivo de la capa de Middleware de Django para gestionar sesiones web seguras y encriptadas de extremo a extremo, facilitando la protección CSRF y prevención de ataques estándar como SQL Injection.

---
*Desarrollado por Rubén Schnettler.*
