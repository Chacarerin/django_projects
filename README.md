# Portafolio de Aplicaciones en Django

![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

Este repositorio contiene un compendio de proyectos web funcionales desarrollados íntegramente con el framework Django. La finalidad de estos proyectos es demostrar habilidades en la construcción de sistemas Full Stack, abarcando desde el modelado de la base de datos y validación de reglas de negocio, hasta el renderizado de la interfaz y construcción de APIs RESTful.

## Catálogo de Proyectos

Cada subcarpeta contiene una aplicación Django independiente. En el interior de cada una encontrarás documentación específica sobre su propósito y dependencias.

* **`biblioteca_vecinal`**: Sistema de gestión comunitaria para préstamos y catálogos de libros.
* **`django_blog`**: Plataforma de publicación de artículos con gestión de usuarios, categorías y comentarios.
* **`django_crud`**: Aplicación fundacional orientada a la dominación de operaciones Crear, Leer, Actualizar y Eliminar mediante ModelForms.
* **`django_portfolio`**: Sistema para la exhibición de portafolios profesionales, administrable mediante el backend de Django.
* **`fruteria` / `fruteria_vecinal`**: Aplicaciones para la gestión de inventario y ventas en locales comerciales de tamaño reducido.
* **`moviesapi`**: Servicio web que expone una API REST para consultar una base de datos de películas (utilizando Django REST Framework).
* **`ski_rental`**: Sistema de administración para el arriendo de equipos de esquí, con control de stock y disponibilidad.
* **`practica_orm` / `practica_final_orm_django`**: Ejercicios enfocados exclusivamente en la manipulación avanzada de bases de datos relacionales sin usar sentencias SQL crudas.

## Consideraciones Generales

Todos los proyectos están diseñados para ejecutarse en entornos virtuales de Python. Las configuraciones por defecto apuntan a bases de datos SQLite locales para facilitar su prueba, aunque la lógica del ORM permite la migración inmediata a motores como PostgreSQL.

---
*Desarrollado por Rubén Schnettler.*
