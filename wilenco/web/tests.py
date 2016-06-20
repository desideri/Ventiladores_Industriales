'''
@Autores: Wilenco team
@Ultima modificacion: junio 20/2016
Pruebas de caja negra para proyecto
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
       Las input que se deben probar son para el campo Nombre, Email,
       Telefono del Usuario.
       Pre Condiciones:
       - Inputs No Vacio.
       - Inputs Validos (Validados por Expresiones regulares).
    """
    def setUp(self):
        self.driver = webdriver.PhantomJS()
        self.driver.implicitly_wait(15)

    def test_nombre_correcto(self):
        """
        En esta prueba se utiliza la clase de equivalencia CE1.
        Como resultado, el usuario no debe ver ningun mensaje
        y los campos del formulario se limpian.
        """
        self.driver.get("http://localhost:8081/contacto/")
        tiempo_inicio_prueba = datetime.now().second
        self.driver.find_element_by_id('nombreUsuario').send_keys("Wilson Enriquez")
        self.driver.find_element_by_id('emailUsuario').send_keys("wilenco@hotmail.com")
        self.driver.find_element_by_id('telUsuario').send_keys("042-587452")
        self.driver.find_element_by_id('asuntoUsuario').send_keys("Mantenimiento de Centrales de Aire tipo Split.")
        self.driver.find_element_by_id("btnEnviar").click()
        mensaje_error = self.driver.find_element_by_id("ErrorMessage")
        formularioEnviado = not mensaje_error.is_displayed()
        tiempo_fin_prueba = datetime.now().second - tiempo_inicio_prueba
        if(formularioEnviado):
            print "Prueba de nombre correcto EXITOSA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"
        else:
            print "Prueba de nombre correcto FALLIDA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"
        self.assertFalse(formularioEnviado)

    def test_nombre_incorrecto(self):
        """
        En esta prueba se utiliza la clase de equivalencia CE2.
        Como resultado, el usuario no debe ver ningun mensaje
        y los campos del formulario se limpian.
        """
        self.driver.get("http://localhost:8081/contacto/")
        tiempo_inicio_prueba = datetime.now().second
        self.driver.find_element_by_id('nombreUsuario').send_keys("$######")
        self.driver.find_element_by_id('emailUsuario').send_keys("wilenco@hotmail.com")
        self.driver.find_element_by_id('telUsuario').send_keys("042-587452")
        self.driver.find_element_by_id('asuntoUsuario').send_keys("Mantenimiento de Centrales de Aire tipo Split.")
        self.driver.find_element_by_id("btnEnviar").click()
        msg_ok = self.driver.find_element_by_id("OkMessage")
        formularioNoEnviado =  msg_ok.is_displayed()
        tiempo_fin_prueba = datetime.now().second - tiempo_inicio_prueba
        if(formularioNoEnviado):
            print "Prueba de nombre incorrecto EXITOSA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"
        else:
            print "Prueba de nombre incorrecto FALLIDA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"
        self.assertTrue(formularioNoEnviado)

    def test_email_correcto(self):
        """
        En esta prueba se utiliza la clase de equivalencia CE1.
        Como resultado, el usuario no debe ver ningun mensaje
        y los campos del formulario se limpian.
        """
        self.driver.get("http://localhost:8081/contacto/")
        tiempo_inicio_prueba = datetime.now().second
        self.driver.find_element_by_id('nombreUsuario').send_keys("Jorge Ayala")
        self.driver.find_element_by_id('emailUsuario').send_keys("test@iana.org")
        self.driver.find_element_by_id('telUsuario').send_keys("042-587452")
        self.driver.find_element_by_id('asuntoUsuario').send_keys("Mantenimiento de Centrales de Aire tipo Split.")
        self.driver.find_element_by_id("btnEnviar").click()
        mensaje_error = self.driver.find_element_by_id("ErrorMessage")
        formularioEnviado =  mensaje_error.is_displayed()
        tiempo_fin_prueba = datetime.now().second - tiempo_inicio_prueba
        if(formularioEnviado):
            print "Prueba de email correcto EXITOSA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"
        else:
            print "Prueba de email correcto FALLIDA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"
        self.assertTrue(formularioEnviado)



    def test_email_incorrecto(self):
        '''
        En esta prueba se utiliza la clase de equivalencia CE2.
        Como resultado, el usuario debe ver un mensaje de email
        incorrecto en rojo.
        '''
        self.driver.get("http://localhost:8081/contacto/")
        tiempo_inicio_prueba = datetime.now().second
        self.driver.find_element_by_id('nombreUsuario').send_keys("Jorge Ayala")
        self.driver.find_element_by_id('emailUsuario').send_keys("testiana.org")
        self.driver.find_element_by_id('telUsuario').send_keys("042-587452")
        self.driver.find_element_by_id('asuntoUsuario').send_keys("Mantenimiento de Centrales de Aire tipo Split.")
        self.driver.find_element_by_id("btnEnviar").click()
        msg_ok = self.driver.find_element_by_id("OkMessage")
        formularioNoEnviado = msg_ok.is_displayed()
        tiempo_fin_prueba = datetime.now().second - tiempo_inicio_prueba
        if(formularioNoEnviado):
            print "Prueba de email incorrecto EXITOSA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"
        else:
            print "Prueba de email incorrecto FALLIDA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"
        self.assertTrue(formularioNoEnviado)

    def test_telefono_correcto(self):
        """
        En esta prueba se utiliza la clase de equivalencia CE1.
        Como resultado, el usuario no debe ver ningun mensaje
        y los campos del formulario se limpian.
        """
        self.driver.get("http://localhost:8081/contacto/")
        tiempo_inicio_prueba = datetime.now().second
        self.driver.find_element_by_id('nombreUsuario').send_keys("Kattya Desiderio")
        self.driver.find_element_by_id('emailUsuario').send_keys("desideri@yahoo.com")
        self.driver.find_element_by_id('telUsuario').send_keys("053-581152")
        self.driver.find_element_by_id('asuntoUsuario').send_keys("Mantenimiento de Centrales de Aire tipo Split.")
        self.driver.find_element_by_id("btnEnviar").click()
        mensaje_error = self.driver.find_element_by_id("ErrorMessage")
        formularioEnviado = mensaje_error.is_displayed()
        tiempo_fin_prueba = datetime.now().second - tiempo_inicio_prueba
        if(formularioEnviado):
            print "Prueba de telefono correcto EXITOSA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"
        else:
            print "Prueba de telefono correcto FALLIDA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"
        self.assertTrue(formularioEnviado)

    def test_telefono_incorrecto(self):
        """
        En esta prueba se utiliza la clase de equivalencia CE1.
        Como resultado, el usuario no debe ver ningun mensaje
        y los campos del formulario se limpian.
        """
        tiempo_inicio_prueba = datetime.now().second
        self.driver.get("http://localhost:8081/contacto/")
        self.driver.find_element_by_id('nombreUsuario').send_keys("Wilson Enriquez")
        self.driver.find_element_by_id('emailUsuario').send_keys("wilenco@hotmail.com")
        self.driver.find_element_by_id('telUsuario').send_keys("042-587")
        self.driver.find_element_by_id('asuntoUsuario').send_keys("Mantenimiento de Centrales de Aire tipo Split.")
        self.driver.find_element_by_id("btnEnviar").click()
        msg_ok = self.driver.find_element_by_id("OkMessage")
        formularioNoEnviado = msg_ok.is_displayed()
        tiempo_fin_prueba = datetime.now().second - tiempo_inicio_prueba
        if(formularioNoEnviado):
            print "Prueba de telefono incorrecto EXITOSA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"
        else:
            print "Prueba de telefono incorrecto FALLIDA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"
        self.assertTrue(formularioNoEnviado)

    def tearDown(self):
        self.driver.quit()


class TestCajaNegraModeloSolicitud(TestCase):
    """
        @Autor: Israel Fernandez
        Clase para realizar un unit test del modelo Solicitud
        Ingresando entradas validas y no validas
    """
    def test_crear_solicitud_valida(self):
        tiempo_inicio_prueba = datetime.now().second
        self.cliente = Cliente.objects.create(cedula="0123457891", nombre="cliente",
                                              direccion="testlandia", telefono="0913458119",
                                              email="test@test.com")
        self.solicitud = Solicitud.objects.create(tipoSolicitud="MANT", descripcion="test",
                                                  fechaEscojida=datetime.now(),
                                                  cliente=self.cliente)

        tiempo_fin_prueba = datetime.now().second - tiempo_inicio_prueba
        if(isinstance(self.solicitud, Solicitud)):
            print "Prueba de crear Solicitud valida EXITOSA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"
        else:
            print "Prueba de crear Solicitud valida FALLIDA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"
        self.assertIsInstance(self.solicitud, Solicitud, 'Solicitud exitosa')

    def test_crear_solicitud_invalida(self):
        tiempo_inicio_prueba = datetime.now().second
        self.solicitud = None
        try:
            self.solicitud = Solicitud.objects.create(tipoSolicitud="INST", descripcion="test",
                                                      fechaEscojida=datetime.now())
        except:
            tiempo_fin_prueba = datetime.now().second - tiempo_inicio_prueba
            if(isinstance(self.solicitud, Solicitud)):
                print "Prueba de crear Solicitud invalida FALLIDA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"
            else:
                print "Prueba de crear Solicitud invalida EXITOSA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"
            self.assertNotIsInstance(self.solicitud, Solicitud, 'Solicitud Invalida')



class TestCajaNegraModeloCliente(TestCase):
    """
        @Autor: Wilson Enriquez
        Clase para realizar un unit test del modelo Cliente
        Ingresando entradas validas y no validas
    """
    def test_crear_cliente_valido(self):
        tiempo_inicio_prueba = datetime.now().second
        self.cliente = Cliente.objects.create(cedula="0123457891", nombre="cliente",
                                              direccion="testlandia", telefono="0913458119",
                                              email="test@test.com")

        tiempo_fin_prueba = datetime.now().second - tiempo_inicio_prueba
        if(isinstance(self.cliente, Cliente)):
            print "Prueba de crear Cliente valida EXITOSA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"
        else:
            print "Prueba de crear Cliente valida FALLIDA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"
        self.assertIsInstance(self.cliente, Cliente, 'Creacion de nuevo Cliente exitosa')

    def test_crear_cliente_invalido(self):
        tiempo_inicio_prueba = datetime.now().second
        self.cliente = None
        try:
            self.cliente = Cliente.objects.create(cedula="012345654545782", nombre="cliente",
                                                  direccion="testlandia", telefono="0913458119",
                                                  email="test@test.com")
        except:
            tiempo_fin_prueba = datetime.now().second - tiempo_inicio_prueba
            if(isinstance(self.cliente, Cliente)):
                print "Prueba de crear Cliente invalido FALLIDA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"
            else:
                print "Prueba de crear Cliente invalido EXITOSA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"

            self.assertNotIsInstance(self.cliente, Cliente, 'Creacion de nuevo Cliente invalida')


class TestCajaNegraModeloCotizacion(TestCase):
    """
        @Autor: Jorge Ayala
        Clase para realizar un unit test de la entidad Cotizador
        Ingresando entradas validas y no validas, considerando validas las entradas
        con longitud correcta
    """
    def test_crear_cotizacion_valida(self):
        tiempo_inicio_prueba = datetime.now().second
        self.cliente = Cliente.objects.create(cedula="0123457891", nombre="cliente",
                                              direccion="testlandia", telefono="0913458119",
                                              email="test@test.com")

        self.producto1 = Producto.objects.create(noSerie="12345", nombre="testproduct",
                                                 stock=12, marca="test",
                                                 categoria="test", potencia="10KW",
                                                 capacidad="120BTU", descripcion="test")

        self.producto2 = Producto.objects.create(noSerie="12345", nombre="testproduct",
                                                 stock=12, marca="test",
                                                 categoria="test", potencia="10KW",
                                                 capacidad="120BTU", descripcion="test")

        self.cotizacion = Cotizacion.objects.create(cotizadorID="iedc1234WL",
                                                   cliente = self.cliente,
                                                   descripcionObra="Nada importante")

        self.cotizacion.producto.add(self.producto1)
        self.cotizacion.producto.add(self.producto2)
        tiempo_fin_prueba = datetime.now().second - tiempo_inicio_prueba
        if(isinstance(self.cotizacion, Cotizacion)):
            print "Prueba de crear Cotizacion valida EXITOSA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"
        else:
            print "Prueba de crear Cotizacion valida FALLIDA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"
        self.assertIsInstance(self.cotizacion, Cotizacion, 'Cotizacion creada')

    def test_crear_cotizacion_invalida(self):
        tiempo_inicio_prueba = datetime.now().second
        self.cliente = Cliente.objects.create(cedula="0123457323891", nombre="cliente",
                                              direccion="testlandia", telefono="0913458119",
                                              email="testtestcom")

        self.producto1 = Producto.objects.create(noSerie="12345", nombre="testproduct",
                                                 stock=12, marca="test",
                                                 categoria="test", potencia="10KW",
                                                 capacidad="120BTU", descripcion="test")

        self.producto2 = Producto.objects.create(noSerie="12345", nombre="testproduct",
                                                 stock=12, marca="test",
                                                 categoria="test", potencia="10KW",
                                                 capacidad="120BTU", descripcion="test")

        self.cotizacion = None

        try:
            self.cotizacion = Cotizacion.objects.create(cotizadorID="iedc1234WL",
                                                       descripcionObra="Nada importante")
        except:
            tiempo_fin_prueba = datetime.now().second - tiempo_inicio_prueba
            if(isinstance(self.cotizacion, Cotizacion)):
                print "Prueba de crear Cotizacion invalido FALLIDA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"
            else:
                print "Prueba de crear Cotizacion invalido EXITOSA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"
            self.assertNotIsInstance(self.cotizacion, Cotizacion, 'Cotizacion creada')


class TestCajaNegraProducto(LiveServerTestCase):
    """
        @Autor: Kattya Desiderio
        Clase para realizar prueba de caja negra para la entidad Producto
    """

    def test_api_producto(self):
        client = Client()
        response = client.get('http://localhost:8081/api/producto/?format=json')
        self.assertEqual(response.status_code, 200)
