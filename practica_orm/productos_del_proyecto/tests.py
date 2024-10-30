from django.test import TestCase
from django.urls import reverse
from productos_del_proyecto.models import Fabricante, Producto

class ProductoTests(TestCase):

    def test_url_producto_agregar_status(self):
        """
        1. Verificación del funcionamiento de la URL /productos/agregar/, que devuelva un código de estatus 200.
        """
        response = self.client.get('/productos/agregar/')
        self.assertEqual(response.status_code, 200)

    def test_url_producto_agregar_reverse(self):
        """
        2. Prueba de validación de URL disponible por nombre del enlace reverso de: agregar_producto.
        """
        url = reverse('agregar_producto')  # Nombre que tienes en urls.py
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_nombre_plantilla_producto(self):
        """
        3. Verificar si el nombre es correcto con relación a la plantilla de agregar y su nombre reverso.
        """
        response = self.client.get(reverse('agregar_producto'))
        self.assertTemplateUsed(response, 'agregar_producto.html')

    def test_contenido_plantilla_producto(self):
        """
        4. Verificar si un contenido corresponde a la plantilla, por ejemplo: el botón "Guardar Producto"
        """
        response = self.client.get(reverse('agregar_producto'))
        self.assertContains(response, 'Guardar Producto')

    @classmethod
    def setUpTestData(cls):
        """
        Crear datos iniciales de prueba para todas las pruebas.
        """
        # Crear un fabricante
        cls.fabricante = Fabricante.objects.create(nombre='P&G', pais='USA')

        # Crear un producto asociado al fabricante
        cls.producto = Producto.objects.create(
            nombre='Crest Premium',
            descripcion='Crema dental premium',
            precio=2500.00,
            fabricante=cls.fabricante,
            f_vencimiento='2024-11-01'
        )

    def test_model_content_fabrica(self):
        """
        1. Verificación de datos para el modelo de Fábrica.
        """
        self.assertEqual(self.fabricante.nombre, 'P&G')
        self.assertEqual(self.fabricante.pais, 'USA')

    def test_model_content_producto(self):
        """
        2. Verificación de datos para el modelo de Producto.
        """
        self.assertEqual(self.producto.nombre, 'Crest Premium')
        self.assertEqual(self.producto.descripcion, 'Crema dental premium')
        self.assertEqual(self.producto.precio, 2500.00)
        self.assertEqual(self.producto.fabricante, self.fabricante)
        self.assertEqual(self.producto.f_vencimiento, '2024-11-01')

    def test_producto_url_status_code(self):
        """
        3. Verificar el código de respuesta HTTP 200 de la URL /producto/.
        """
        response = self.client.get('/productos/')
        self.assertEqual(response.status_code, 200)

    def test_lista_productos_view(self):
        """
        4. Verificar la vista lista_productos:
            - Verificación del código de respuesta 200
            - Verificación de la plantilla correcta (productos.html)
            - Verificación del contenido esperado: "Información de Productos"
        """
        response = self.client.get(reverse('lista_productos'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'productos.html')
        self.assertContains(response, 'Productos')