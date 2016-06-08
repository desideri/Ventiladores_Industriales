from django.test import TestCase
from web.models import *
from datetime import datetime
import unittest
from selenium import webdriver
'''
@Autores: Wilenco team
@Ultima modificacion: junio07/2016
@Ultimo modificador: Israel Fernandez
Pruebas de caja negra y blanca para proyecto
Fuente de referencia: https://realpython.com/blog/python/headless-selenium-testing-with-python-and-phantomjs/

'''

class TestCajaNegraContacto(TestCase):
    """
       @Autor: Jorge Ayala
       Como su nombre lo indica, es una clase usada para realizar unit test.
       En este caso se lo usa para realizar pruebas de Caja negra a la Pagina Contacto de nuestro sitio web.
       Las input que se deben probar son:
       - Email
       Para las cuales se han identificado las siguientes clases de equivalencia:
       -Email:
            Clases de equivalencia:
               CE1: las cadenas de caracteres aceptados por el regex: /^([a-z\d!#$%&'*+\-\/=?^_`{|}~\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]+(\.[a-z\d!#$%&'*+\-\/=?^_`{|}~\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]+)*|"((([ \t]*\r\n)?[ \t]+)?([\x01-\x08\x0b\x0c\x0e-\x1f\x7f\x21\x23-\x5b\x5d-\x7e\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]|\\[\x01-\x09\x0b\x0c\x0d-\x7f\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]))*(([ \t]*\r\n)?[ \t]+)?")@(([a-z\d\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]|[a-z\d\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF][a-z\d\-._~\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]*[a-z\d\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])\.)+([a-z\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]|[a-z\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF][a-z\d\-._~\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]*[a-z\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])\.?$/i
               CE2: las cadenas de caracteres no aceptados por el regex: /^([a-z\d!#$%&'*+\-\/=?^_`{|}~\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]+(\.[a-z\d!#$%&'*+\-\/=?^_`{|}~\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]+)*|"((([ \t]*\r\n)?[ \t]+)?([\x01-\x08\x0b\x0c\x0e-\x1f\x7f\x21\x23-\x5b\x5d-\x7e\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]|\\[\x01-\x09\x0b\x0c\x0d-\x7f\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]))*(([ \t]*\r\n)?[ \t]+)?")@(([a-z\d\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]|[a-z\d\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF][a-z\d\-._~\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]*[a-z\d\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])\.)+([a-z\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]|[a-z\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF][a-z\d\-._~\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]*[a-z\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])\.?$/i
            Validez:
                CE1: valido
                CE2: invalido
    """

    def setUp(self):
        self.driver = webdriver.PhantomJS()
        # self.driver = webdriver.Firefox()
        self.driver.set_window_size(1120,550)

    def test_emailCorrecto(self):
        """
        En esta prueba se utiliza la clase de equivalencia CE1.
        Como resultado, el usuario no debe ver ningun mensaje y los campos del formulario se limpian.
        """
        self.driver.get("http://localhost:8000/contacto/")
        self.driver.find_element_by_id('nombreUsuario').send_keys("Jorge Ayala")
        self.driver.find_element_by_id('emailUsuario').send_keys("test@iana.org.")
        self.driver.find_element_by_id('telUsuario').send_keys("22323")
        self.driver.find_element_by_id('asuntoUsuario').send_keys("Nada improtante")
        self.driver.find_element_by_class_name("mybutton").click()

        msgEmailInvalido = self.driver.find_element_by_id("msgEmailInvalido")

        self.assertFalse(msgEmailInvalido.is_displayed())

    def test_emailIncorrecto(self):
        '''
        En esta prueba se utiliza la clase de equivalencia CE2.
        Como resultado, el usuario debe ver un mensaje de email incorrecto en rojo.
        '''
        self.driver.get("http://localhost:8000/contacto/")
        self.driver.find_element_by_id('nombreUsuario').send_keys("Jorge Ayala")
        self.driver.find_element_by_id('emailUsuario').send_keys("testiana.org.")
        self.driver.find_element_by_id('telUsuario').send_keys("22323")
        self.driver.find_element_by_id('asuntoUsuario').send_keys("Nada improtante")
        self.driver.find_element_by_class_name("mybutton").click()

        msgEmailInvalido = self.driver.find_element_by_id("msgEmailInvalido")

        self.assertTrue(msgEmailInvalido.is_displayed())

    def tearDown(self):
        self.driver.quit()

class TestCajaNegraModeloSolicitud(TestCase):
    """
        @Autor: Israel Fernandez
        Clase para realizar un unit test del modelo Solicitud
        Ingresando entradas validas y no validas
    """
    def crear_solicitud_valida(self):
        self.solicitud = Solicitud.objects.create(tipo = False, descripcion = "test",
                                                  fechaEscojida = datetime.now(), nombre="test",
                                                  apellido ="test", cedulaCliente = "0912345678")

        self.assertIsInstance(self.solicitud, Solicitud, 'Solicitud exitosa')

    def crear_solicitud_invalida(self):
        self.solicitud = Solicitud.objects.create(tipo = False, descripcion = "test",
                                                  fechaEscojida = datetime.now(), nombre="test",
                                                  apellido ="test", cedulaCliente = "09123456780")

        self.assertNotIsInstance(self.solicitud, Solicitud, 'Solicitud invalida :(')
