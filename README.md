# 🚀 Portafolio de Proyectos en Django

![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%238511FA.svg?style=for-the-badge&logo=bootstrap&logoColor=white)

¡Bienvenido! Este repositorio agrupa varios proyectos web desarrollados con **Django**, diseñados para resolver distintos casos de uso utilizando las capacidades Full Stack del framework (ORM, sistema de plantillas, autenticación y más).

## 🏆 Proyectos Destacados

### 1. 📚 Biblioteca Vecinal (`biblioteca_vecinal`)
Una aplicación para la gestión comunitaria de libros.
- Sistema de catálogo de libros.
- Registro de préstamos y devoluciones.
- Interfaz amigable para los vecinos y administradores.

### 2. 📝 Django Blog (`django_blog`)
Un sistema de blog completo y funcional.
- Creación, edición y eliminación de artículos (CRUD completo).
- Sistema de categorías y etiquetas.
- Comentarios y autenticación de autores.

### 3. ⚙️ Django CRUD Básicos (`django_crud`)
Proyecto enfocado en dominar las operaciones CRUD de forma limpia y segura.
- Formularios interactivos (ModelForms).
- Validaciones personalizadas en el backend.

### 4. 💼 Django Portfolio (`django_portfolio`)
Una aplicación diseñada para mostrar proyectos profesionales (como este mismo repositorio pero en formato web).
- Panel de administración para cargar nuevos trabajos.
- Frontend estilizado para una presentación atractiva.

---

## 🛠️ Instalación y Uso

Para probar cualquiera de estos proyectos en tu máquina local:

1. Clona este repositorio:
   ```bash
   git clone https://github.com/Chacarerin/django_projects.git
   ```
2. Entra en la carpeta del proyecto que te interese (ej. `cd biblioteca_vecinal`).
3. Crea y activa tu entorno virtual (`python -m venv venv`).
4. Instala Django y las dependencias (si existe un `requirements.txt`).
5. Corre las migraciones para inicializar la base de datos:
   ```bash
   python manage.py migrate
   ```
6. (Opcional) Crea un superusuario para acceder al panel de administración:
   ```bash
   python manage.py createsuperuser
   ```
7. Inicia el servidor local:
   ```bash
   python manage.py runserver
   ```
---
*Desarrollado por Rubén Schnettler.*
