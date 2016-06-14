'''
@Autores: Wilenco team
@Ultima modificacion: junio 13/2016
@Ultimo modificador: Jorge Ayala
Pruebas de caja negra y blanca para proyecto
Fuente de referencia:
https://realpython.com/blog/python/headless-selenium-testing-with-python-and-phantomjs/
'''
from datetime import datetime
from django.test import TestCase
from django.test import Client
from django.test import LiveServerTestCase
from selenium import webdriver
from web.models import *


class TestCajaNegraContacto(LiveServerTestCase):
    """
       @Autor: Jorge Ayala
       Como su nombre lo indica, es una clase usada para realizar test.
       En este caso se lo usa para realizar pruebas de Caja negra a la
       Pagina Contacto de nuestro sitio web.
       Las input que se deben probar son:
       - Email
       Para las cuales se han identificado las siguientes clases
       de equivalencia:
       -Email:
            Clases de equivalencia:
               CE1: las cadenas de caracteres aceptados por el regex:
               encontrado en: http://so.devilmaycode.it/jquery-validate-e-mail-address-regex/
               CE2: las cadenas de caracteres no aceptados por el regex:
               encontrado en: http://so.devilmaycode.it/jquery-validate-e-mail-address-regex/
            Validez:
                CE1: valido
                CE2: invalido
    """
    def setUp(self):
        self.driver = webdriver.PhantomJS()
        # self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(6)
        self.driver.set_window_size(1120, 550)

    def tearDown(self):
        self.driver.quit()

    def test_email_correcto(self):
        """
        En esta prueba se utiliza la clase de equivalencia CE1.
        Como resultado, el usuario no debe ver ningun mensaje
        y los campos del formulario se limpian.
        """
        self.driver.get("http://localhost:8081/contacto/")
        self.driver.find_element_by_id('nombreUsuario').send_keys("Jorge Ayala")
        self.driver.find_element_by_id('emailUsuario').send_keys("test@iana.org.")
        self.driver.find_element_by_id('telUsuario').send_keys("22323")
        self.driver.find_element_by_id('asuntoUsuario').send_keys("Nada improtante")
        self.driver.find_element_by_class_name("mybutton").click()
        msg_email_invalido = self.driver.find_element_by_id("msgEmailInvalido")
        self.assertFalse(msg_email_invalido.is_displayed())
        email_incorrecto = msg_email_invalido.is_displayed()
        prueba_correcta = not email_incorrecto
        print "Prueba de mail correcto exitosa? " + str(prueba_correcta)
        
    def test_email_incorrecto(self):
        '''
        En esta prueba se utiliza la clase de equivalencia CE2.
        Como resultado, el usuario debe ver un mensaje de email
        incorrecto en rojo.
        '''
        self.driver.get("http://localhost:8081/contacto/")
        self.driver.find_element_by_id('nombreUsuario').send_keys("Jorge Ayala")
        self.driver.find_element_by_id('emailUsuario').send_keys("testiana.org.")
        self.driver.find_element_by_id('telUsuario').send_keys("22323")
        self.driver.find_element_by_id('asuntoUsuario').send_keys("Nada improtante")
        self.driver.find_element_by_class_name("mybutton").click()
        msg_email_invalido = self.driver.find_element_by_id("msgEmailInvalido")
        self.assertTrue(msg_email_invalido.is_displayed())
        print "Prueba de mail Incorrecto exitosa? " + str(msg_email_invalido.is_displayed())


class TestCajaNegraModeloSolicitud(TestCase):
    """
        @Autor: Israel Fernandez
        Clase para realizar un unit test del modelo Solicitud
        Ingresando entradas validas y no validas
    """
    def test_crear_solicitud_valida(self):
        self.solicitud = Solicitud.objects.create(tipo=False, descripcion="test",
                                                  fechaEscojida=datetime.now(),
                                                  nombre="test", apellido="test",
                                                  cedulaCliente="0912345678")

        self.assertIsInstance(self.solicitud, Solicitud, 'Solicitud exitosa')

    def test_crear_solicitud_invalida(self):
        self.solicitud = Solicitud.objects.create(tipo=False, descripcion="test",
                                                  fechaEscojida=datetime.now(),
                                                  nombre="test", apellido="test",
                                                  cedulaCliente="09asdasd123456780")

        try:
            self.solicitud.full_clean()
        except:
            print "Test Solicitud invalida: Solicitud Invalida"

        
class TestCajaNegraModeloCotizador(TestCase):
    """
        @Autor: Jorge Ayala
        Clase para realizar un unit test de la entidad Cotizador
        Ingresando entradas validas y no validas, considerando validas las entradas
        con longitud correcta
    """
    def test_crear_cotizacion_valida(self):
        self.cotizacion = Cotizador.objects.create(cotizadorID="iedc1234WL",
                                                   fechaDeSolicitud=datetime.now(),
                                                   nombresCliente="Pablo Alberto",
                                                   apellidosCliente="Iglesias Garzon",
                                                   telefonoCliente="593-2434593",
                                                   mailCliente="test@iana.org.",
                                                   descripcionObra="Nada importante")

        self.assertIsInstance(self.cotizacion, Cotizador, 'Cotizacion creada')

    def test_crear_cotizacion_invalida(self):
        self.cotizacion = Cotizador.objects.create(cotizadorID="iedc1234WL000",
                                                   fechaDeSolicitud=datetime.now(),
                                                   nombresCliente="Pablo Alberto",
                                                   apellidosCliente="Iglesias Garzon",
                                                   telefonoCliente="593-2434593",
                                                   mailCliente="test@iana.org.",
                                                   descripcionObra="Nada importante")
        try:
            self.cotizacion.full_clean()
        except:
            print "Test Cotizacion invalida: Cotizacion Invalida"


class TestCajaNegraProducto(LiveServerTestCase):
    '''
    Clase para realizar prueba de caja negra para la entidad Producto
    '''
    def setUp(self):
        self.driver = webdriver.PhantomJS()
        # self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(6)
        self.driver.set_window_size(1120, 550)

    def tearDown(self):
        self.driver.quit()

    def test_api_producto(self):
        client = Client()
        response = client.get('http://localhost:8081/api/producto/?format=json')
        self.assertEqual(response.status_code, 200)
