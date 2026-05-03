# 📚 Biblioteca Vecinal

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)

El presente repositorio expone el desarrollo de un sistema de información web para la administración de un acervo bibliográfico comunitario. El objetivo fundamental es la digitalización y trazabilidad estricta del inventario de libros y del control de préstamos a socios vecinales.

## 📌 Contenidos Principales
- **Arquitectura de Dominio (Modelos):** Diseño lógico de entidades fundamentales tales como `Libro`, `Autor`, `Socio` y `Prestamo`. 
- **Integridad Referencial:** Implementación de claves foráneas (`ForeignKey`) para mapear relaciones de uno-a-muchos (ej. un autor puede tener múltiples libros, un socio múltiples préstamos).
- **Flujo de Vistas Estándar (FBV):** Enrutamiento de peticiones HTTP hacia funciones procesadoras (Views) encargadas de invocar al ORM y devolver respuestas renderizadas a través del motor de plantillas.
- **Panel Administrativo:** Configuración nativa para habilitar a los administradores del recinto la carga masiva y depuración de registros sin requerir una interfaz frontend especializada.

## ⚙️ Tecnologías y Frameworks Aplicados
- **Django Framework:** Elegido por su robusto paradigma MVT (Model-View-Template) y sus facilidades nativas ('batteries-included'). Destaca su panel de administración automático, crucial para el mantenimiento de los registros vecinales a bajo costo de desarrollo.

---
*Desarrollado por Rubén Schnettler.*
