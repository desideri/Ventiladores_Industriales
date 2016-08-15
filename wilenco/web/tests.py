'''
@Autores: Wilenco team
@Ultima modificacion: julio 24/2016
@Modificado por: Jorge Ayala
Pruebas de caja negra para proyecto
Este script contienen funciones que permiten realizar pruebas de caja
negra sobre las componentes del sistemas ya desarrolladas. Para ello
se usan la libreria Selenium y PhantomJS, que permiten interactuar
con la interfaz grafica de la aplicacion usando un web browser que
permite el ingreso de datos a elementos como formularios y dar clic
sobre botones u otros elementos usando codigo.
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
       @Ultima modificacion: julio 17/2016
       @Modificado por: Jorge Ayala
       Como su nombre lo indica, es una clase usada para realizar test.
       En este caso se lo usa para realizar pruebas de Caja negra al
       formulario de la pagina Contacto de nuestro sitio web.
       Las variables a probar son Nombre, Email, Telefono del Usuario.
       Pre Condiciones para todas las pruebas:
       - Inputs No Vacios.

    """

    def setUp(self):
        self.driver = webdriver.PhantomJS()
        self.driver.implicitly_wait(15)

    def test_ingreso_nombre(self):
        """
        Para la variable nombre se han definido dos clases de equivalencia:
        CE1: cadenas de caracteres generadas por el regex definido en el codigo
        CE2: cadenas de caracteres no generados por el regex definido en el codigo

        En esta prueba se utiliza la clase de equivalencia CE1.
        Precondiciones:
            - las demas inputs son ingresados correctamente
        Resultado:
        Como resultado, el usuario no debe ver ningun mensaje
        y los campos del formulario se limpian.
        """
        self.driver.get("http://localhost:8081/contacto/")
        tiempo_inicio_prueba = datetime.now().second
        self.driver.find_element_by_id(
            'nombreUsuario').send_keys("Wilson Enriquez")
        self.driver.find_element_by_id(
            'emailUsuario').send_keys("wilenco@hotmail.com")
        self.driver.find_element_by_id('telUsuario').send_keys("042-587452")
        self.driver.find_element_by_id('asuntoUsuario').send_keys(
            "Mantenimiento de Centrales de Aire tipo Split.")
        self.driver.find_element_by_id("btnEnviar").click()
        mensaje_error = self.driver.find_element_by_id("ErrorMessage")
        formularioEnviado = not mensaje_error.is_displayed()
        tiempo_fin_prueba = datetime.now().second - tiempo_inicio_prueba
        if(formularioEnviado):
            print "Formulario Contacto. Prueba de nombre correcto EXITOSA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"
        else:
            print "Formulario Contacto. Prueba de nombre correcto FALLIDA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"

        self.driver.get("http://localhost:8081/contacto/")
        tiempo_inicio_prueba = datetime.now().second
        self.driver.find_element_by_id(
            'nombreUsuario').send_keys("$######")
        self.driver.find_element_by_id(
            'emailUsuario').send_keys("wilenco@hotmail.com")
        self.driver.find_element_by_id('telUsuario').send_keys("042-587452")
        self.driver.find_element_by_id('asuntoUsuario').send_keys(
            "Mantenimiento de Centrales de Aire tipo Split.")
        self.driver.find_element_by_id("btnEnviar").click()
        mensaje_error = self.driver.find_element_by_id("ErrorMessage")
        formularioNoEnviado = not mensaje_error.is_displayed()
        tiempo_fin_prueba = datetime.now().second - tiempo_inicio_prueba
        if(formularioNoEnviado):
            print "Formulario Contacto. Prueba de nombre incorrecto EXITOSA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"
        else:
            print "Formulario Contacto. Prueba de nombre incorrecto FALLIDA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"

        pruebaExitosa = formularioNoEnviado and formularioEnviado
        self.assertFalse(pruebaExitosa)

    def test_ingreso_email(self):
        """
        Para la variable email se han definido dos clases de equivalencia:
        CE3: cadenas de caracteres generadas por el regex definido en el codigo
        CE4: cadenas de caracteres no generados por el regex definido en el codigo

        En esta prueba se utiliza la clase de equivalencia CE3.
        Precondiciones:
            - las demas inputs son ingresados correctamente
        Resultado:
        Como resultado, el usuario ve un mensaje de exito
        y los campos del formulario se limpian.
        """
        self.driver.get("http://localhost:8081/contacto/")
        tiempo_inicio_prueba = datetime.now().second
        self.driver.find_element_by_id(
            'nombreUsuario').send_keys("Jorge Ayala")
        self.driver.find_element_by_id(
            'emailUsuario').send_keys("test@iana.org")
        self.driver.find_element_by_id('telUsuario').send_keys("042-587452")
        self.driver.find_element_by_id('asuntoUsuario').send_keys(
            "Mantenimiento de Centrales de Aire tipo Split.")
        self.driver.find_element_by_id("btnEnviar").click()
        mensaje_error = self.driver.find_element_by_id("ErrorMessage")
        formularioEnviado = not mensaje_error.is_displayed()
        tiempo_fin_prueba = datetime.now().second - tiempo_inicio_prueba
        if(formularioEnviado):
            print "Formulario Contacto. Prueba de email correcto EXITOSA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"
        else:
            print "Formulario Contacto. Prueba de email correcto FALLIDA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"

        self.driver.get("http://localhost:8081/contacto/")
        tiempo_inicio_prueba = datetime.now().second
        self.driver.find_element_by_id(
            'nombreUsuario').send_keys("Jorge Ayala")
        self.driver.find_element_by_id(
            'emailUsuario').send_keys("testiana.org")
        self.driver.find_element_by_id('telUsuario').send_keys("042-587452")
        self.driver.find_element_by_id('asuntoUsuario').send_keys(
            "Mantenimiento de Centrales de Aire tipo Split.")
        self.driver.find_element_by_id("btnEnviar").click()
        msg_ok = self.driver.find_element_by_id("OkMessage")
        formularioNoEnviado = not msg_ok.is_displayed()
        tiempo_fin_prueba = datetime.now().second - tiempo_inicio_prueba
        if(formularioNoEnviado):
            print "Formulario Contacto. Prueba de email incorrecto EXITOSA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"
        else:
            print "Formulario Contacto. Prueba de email incorrecto FALLIDA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"

        pruebaExitosa = formularioNoEnviado and formularioEnviado
        self.assertTrue(pruebaExitosa)

    def test_ingreso_telefono(self):
        """
        Para la variable telefono se han definido dos clases de equivalencia:
        CE5: cadenas de caracteres generadas por el regex definido en el codigo
        CE6: cadenas de caracteres no generados por el regex definido en el codigo

        En esta prueba se utiliza la clase de equivalencia CE5.
        Precondiciones:
            - las demas inputs son ingresados correctamente
        Resultado:
        Como resultado, el usuario ve un mensaje de exito
        y los campos del formulario se limpian.
        """
        self.driver.get("http://localhost:8081/contacto/")
        tiempo_inicio_prueba = datetime.now().second
        self.driver.find_element_by_id(
            'nombreUsuario').send_keys("Kattya Desiderio")
        self.driver.find_element_by_id(
            'emailUsuario').send_keys("desideri@yahoo.com")
        self.driver.find_element_by_id('telUsuario').send_keys("053-581152")
        self.driver.find_element_by_id('asuntoUsuario').send_keys(
            "Mantenimiento de Centrales de Aire tipo Split.")
        self.driver.find_element_by_id("btnEnviar").click()
        mensaje_error = self.driver.find_element_by_id("ErrorMessage")
        formularioEnviado = not mensaje_error.is_displayed()
        tiempo_fin_prueba = datetime.now().second - tiempo_inicio_prueba
        if(formularioEnviado):
            print "Formulario Contacto. Prueba de telefono correcto EXITOSA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"
        else:
            print "Formulario Contacto. Prueba de telefono correcto FALLIDA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"

        self.driver.get("http://localhost:8081/contacto/")
        tiempo_inicio_prueba = datetime.now().second
        self.driver.find_element_by_id(
            'nombreUsuario').send_keys("Kattya Desiderio")
        self.driver.find_element_by_id(
            'emailUsuario').send_keys("desideri@yahoo.com")
        self.driver.find_element_by_id('telUsuario').send_keys("042-587")
        self.driver.find_element_by_id('asuntoUsuario').send_keys(
            "Mantenimiento de Centrales de Aire tipo Split.")
        self.driver.find_element_by_id("btnEnviar").click()
        mensaje_error = self.driver.find_element_by_id("ErrorMessage")
        formularioNoEnviado = not mensaje_error.is_displayed()
        tiempo_fin_prueba = datetime.now().second - tiempo_inicio_prueba
        if(formularioNoEnviado):
            print "Formulario Contacto. Prueba de telefono incorrecto EXITOSA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"
        else:
            print "Formulario Contacto. Prueba de telefono incorrecto FALLIDA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"

        pruebaExitosa = formularioNoEnviado and formularioEnviado
        self.assertFalse(pruebaExitosa)

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
        self.cliente = Cliente.objects.create(
            cedula="0123457891",
            nombre="cliente",
            direccion="testlandia",
            telefono="0913458119",
            email="test@test.com")
        self.solicitud = Solicitud.objects.create(
            tipoSolicitud="MANT",
            descripcion="test",
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
            self.solicitud = Solicitud.objects.create(
                tipoSolicitud="INST", descripcion="test", fechaEscojida=datetime.now())
        except:
            tiempo_fin_prueba = datetime.now().second - tiempo_inicio_prueba
            if(isinstance(self.solicitud, Solicitud)):
                print "Prueba de crear Solicitud invalida FALLIDA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"
            else:
                print "Prueba de crear Solicitud invalida EXITOSA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"
            self.assertNotIsInstance(
                self.solicitud, Solicitud, 'Solicitud Invalida')


class TestCajaNegraModeloCliente(TestCase):
    """
        @Autor: Wilson Enriquez
        Clase para realizar un unit test del modelo Cliente
        Ingresando entradas validas y no validas
    """

    def test_crear_cliente_valido(self):
        tiempo_inicio_prueba = datetime.now().second
        self.cliente = Cliente.objects.create(
            cedula="0123457891",
            nombre="cliente",
            direccion="testlandia",
            telefono="0913458119",
            email="test@test.com")

        tiempo_fin_prueba = datetime.now().second - tiempo_inicio_prueba
        if(isinstance(self.cliente, Cliente)):
            print "Prueba de crear Cliente valida EXITOSA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"
        else:
            print "Prueba de crear Cliente valida FALLIDA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"
        self.assertIsInstance(
            self.cliente,
            Cliente,
            'Creacion de nuevo Cliente exitosa')

    def test_crear_cliente_invalido(self):
        tiempo_inicio_prueba = datetime.now().second
        self.cliente = None
        try:
            self.cliente = Cliente.objects.create(
                cedula="012345654545782",
                nombre="cliente",
                direccion="testlandia",
                telefono="0913458119",
                email="test@test.com")
        except:
            tiempo_fin_prueba = datetime.now().second - tiempo_inicio_prueba
            if(isinstance(self.cliente, Cliente)):
                print "Prueba de crear Cliente invalido FALLIDA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"
            else:
                print "Prueba de crear Cliente invalido EXITOSA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"

            self.assertNotIsInstance(
                self.cliente, Cliente, 'Creacion de nuevo Cliente invalida')


class TestCajaNegraModeloCotizacion(TestCase):
    """
        @Autor: Jorge Ayala
        Clase para realizar un unit test de la entidad Cotizador
        Ingresando entradas validas y no validas, considerando validas las entradas
        con longitud correcta
    """

    def test_crear_cotizacion_valida(self):
        tiempo_inicio_prueba = datetime.now().second
        self.cliente = Cliente.objects.create(
            cedula="0123457891",
            nombre="cliente",
            direccion="testlandia",
            telefono="0913458119",
            email="test@test.com")

        self.producto1 = Producto.objects.create(
            noSerie="12345",
            nombre="testproduct",
            stock=12,
            marca="test",
            categoria="test",
            potencia="10KW",
            capacidad="120BTU",
            descripcion="test")

        self.producto2 = Producto.objects.create(
            noSerie="12345",
            nombre="testproduct",
            stock=12,
            marca="test",
            categoria="test",
            potencia="10KW",
            capacidad="120BTU",
            descripcion="test")

        self.cotizacion = Cotizacion.objects.create(
            cotizadorID="iedc1234WL",
            cliente=self.cliente,
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
        self.cliente = Cliente.objects.create(
            cedula="0123457323",
            nombre="cliente",
            direccion="testlandia",
            telefono="0913458119",
            email="testtestcom")

        self.producto1 = Producto.objects.create(
            noSerie="12345",
            nombre="testproduct",
            stock=12,
            marca="test",
            categoria="test",
            potencia="10KW",
            capacidad="120BTU",
            descripcion="test")

        self.producto2 = Producto.objects.create(
            noSerie="12345",
            nombre="testproduct",
            stock=12,
            marca="test",
            categoria="test",
            potencia="10KW",
            capacidad="120BTU",
            descripcion="test")

        self.cotizacion = None

        try:
            self.cotizacion = Cotizacion.objects.create(
                cotizadorID="iedc1234WL", descripcionObra="Nada importante")
        except:
            tiempo_fin_prueba = datetime.now().second - tiempo_inicio_prueba
            if(isinstance(self.cotizacion, Cotizacion)):
                print "Prueba de crear Cotizacion invalido FALLIDA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"
            else:
                print "Prueba de crear Cotizacion invalido EXITOSA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"
            self.assertNotIsInstance(
                self.cotizacion, Cotizacion, 'Cotizacion creada')


class TestCajaNegraFormularioServicio(LiveServerTestCase):
    """
       @Autor: Jorge Ayala
       @Ultima modificacion: julio 17/2016
       @Modificado por: Jorge Ayala
       Como su nombre lo indica, es una clase usada para realizar test.
       En este caso se lo usa para realizar pruebas de Caja negra a la
       Pagina Servicio de nuestro sitio web.
       Las input que se deben probar son para el campo Nombre,Apellido, Email,
       Telefono del Usuario, asi como la Descripcion del  servicio.
       Pre Condiciones para todas las pruebas:
       - Inputs No Vacio.

    """

    def setUp(self):
        self.driver = webdriver.PhantomJS()
        self.driver.implicitly_wait(15)

    def test_ingreso_nombre(self):
        """
        Para la variable nombre se han definido dos clases de equivalencia:
        CE7: cadenas de caracteres generadas por el regex definido en el codigo
        CE8: cadenas de caracteres no generados  por el regex definido en el codigo

        En esta prueba se utiliza la clase de equivalencia CE7.
        Precondiciones:
            - las demas inputs son ingresados correctamente
        Resultado:
        Como resultado, el usuario ve un mensaje de exito
        y los campos del formulario se limpian.
        """
        self.driver.get("http://localhost:8081/servicio/")
        tiempo_inicio_prueba = datetime.now().second
        self.driver.find_element_by_id('nombreCliente').send_keys("Wilson")
        self.driver.find_element_by_id('apellidoCliente').send_keys("Enriquez")
        self.driver.find_element_by_id(
            'emailCliente').send_keys("wilenco@hotmail.com")
        self.driver.find_element_by_id('telCliente').send_keys("042-587452")
        self.driver.find_element_by_id('cedulaCliente').send_keys("0927219915")
        self.driver.find_element_by_id('direccionCliente').send_keys(
            "General Gomez 2012 y Los Rios")
        self.driver.find_element_by_id('descripcion').send_keys(
            "Mantenimiento de Centrales de Aire tipo Split.")
        self.driver.find_element_by_id("btnEnviar").click()
        mensaje_error = self.driver.find_element_by_id("ErrorMessage")
        formularioEnviado = not mensaje_error.is_displayed()
        tiempo_fin_prueba = datetime.now().second - tiempo_inicio_prueba
        if(formularioEnviado):
            print "Formulario Servicio.Prueba de nombre correcto FALLIDA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"
        else:
            print "Formulario Servicio.Prueba de nombre correcto EXITOSA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"

        self.driver.get("http://localhost:8081/servicio/")
        tiempo_inicio_prueba = datetime.now().second
        self.driver.find_element_by_id('nombreCliente').send_keys("$######")
        self.driver.find_element_by_id('apellidoCliente').send_keys("Enriquez")
        self.driver.find_element_by_id(
            'emailCliente').send_keys("wilenco@hotmail.com")
        self.driver.find_element_by_id('telCliente').send_keys("042-587452")
        self.driver.find_element_by_id('cedulaCliente').send_keys("0927219915")
        self.driver.find_element_by_id('direccionCliente').send_keys(
            "General Gomez 2012 y Los Rios")
        self.driver.find_element_by_id('descripcion').send_keys(
            "Mantenimiento de Centrales de Aire tipo Split.")
        self.driver.find_element_by_id("btnEnviar").click()
        msg_ok = self.driver.find_element_by_id("OkMessage")
        formularioNoEnviado = not msg_ok.is_displayed()
        tiempo_fin_prueba = datetime.now().second - tiempo_inicio_prueba
        if(formularioNoEnviado):
            print "Formulario Servicio.Prueba de nombre incorrecto EXITOSA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"
        else:
            print "Formulario Servicio.Prueba de nombre incorrecto FALLIDA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"

        pruebaExitosa = formularioNoEnviado and formularioEnviado
        self.assertFalse(pruebaExitosa)

    def test_ingreso_apellido(self):
        """
        Para la variable apellido se han definido dos clases de equivalencia:
        CE9: cadenas de caracteres generadas por el regex definido en el codigo
        CE10: cadenas de caracteres no generados por el regex definido en el codigo

        En esta prueba se utiliza la clase de equivalencia CE9.
        Precondiciones:
            - las demas inputs son ingresados correctamente
        Resultado:
        Como resultado, el usuario ve un mensaje de exito
        y los campos del formulario se limpian.
        """
        self.driver.get("http://localhost:8081/servicio/")
        tiempo_inicio_prueba = datetime.now().second
        self.driver.find_element_by_id('nombreCliente').send_keys("Wilson")
        self.driver.find_element_by_id('apellidoCliente').send_keys("Enriquez")
        self.driver.find_element_by_id(
            'emailCliente').send_keys("wilenco@hotmail.com")
        self.driver.find_element_by_id('telCliente').send_keys("042-587452")
        self.driver.find_element_by_id('cedulaCliente').send_keys("0927219915")
        self.driver.find_element_by_id('direccionCliente').send_keys(
            "General Gomez 2012 y Los Rios")
        self.driver.find_element_by_id('descripcion').send_keys(
            "Mantenimiento de Centrales de Aire tipo Split.")
        self.driver.find_element_by_id("btnEnviar").click()
        mensaje_error = self.driver.find_element_by_id("ErrorMessage")
        formularioEnviado = not mensaje_error.is_displayed()
        tiempo_fin_prueba = datetime.now().second - tiempo_inicio_prueba
        if(formularioEnviado):
            print "Formulario Servicio.Prueba de apellido correcto EXITOSA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"
        else:
            print "Formulario Servicio.Prueba de apellido correcto EXITOSA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"

        self.driver.get("http://localhost:8081/servicio/")
        tiempo_inicio_prueba = datetime.now().second
        self.driver.find_element_by_id('nombreCliente').send_keys("Wilson")
        self.driver.find_element_by_id('apellidoCliente').send_keys("$######")
        self.driver.find_element_by_id(
            'emailCliente').send_keys("wilenco@hotmail.com")
        self.driver.find_element_by_id('telCliente').send_keys("042-587452")
        self.driver.find_element_by_id('cedulaCliente').send_keys("0927219915")
        self.driver.find_element_by_id('direccionCliente').send_keys(
            "General Gomez 2012 y Los Rios")
        self.driver.find_element_by_id('descripcion').send_keys(
            "Mantenimiento de Centrales de Aire tipo Split.")
        self.driver.find_element_by_id("btnEnviar").click()
        msg_ok = self.driver.find_element_by_id("OkMessage")
        formularioNoEnviado = not msg_ok.is_displayed()
        tiempo_fin_prueba = datetime.now().second - tiempo_inicio_prueba
        if(formularioNoEnviado):
            print "Formulario Servicio.Prueba de apellido incorrecto EXITOSA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"
        else:
            print "Formulario Servicio.Prueba de apellido incorrecto FALLIDA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"
        pruebaExitosa = formularioNoEnviado and formularioEnviado
        self.assertFalse(pruebaExitosa)

    def test_ingreso_email(self):
        """
        Para la variable email se han definido dos clases de equivalencia:
        CE11: cadenas de caracteres generadas por el regex definido en el codigo
        CE12: cadenas de caracteres no generados por el regex definido en el codigo

        En esta prueba se utiliza la clase de equivalencia CE11.
        Precondiciones:
            - las demas inputs son ingresados correctamente
        Resultado:
        Como resultado, el usuario ve un mensaje de exito
        y los campos del formulario se limpian.
        """
        self.driver.get("http://localhost:8081/servicio/")
        tiempo_inicio_prueba = datetime.now().second
        self.driver.find_element_by_id('nombreCliente').send_keys("Wilson")
        self.driver.find_element_by_id('apellidoCliente').send_keys("Enriquez")
        self.driver.find_element_by_id(
            'emailCliente').send_keys("wilenco@hotmail.com")
        self.driver.find_element_by_id('telCliente').send_keys("042-587452")
        self.driver.find_element_by_id('cedulaCliente').send_keys("0927219915")
        self.driver.find_element_by_id('direccionCliente').send_keys(
            "General Gomez 2012 y Los Rios")
        self.driver.find_element_by_id('descripcion').send_keys(
            "Mantenimiento de Centrales de Aire tipo Split.")
        self.driver.find_element_by_id("btnEnviar").click()
        mensaje_error = self.driver.find_element_by_id("ErrorMessage")
        formularioEnviado = not mensaje_error.is_displayed()
        tiempo_fin_prueba = datetime.now().second - tiempo_inicio_prueba
        if(formularioEnviado):
            print "Formulario Servicio. Prueba de email correcto EXITOSA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"
        else:
            print "Formulario Servicio. Prueba de email correcto EXITOSA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"

        self.driver.get("http://localhost:8081/servicio/")
        tiempo_inicio_prueba = datetime.now().second
        self.driver.find_element_by_id('nombreCliente').send_keys("Wilson")
        self.driver.find_element_by_id('apellidoCliente').send_keys("Enriquez")
        self.driver.find_element_by_id(
            'emailCliente').send_keys("wilencohotmailom")
        self.driver.find_element_by_id('telCliente').send_keys("042-587452")
        self.driver.find_element_by_id('cedulaCliente').send_keys("0927219915")
        self.driver.find_element_by_id('direccionCliente').send_keys(
            "General Gomez 2012 y Los Rios")
        self.driver.find_element_by_id('descripcion').send_keys(
            "Mantenimiento de Centrales de Aire tipo Split.")
        self.driver.find_element_by_id("btnEnviar").click()
        msg_ok = self.driver.find_element_by_id("OkMessage")
        formularioNoEnviado = not msg_ok.is_displayed()
        tiempo_fin_prueba = datetime.now().second - tiempo_inicio_prueba
        if(formularioNoEnviado):
            print "Formulario Servicio. Prueba de email incorrecto EXITOSA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"
        else:
            print "Formulario Servicio. Prueba de email incorrecto FALLIDA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"

        pruebaExitosa = formularioNoEnviado and formularioEnviado
        self.assertFalse(pruebaExitosa)

    def test_ingreso_telefono(self):
        """
        Para la variable telefono se han definido dos clases de equivalencia:
        CE13: cadenas de caracteres generadas por el regex definido en el codigo
        CE14: cadenas de caracteres no generados por el regex definido en el codigo

        En esta prueba se utiliza la clase de equivalencia CE13.
        Precondiciones:
            - las demas inputs son ingresados correctamente
        Resultado:
        Como resultado, el usuario ve un mensaje de exito
        y los campos del formulario se limpian.
        """
        self.driver.get("http://localhost:8081/servicio/")
        tiempo_inicio_prueba = datetime.now().second
        self.driver.find_element_by_id('nombreCliente').send_keys("Wilson")
        self.driver.find_element_by_id('apellidoCliente').send_keys("Enriquez")
        self.driver.find_element_by_id(
            'emailCliente').send_keys("wilenco@hotmail.com")
        self.driver.find_element_by_id('telCliente').send_keys("042-587452")
        self.driver.find_element_by_id('cedulaCliente').send_keys("0927219915")
        self.driver.find_element_by_id('direccionCliente').send_keys(
            "General Gomez 2012 y Los Rios")
        self.driver.find_element_by_id('descripcion').send_keys(
            "Mantenimiento de Centrales de Aire tipo Split.")
        self.driver.find_element_by_id("btnEnviar").click()
        mensaje_error = self.driver.find_element_by_id("ErrorMessage")
        formularioEnviado = not mensaje_error.is_displayed()
        tiempo_fin_prueba = datetime.now().second - tiempo_inicio_prueba
        if(formularioEnviado):
            print "Formulario Servicio.Prueba de telefono correcto FALLIDA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"
        else:
            print "Formulario Servicio.Prueba de telefono correcto EXITOSA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"

        self.driver.get("http://localhost:8081/servicio/")
        tiempo_inicio_prueba = datetime.now().second
        self.driver.find_element_by_id('nombreCliente').send_keys("Wilson")
        self.driver.find_element_by_id('apellidoCliente').send_keys("Enriquez")
        self.driver.find_element_by_id(
            'emailCliente').send_keys("wilenco@hotmail.com")
        self.driver.find_element_by_id('telCliente').send_keys("0978095645")
        self.driver.find_element_by_id('cedulaCliente').send_keys("3927219915")
        self.driver.find_element_by_id('direccionCliente').send_keys(
            "General Gomez 2012 y Los Rios")
        self.driver.find_element_by_id('descripcion').send_keys(
            "Mantenimiento de Centrales de Aire tipo Split.")
        msg_ok = self.driver.find_element_by_id("OkMessage")
        formularioNoEnviado = not msg_ok.is_displayed()
        tiempo_fin_prueba = datetime.now().second - tiempo_inicio_prueba
        if(formularioNoEnviado):
            print "Formulario Servicio.Prueba de telefono incorrecto EXITOSA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"
        else:
            print "Formulario Servicio.Prueba de telefono incorrecto FALLIDA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"

        pruebaExitosa = formularioNoEnviado and formularioEnviado
        self.assertFalse(pruebaExitosa)

    def tearDown(self):
        self.driver.quit()


class TestCajaNegraFormularioCotizacion(LiveServerTestCase):
    """
       @Autor: Jorge Ayala
       @Ultima modificacion: julio 17/2016
       @Modificado por: Jorge Ayala
       Como su nombre lo indica, es una clase usada para realizar test.
       En este caso se lo usa para realizar pruebas de Caja negra a la
       Pagina Cotizacion de nuestro sitio web.
       Las input que se deben probar son para el campo Nombre,Apellido, Email,
       Telefono del Usuario, asi como la Descripcion del  servicio.
       Pre Condiciones:
       - Inputs No Vacio.
       - Inputs Validos (Validados por Expresiones regulares).
    """

    def setUp(self):
        self.driver = webdriver.PhantomJS()
        self.driver.implicitly_wait(15)

    def test_ingreso_nombre(self):
        """
        Para la variable nombre se han definido dos clases de equivalencia:
        CE15: cadenas de caracteres generadas por el regex definido en el codigo
        CE16: cadenas de caracteres no generados por el regex definido en el codigo

        En esta prueba se utiliza la clase de equivalencia CE15.
        Precondiciones:
            - las demas inputs son ingresados correctamente
        Resultado:
        Como resultado, el usuario ve un mensaje de exito
        y los campos del formulario se limpian.
        """
        self.driver.get("http://localhost:8081/cotizacion/")
        tiempo_inicio_prueba = datetime.now().second
        self.driver.find_element_by_id('nombreCliente').send_keys("Wilson")
        self.driver.find_element_by_id('apellidoCliente').send_keys("Enriquez")
        self.driver.find_element_by_id(
            'emailCliente').send_keys("wilenco@hotmail.com")
        self.driver.find_element_by_id('telCliente').send_keys("042-587452")
        self.driver.find_element_by_id('cedulaCliente').send_keys("0927219915")
        self.driver.find_element_by_id('direccionCliente').send_keys(
            "General Gomez 2012 y Los Rios")
        self.driver.find_element_by_id('descripcion').send_keys(
            "Mantenimiento de Centrales de Aire tipo Split.")
        self.driver.find_element_by_id("btnEnviar").click()
        mensaje_error = self.driver.find_element_by_id("ErrorMessage")
        formularioEnviado = not mensaje_error.is_displayed()
        tiempo_fin_prueba = datetime.now().second - tiempo_inicio_prueba
        if(formularioEnviado):
            print "Formulario Cotizacion.Prueba de nombre correcto EXITOSA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"
        else:
            print "Formulario Cotizacion.Prueba de nombre correcto FALLIDA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"

        self.driver.get("http://localhost:8081/cotizacion/")
        tiempo_inicio_prueba = datetime.now().second
        self.driver.find_element_by_id('nombreCliente').send_keys("$######")
        self.driver.find_element_by_id('apellidoCliente').send_keys("Enriquez")
        self.driver.find_element_by_id(
            'emailCliente').send_keys("wilenco@hotmail.com")
        self.driver.find_element_by_id('telCliente').send_keys("042-587452")
        self.driver.find_element_by_id('cedulaCliente').send_keys("0927219915")
        self.driver.find_element_by_id('direccionCliente').send_keys(
            "General Gomez 2012 y Los Rios")
        self.driver.find_element_by_id('descripcion').send_keys(
            "Mantenimiento de Centrales de Aire tipo Split.")
        self.driver.find_element_by_id("btnEnviar").click()
        msg_ok = self.driver.find_element_by_id("OkMessage")
        formularioNoEnviado = not msg_ok.is_displayed()
        tiempo_fin_prueba = datetime.now().second - tiempo_inicio_prueba
        if(formularioNoEnviado):
            print "Formulario Cotizacion.Prueba de nombre incorrecto EXITOSA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"
        else:
            print "Formulario Cotizacion.Prueba de nombre incorrecto FALLIDA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"

        pruebaExitosa = formularioNoEnviado and formularioEnviado
        self.assertTrue(pruebaExitosa)

    def test_ingreso_apellido(self):
        """
        Para la variable apellido se han definido dos clases de equivalencia:
        CE17: cadenas de caracteres generadas por el regex definido en el codigo
        CE18: cadenas de caracteres no generados por el regex definido en el codigo

        En esta prueba se utiliza la clase de equivalencia CE17.
        Precondiciones:
            - las demas inputs son ingresados correctamente
        Resultado:
        Como resultado, el usuario ve un mensaje de exito
        y los campos del formulario se limpian.
        """
        self.driver.get("http://localhost:8081/cotizacion/")
        tiempo_inicio_prueba = datetime.now().second
        self.driver.find_element_by_id('nombreCliente').send_keys("Wilson")
        self.driver.find_element_by_id('apellidoCliente').send_keys("Enriquez")
        self.driver.find_element_by_id(
            'emailCliente').send_keys("wilenco@hotmail.com")
        self.driver.find_element_by_id('telCliente').send_keys("042-587452")
        self.driver.find_element_by_id('cedulaCliente').send_keys("0927219915")
        self.driver.find_element_by_id('direccionCliente').send_keys(
            "General Gomez 2012 y Los Rios")
        self.driver.find_element_by_id('descripcion').send_keys(
            "Mantenimiento de Centrales de Aire tipo Split.")
        self.driver.find_element_by_id("btnEnviar").click()
        mensaje_error = self.driver.find_element_by_id("ErrorMessage")
        formularioEnviado = not mensaje_error.is_displayed()
        tiempo_fin_prueba = datetime.now().second - tiempo_inicio_prueba
        if(formularioEnviado):
            print "Formulario Cotizacion.Prueba de apellido correcto EXITOSA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"
        else:
            print "Formulario Cotizacion.Prueba de apellido correcto FALLIDA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"

        self.driver.get("http://localhost:8081/cotizacion/")
        tiempo_inicio_prueba = datetime.now().second
        self.driver.find_element_by_id('nombreCliente').send_keys("Wilson")
        self.driver.find_element_by_id('apellidoCliente').send_keys("$######")
        self.driver.find_element_by_id(
            'emailCliente').send_keys("wilenco@hotmail.com")
        self.driver.find_element_by_id('telCliente').send_keys("042-587452")
        self.driver.find_element_by_id('cedulaCliente').send_keys("0927219915")
        self.driver.find_element_by_id('direccionCliente').send_keys(
            "General Gomez 2012 y Los Rios")
        self.driver.find_element_by_id('descripcion').send_keys(
            "Mantenimiento de Centrales de Aire tipo Split.")
        self.driver.find_element_by_id("btnEnviar").click()
        msg_ok = self.driver.find_element_by_id("OkMessage")
        formularioNoEnviado = not msg_ok.is_displayed()
        tiempo_fin_prueba = datetime.now().second - tiempo_inicio_prueba
        if(formularioNoEnviado):
            print "Formulario Cotizacion.Prueba de apellido incorrecto EXITOSA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"
        else:
            print "Formulario Cotizacion.Prueba de apellido incorrecto FALLIDA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"

        pruebaExitosa = formularioNoEnviado and formularioEnviado
        self.assertTrue(pruebaExitosa)

    def test_ingreso_email(self):
        """
        Para la variable email se han definido dos clases de equivalencia:
        CE19: cadenas de caracteres generadas por el regex definido en el codigo
        CE20: cadenas de caracteres no generados por el regex definido en el codigo

        En esta prueba se utiliza la clase de equivalencia CE19.
        Precondiciones:
            - las demas inputs son ingresados correctamente
        Resultado:
        Como resultado, el usuario ve un mensaje de exito
        y los campos del formulario se limpian.
        """
        self.driver.get("http://localhost:8081/cotizacion/")
        tiempo_inicio_prueba = datetime.now().second
        self.driver.find_element_by_id('nombreCliente').send_keys("Wilson")
        self.driver.find_element_by_id('apellidoCliente').send_keys("Enriquez")
        self.driver.find_element_by_id(
            'emailCliente').send_keys("wilenco@hotmail.com")
        self.driver.find_element_by_id('telCliente').send_keys("042-587452")
        self.driver.find_element_by_id('cedulaCliente').send_keys("0927219915")
        self.driver.find_element_by_id('direccionCliente').send_keys(
            "General Gomez 2012 y Los Rios")
        self.driver.find_element_by_id('descripcion').send_keys(
            "Mantenimiento de Centrales de Aire tipo Split.")
        self.driver.find_element_by_id("btnEnviar").click()
        mensaje_error = self.driver.find_element_by_id("ErrorMessage")
        formularioEnviado = not mensaje_error.is_displayed()
        tiempo_fin_prueba = datetime.now().second - tiempo_inicio_prueba
        if(formularioEnviado):
            print "Formulario Cotizacion. Prueba de email correcto EXITOSA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"
        else:
            print "Formulario Cotizacion. Prueba de email correcto FALLIDA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"

        self.driver.get("http://localhost:8081/cotizacion/")
        tiempo_inicio_prueba = datetime.now().second
        self.driver.find_element_by_id('nombreCliente').send_keys("Wilson")
        self.driver.find_element_by_id('apellidoCliente').send_keys("Enriquez")
        self.driver.find_element_by_id(
            'emailCliente').send_keys("wilencohotmailom")
        self.driver.find_element_by_id('telCliente').send_keys("042-587452")
        self.driver.find_element_by_id('cedulaCliente').send_keys("0927219915")
        self.driver.find_element_by_id('direccionCliente').send_keys(
            "General Gomez 2012 y Los Rios")
        self.driver.find_element_by_id('descripcion').send_keys(
            "Mantenimiento de Centrales de Aire tipo Split.")
        self.driver.find_element_by_id("btnEnviar").click()
        msg_ok = self.driver.find_element_by_id("OkMessage")
        formularioNoEnviado = not msg_ok.is_displayed()
        tiempo_fin_prueba = datetime.now().second - tiempo_inicio_prueba
        if(formularioNoEnviado):
            print "Formulario Cotizacion. Prueba de email incorrecto EXITOSA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"
        else:
            print "Formulario Cotizacion. Prueba de email incorrecto FALLIDA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"

        pruebaExitosa = formularioNoEnviado and formularioEnviado
        self.assertTrue(pruebaExitosa)

    def test_ingreso_telefono(self):
        """
        Para la variable telefono se han definido dos clases de equivalencia:
        CE21: cadenas de caracteres generadas por el regex definido en el codigo
        CE22: cadenas de caracteres no generados por el regex definido en el codigo

        En esta prueba se utiliza la clase de equivalencia CE21.
        Precondiciones:
            - las demas inputs son ingresados correctamente
        Resultado:
        Como resultado, el usuario ve un mensaje de exito
        y los campos del formulario se limpian.
        """
        self.driver.get("http://localhost:8081/cotizacion/")
        tiempo_inicio_prueba = datetime.now().second
        self.driver.find_element_by_id('nombreCliente').send_keys("Wilson")
        self.driver.find_element_by_id('apellidoCliente').send_keys("Enriquez")
        self.driver.find_element_by_id(
            'emailCliente').send_keys("wilenco@hotmail.com")
        self.driver.find_element_by_id('telCliente').send_keys("042-587452")
        self.driver.find_element_by_id('cedulaCliente').send_keys("0927219915")
        self.driver.find_element_by_id('direccionCliente').send_keys(
            "General Gomez 2012 y Los Rios")
        self.driver.find_element_by_id('descripcion').send_keys(
            "Mantenimiento de Centrales de Aire tipo Split.")
        self.driver.find_element_by_id("btnEnviar").click()
        mensaje_error = self.driver.find_element_by_id("ErrorMessage")
        formularioEnviado = not mensaje_error.is_displayed()
        tiempo_fin_prueba = datetime.now().second - tiempo_inicio_prueba
        if(formularioEnviado):
            print "Formulario Cotizacion.Prueba de telefono correcto EXITOSA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"
        else:
            print "Formulario Cotizacion.Prueba de telefono correcto FALLIDA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"

        self.driver.get("http://localhost:8081/cotizacion/")
        tiempo_inicio_prueba = datetime.now().second
        self.driver.find_element_by_id('nombreCliente').send_keys("Wilson")
        self.driver.find_element_by_id('apellidoCliente').send_keys("Enriquez")
        self.driver.find_element_by_id(
            'emailCliente').send_keys("wilenco@hotmail.com")
        self.driver.find_element_by_id('telCliente').send_keys("0978095645")
        self.driver.find_element_by_id('cedulaCliente').send_keys("3927219915")
        self.driver.find_element_by_id('direccionCliente').send_keys(
            "General Gomez 2012 y Los Rios")
        self.driver.find_element_by_id('descripcion').send_keys(
            "Mantenimiento de Centrales de Aire tipo Split.")
        msg_ok = self.driver.find_element_by_id("OkMessage")
        formularioNoEnviado = not msg_ok.is_displayed()
        tiempo_fin_prueba = datetime.now().second - tiempo_inicio_prueba
        if(formularioNoEnviado):
            print "Formulario Cotizacion.Prueba de telefono incorrecto EXITOSA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"
        else:
            print "Formulario Cotizacion.Prueba de telefono incorrecto FALLIDA. Tiempo transcurrido: " + str(tiempo_fin_prueba) + " segundos"

        pruebaExitosa = formularioNoEnviado and formularioEnviado
        self.assertTrue(pruebaExitosa)

    def tearDown(self):
        self.driver.quit()


class TestTypeAheadProductos(LiveServerTestCase):
    '''@Autor: Jorge Ayala
        Clase definida para realizar prueba de integracion entre la base de
        datos y el modulo de filtrado de productos.
    '''

    def setUp(self):
        self.driver = webdriver.PhantomJS()
        self.driver.implicitly_wait(15)

    def testTypeAheadProductoValido(self):
        '''
            La prueba es exitosa si al ingresar palabras clave como aire, extractor, etc
            se activa la funcion typeahead y se muestra una lista con recomendaciones
            al usuario
        '''

        self.driver.get("http://localhost:8081/productos/")
        palabrasValidas = [
            "aire",
            "extractor",
            "acondicionador",
            "ventilador",
            "central"]
        correcto = True
        for palabraValida in palabrasValidas:
            self.driver.find_element_by_class_name(
                "js-typeahead-lista_productos").send_keys(palabraValida)
            resultado = self.driver.find_element_by_class_name(
                "typeahead__result")
            correcto = correcto and resultado.is_displayed()
        if(correcto):
            print "Prueba typeaheadProductosValido EXITOSA"
        else:
            print "Prueba typeaheadProductosValido FALLIDA"

        self.assertTrue(correcto)

    def testTypeAheadProductoInvalido(self):
        '''
            La prueba es exitosa si se ingresan palabras diferentes a ["aire","extractor","acondicionador","ventilador","central"]
            y no se activa la funcion  de typeahead
        '''

        self.driver.get("http://localhost:8081/productos/")
        self.driver.find_element_by_class_name(
            "js-typeahead-lista_productos").send_keys("jifewrr")
        resultado = self.driver.find_element_by_class_name("typeahead__result")
        correcto = not resultado.is_displayed()
        if(correcto):
            print "Prueba testTypeAheadProductoInvalido EXITOSA"
        else:
            print "Prueba testTypeAheadProductoInvalido FALLIDA"

        self.assertTrue(correcto)

    def tearDown(self):
        self.driver.quit()


class TestCajaNegraProducto(LiveServerTestCase):
    """
        @Autor: Kattya Desiderio
        Clase para realizar prueba de caja negra para la entidad Producto
    """

    def test_api_producto(self):
        client = Client()
        response = client.get(
            'http://localhost:8081/api/producto/?format=json')
        self.assertEqual(response.status_code, 200)
