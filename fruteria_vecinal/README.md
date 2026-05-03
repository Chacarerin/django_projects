# 🛒 Frutería Vecinal

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)

Evolución del sistema básico de control de inventario frutal, esta iteración incorpora capas adicionales de lógica de negocio orientadas a la autorización y validación asimétrica de usuarios.

## 📌 Contenidos Principales
- **Control de Acceso Basado en Roles (RBAC):** Restricción de interfaces y operaciones CRUD dependiendo de si el usuario es un cliente final (solo lectura del catálogo) o un administrador (lectura y escritura de inventario).
- **Formularios Dinámicos Avanzados:** Procesamiento de actualizaciones simultáneas en lotes de productos.
- **Consultas Filtradas:** Explotación del ORM para recuperar subconjuntos específicos de datos utilizando filtros lógicos (ej. productos agotados, productos en oferta).

## ⚙️ Tecnologías y Frameworks Aplicados
- **Django Auth & Permissions:** El sistema nativo de permisos es la pieza clave para habilitar la lógica de roles sin recurrir a validaciones manuales inseguras a nivel de vista.

---
*Desarrollado por Rubén Schnettler.*
