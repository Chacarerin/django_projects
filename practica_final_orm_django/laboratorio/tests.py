from django.test import TestCase
from django.urls import reverse
from .models import Laboratorio

class LaboratorioModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Creamos un laboratorio de prueba para usar en todas las pruebas
        cls.laboratorio = Laboratorio.objects.create(
            nombre="Laboratorio Prueba",
            ciudad="Ciudad Prueba",
            pais="País Prueba"
        )

    # 1. Verificar que los datos del laboratorio creado coinciden con lo que se espera
    def test_laboratorio_data(self):
        laboratorio = Laboratorio.objects.get(id=self.laboratorio.id)
        self.assertEqual(laboratorio.nombre, "Laboratorio Prueba")
        self.assertEqual(laboratorio.ciudad, "Ciudad Prueba")
        self.assertEqual(laboratorio.pais, "País Prueba")

    # 2. Verificar que la URL para la lista de laboratorios devuelve una respuesta HTTP 200
    def test_lista_laboratorios_url(self):
        response = self.client.get(reverse('lista_laboratorios'))
        self.assertEqual(response.status_code, 200)

    # 3. Verificar que se usa la plantilla correcta y que el contenido HTML es el esperado
    def test_lista_laboratorios_template(self):
        response = self.client.get(reverse('lista_laboratorios'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lista_laboratorios.html')
        self.assertContains(response, 'Información de Laboratorios')
        self.assertContains(response, 'Laboratorio Prueba')
        self.assertContains(response, 'Ciudad Prueba')
        self.assertContains(response, 'País Prueba')