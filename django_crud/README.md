# ⚙️ Django CRUD Básico

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)

Proyecto puramente formativo cuyo alcance es diseccionar y automatizar las cuatro operaciones atómicas fundamentales requeridas en cualquier base de datos persistente: Creación, Lectura, Actualización y Eliminación (CRUD).

## 📌 Contenidos Principales
- **Aislamiento del Modelo de Datos:** Se estudia cómo la capa ORM abstrae por completo al desarrollador del dialecto SQL subyacente.
- **Parametrización de Enrutamiento:** Ingeniería de URLs limpias y dinámicas que capturan identificadores únicos (ej. `/<id>/update`) para direccionar la petición hacia el registro exacto a modificar en memoria.
- **Protección de Vectores de Ataque:** Implementación rigurosa de protección CSRF (Cross-Site Request Forgery) en cada transmisión de carga útil mediante métodos POST.
- **Ciclo de Vida de la Petición:** Gestión del redireccionamiento HTTP tras ejecuciones transaccionales exitosas en la base de datos.

## ⚙️ Tecnologías y Frameworks Aplicados
- **Django ORM (Object-Relational Mapping):** Un puente tecnológico sofisticado que traslada la lógica de conjuntos (álgebra relacional) a simples llamadas de métodos sobre objetos Python. Esto agiliza la refactorización de esquemas sin refactorizar el código de la vista.

---
*Desarrollado por Rubén Schnettler.*
