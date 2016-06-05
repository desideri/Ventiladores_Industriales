$(document).ready(function () {
    SVGElement.prototype.getTransformToElement = SVGElement.prototype.getTransformToElement || function (toElement) {
        return toElement.getScreenCTM().inverse().multiply(this.getScreenCTM());
    };


    var nombreUsuario = $('#clienteID').text();
    var diagramaID = $('#dibujoID').text();
    var ideUnico = $('#ideUnico').text();
    var servicioCliente = $('#servicioCliente').text();
    var estatusConexion = 'BIENVENIDO';
    var lastModificador = $('#ultimoModificador').text();

    //alert("Es un nuevo dibujo? " + $('#nuevoDibujo').text());
    if ($('#nuevoDibujo').text() == 'No') {
        //alert('SE EJECUTA: ' + ideUnico + diagramaID);
        //graph.clear();

        $.post('http://localhost:16550/dameEntidades', { usuario: nombreUsuario, diagramaID: ideUnico, nombreDiagrama: diagramaID }, function (datos) {
            //alert('Esto me devuelve: ' + datos);
            if (datos != null) {//&& datos != '') {

                //graph.fromJSON(JSON.parse(datos));
                graph.addCell(JSON.parse(datos));
            }



        });

        $.post('http://localhost:16550/dameRelaciones', { usuario: nombreUsuario, diagramaID: ideUnico, nombreDiagrama: diagramaID }, function (datos) {
            if (datos != null) {//&& datos != '') {

                //graph.fromJSON(JSON.parse(datos));
                graph.addCells(JSON.parse(datos));
            }



        });


    }


    //alert('el id:' + ideUnico + 'y el servico es: ' + servicioCliente);
    var clientesConectados = 1;
    var enlacesMapeador = { "relación uno A uno": ["1", "1"], "relación ceroOmuchosAceroOmuchos": ["0..M", "0..M"], "relación ceroOmuchosAceroOuno": ["0..M", "0..1"], "relación ceroOmuchosAmuchos": ["0..M", "M"],
        "relación ceroOunoAmuchos": ["0..1", "M"], "relación muchosAmuchos": ["M", "M"], "relación unoAceroOmuchos": ["1", "0..M"], "relación unoAceroOuno": ["1", "0..1"],
        "relación unoAmuchos": ["1", "M"]
    };
    var contadorEntidades = 0;



    /*Se usó como guía el ejemplo del sitio web oficial de Jointjs sobre html embebido: http://jointjs.com/tutorial/html-elements*/

    joint.shapes.html = {};
    joint.shapes.html.Element = joint.shapes.basic.Rect.extend({
        defaults: joint.util.deepSupplement({
            type: 'html.Element',
            attrs: {
                rect: { stroke: 'none', 'fill-opacity': 0 }
            }
        }, joint.shapes.basic.Rect.prototype.defaults)
    });

    // Crear una vista personalizada para ese elemento que muestra un div HTML encima de ella.
    // ------------------------------------------------ -------------------------

    joint.shapes.html.ElementView = joint.dia.ElementView.extend({

        template: [
                    '<div class="html-element">',
                    '<button class="delete">x</button>',
                    '<button type="button" id = "editarNombre" class="btn btn-default btn-sm"><span class="glyphicon glyphicon-pencil"></span></button>',
                    '<strong id="nombreEntidad">Mi entidad </strong>', '<br/>',
                    '<button type="button" id = "editarPrimaryKey"  class="btn btn-default btn-sm"><span  class="glyphicon glyphicon-pencil"></span>Editar PK</button>',
                    '<table  class="table"><thead id = "primaryKey"><tr><td>PK</td><td>id</td><td>INT</td></tr></thead><tbody id ="dosAtributos" >',
                    '<tr id="At1"><td></td><td>id</td><td>INT</td><td><button type="button" id = "editAt1" class="btn btn-default btn-sm"><span class="glyphicon glyphicon-pencil"></span></button></td></tr>',
                    '<tr id="At2"><td></td><td>id</td><td>INT</td><td><button type="button" id = "editAt2" class="btn btn-default btn-sm"><span class="glyphicon glyphicon-pencil"></span></button></td></tr>',
                    '</tbody></table>',
                    '</div>'
                ].join(''),

        initialize: function () {
            _.bindAll(this, 'updateBox');
            joint.dia.ElementView.prototype.initialize.apply(this, arguments);

            this.$box = $(_.template(this.template)());

            this.$box.find('input,select,agregar,cambiarNombre,cambiarPrimaryKey,cambiarA1,cambiarA2').on('mousedown click', function (evt) { evt.stopPropagation(); });

            this.$box.find('input').on('change', _.bind(function (evt) {
                this.model.set('input', $(evt.target).val());
            }, this));
            this.$box.find('select').on('change', _.bind(function (evt) {

                this.model.set('select', $(evt.target).val());

            }, this));

            this.$box.find('button#editAt2').on('click', _.bind(function (evt) {
                var esFK = confirm("¿Es FK?");

                var nombreA1 = prompt("Nombre del atributo");

                var tipoDatos = ["VARCHAR", "CHAR", "TINYTEXT", "TEXT", "BLOB", "MEDIUMTEXT", "MEDIUMBLOB", "LONGTEXT", "LONGBLOB", "ENUM(x,y,z,etc.)", "SET", "TINYINT", "SMALLINT", "MEDIUMINT", "INT", "BIGINT", "FLOAT", "DOUBLE", "DECIMAL", "DATE", "DATETIME", "TIMESTAMP", "TIME", "YEAR"];
                var tipoDato;

                do {
                    tipoDato = prompt("Digite el tipo de dato, en mayúsculas (INT, VARCHAR,etc). Por más info: http://www.w3schools.com/sql/sql_datatypes.asp ", "INT");

                } while (tipoDatos.indexOf(tipoDato) < 0);

                var nuevaA2;

                if (esFK) {

                    nuevaA2 = "<td>FK</td><td>" + nombrePK + "</td><td>" + tipoDato + "</td><td><button type='button' id = 'editAt2' class='btn btn-default btn-sm'><span class='glyphicon glyphicon-pencil''></span></button></td>";
                }
                else {
                    nuevaA2 = "<td></td><td>" + nombrePK + '</td><td>' + tipoDato + '</td><td><button type="button" id = "editAt2" class="btn btn-default btn-sm"><span class="glyphicon glyphicon-pencil"></span></button></td>';
                }



                this.model.set('cambiarA2', nuevaA2);


            }, this));

            this.$box.find('button#editAt1').on('click', _.bind(function (evt) {
                var esFK = confirm("¿Es FK?");

                var nombreA1 = prompt("Nombre del atributo");

                var tipoDatos = ["VARCHAR", "CHAR", "TINYTEXT", "TEXT", "BLOB", "MEDIUMTEXT", "MEDIUMBLOB", "LONGTEXT", "LONGBLOB", "ENUM(x,y,z,etc.)", "SET", "TINYINT", "SMALLINT", "MEDIUMINT", "INT", "BIGINT", "FLOAT", "DOUBLE", "DECIMAL", "DATE", "DATETIME", "TIMESTAMP", "TIME", "YEAR"];
                var tipoDato;

                do {
                    tipoDato = prompt("Digite el tipo de dato, en mayúsculas (INT, VARCHAR,etc). Por más info: http://www.w3schools.com/sql/sql_datatypes.asp ", "INT");

                } while (tipoDatos.indexOf(tipoDato) < 0);

                var nuevaA1;

                if (esFK) {

                    nuevaA1 = "<td>FK</td><td>" + nombrePK + "</td><td>" + tipoDato + "</td><td><button type='button' id = 'editAt1' class='btn btn-default btn-sm'><span class='glyphicon glyphicon-pencil''></span></button></td>";
                }
                else {
                    nuevaA1 = "<td></td><td>" + nombrePK + "</td><td>" + tipoDato + "</td><td><button type='button' id = 'editAt1' class='btn btn-default btn-sm'><span class='glyphicon glyphicon-pencil''></span></button></td>";
                }

                alert(nuevaA1);

                this.model.set('cambiarA1', nuevaA1);


            }, this));

            this.$box.find('button#editarNombre').on('click', _.bind(function (evt) {
                var nuevoNombreEntidad = prompt("Nombre de la nueva entidad", "Entidad" + contadorEntidades);
                this.model.set('cambiarNombre', nuevoNombreEntidad);


            }, this));

            this.$box.find('button#editarPrimaryKey').on('click', _.bind(function (evt) {
                var nombrePK = prompt("Nombre del PK", "id");

                var tipoDatos = ["VARCHAR", "CHAR", "TINYTEXT", "TEXT", "BLOB", "MEDIUMTEXT", "MEDIUMBLOB", "LONGTEXT", "LONGBLOB", "ENUM(x,y,z,etc.)", "SET", "TINYINT", "SMALLINT", "MEDIUMINT", "INT", "BIGINT", "FLOAT", "DOUBLE", "DECIMAL", "DATE", "DATETIME", "TIMESTAMP", "TIME", "YEAR"];
                var tipoDato;

                do {
                    tipoDato = prompt("Digite el tipo de dato, en mayúsculas (INT, VARCHAR,etc). Por más info: http://www.w3schools.com/sql/sql_datatypes.asp ", "INT");

                } while (tipoDatos.indexOf(tipoDato) < 0);

                //<tbody><tr><td>PK</td><td>id</td><td>INT</td></tr></tbody>

                var nuevaPrimaryKey = "<tr><td>PK</td><td>" + nombrePK + "</td><td>" + tipoDato + "</td></tr>";

                this.model.set('cambiarPrimaryKey', nuevaPrimaryKey);


            }, this));




            this.$box.find('select').val(this.model.get('select'));

            this.$box.find('.delete').on('click', _.bind(this.model.remove, this.model));

            this.model.on('change', this.updateBox, this);

            this.model.on('remove', this.removeBox, this);


            this.updateBox();



        },
        render: function () {
            joint.dia.ElementView.prototype.render.apply(this, arguments);
            this.paper.$el.prepend(this.$box);
            this.updateBox();

            return this;
        },
        updateBox: function () {

            var bbox = this.model.getBBox();


            this.$box.find('strong#nombreEntidad').text(this.model.get('cambiarNombre'));
            this.$box.find('#primaryKey').html(this.model.get('cambiarPrimaryKey'));
            this.$box.find('tr#At1').html(this.model.get('cambiarA1'));
            this.$box.find('tr#At2').html(this.model.get('cambiarA2'));
            this.$box.css({ width: bbox.width, height: bbox.height, left: bbox.x, top: bbox.y, transform: 'rotate(' + (this.model.get('angle') || 0) + 'deg)' });

        },
        removeBox: function (evt) {
            this.$box.remove();


        }

    });
    //





    var graph = new joint.dia.Graph;

    var paper = new joint.dia.Paper({
        el: $('#Zona_de_dibujo'),
        width: 10000,
        height: 10000,
        model: graph,
        gridSize: 1
    });




    $("#Abrir").hide();

    $(".img-responsive").draggable({ appendTo: 'body', containment: '#Zona_de_dibujo', scroll: true, helper: 'clone' });


    $("#Zona_de_dibujo").droppable({ drop: crearElementoEnZonaDibujo });

    $("a#abrirArchivo").click(function () {
        $("#Abrir").show();
    });

    function generarRelacion(tipoRelacion, offsetX, offsetY) {
        var relacion = enlacesMapeador[tipoRelacion];
        var elemento = new joint.dia.Link({
            source: { x: offsetX - 100, y: offsetY },
            target: { x: offsetX + 100, y: offsetY },
            attrs: {
                '.marker-source': { fill: '#4b4a67', stroke: '#4b4a67', d: 'M 10 0 L 0 5 L 10 10 z' },
                '.marker-target': { fill: '#4b4a67', stroke: '#4b4a67', d: 'M 10 0 L 0 5 L 10 10 z' }
            },
            labels: [{ position: 45, attrs: { text: { text: relacion[0], fill: '#f6f6f6', 'font-family': 'sans-serif', 'font-size': '150%' }, rect: { stroke: '#7c68fc', 'stroke-width': 20, rx: 5, ry: 5}} },
                                                    { position: -45, attrs: { text: { text: relacion[1], fill: '#f6f6f6', 'font-family': 'sans-serif', 'font-size': '150%' }, rect: { stroke: '#7c68fc', 'stroke-width': 20, rx: 5, ry: 5}} }
                                                                ]
        });
        return elemento;
    }

    function crearElementoEnZonaDibujo(event, ui) {
        var offsetXPos = parseInt(ui.offset.left) - 400; //El 400 se originó usando prueba y error 
        var offsetYPos = parseInt(ui.offset.top) - 250; //El 250 se originó usando prueba y error
        var arrastrable = ui.draggable;
        var elemento;
        if (arrastrable.attr('alt') == "relación entidadConKey") {


            elemento = new joint.shapes.html.Element({ position: { x: offsetXPos, y: offsetYPos }, size: { width: 220, height: 200} });
            contadorEntidades = contadorEntidades + 1;

        }
        else {
            elemento = generarRelacion(arrastrable.attr('alt'), offsetXPos, offsetYPos);

        }
        graph.addCell(elemento);


    }


    $("a#guardarArchivo").click(function () {
        var textFile = null,
                                  makeTextFile = function (text) {
                                      var data = new Blob([text], { type: 'text/plain' });

                                      // Si estamos reemplazando un archivo generado previamente tenemos que
                                      // Revocar manualmente la URL objeto de evitar pérdidas de memoria.
                                      if (textFile !== null) {
                                          window.URL.revokeObjectURL(textFile);
                                      }

                                      textFile = window.URL.createObjectURL(data);

                                      return textFile;
                                  };
        this.href = makeTextFile(JSON.stringify(graph));


    });



    var subirArchivo = document.querySelector('#Abrir');
    subirArchivo.addEventListener('change', function () {
        var fileSelected = this.files[0];
        abrirArchivo(fileSelected);
    }, false);



    function abrirArchivo(file) {
        var reader = new FileReader();
        reader.onload = function () {
            graph.clear();
            graph.fromJSON(JSON.parse(reader.result));
            $("#Abrir").hide();
        };
        reader.readAsText(file);

    }

    var clientesConectados = [];

    //var socket = io.connect('http://localhost:16550', { resource: '/socket.io' });
    var socket = io();

    function hacerLogin(nombre, ideUnico) {

        socket.emit('editandoDiagrama', nombre, ideUnico);
    }

    hacerLogin(nombreUsuario, ideUnico);

    socket.on('alguienModifico', function (ideUnicoDiagrama, nombreDibujo, ultimoModificador, diagrama) {
        if (ideUnico == ideUnicoDiagrama) {
            graph.clear();
            graph.fromJSON(JSON.parse(diagrama));
            diagramaID = nombreDibujo;
            lastModificador = ultimoModificador;
            $('#nombreDiagrama.estado.alert.alert-success').html(nombreDibujo);
            $("#ultimaModificacion.estado.alert.alert-success").html(ultimoModificador);
        }
    });

    

    $("input#compartir").keyup(
        function () {
            var valor = $("input#compartir").val();
            var servicioComp = $("#servicioCompartir option:selected" ).text();
            if (valor == nombreUsuario && servicioComp == servicioCliente) {
                $("#mensajeAJAXcompartir").text("ES USTED!");
            }
            else {
                $.post('http://localhost:16550/usuarioExiste', { nombre: valor, servicio: servicioComp }, function (datos) {
                    if (datos == "EXISTE") {
                        $("#mensajeAJAXcompartir").text("EXISTE ESE USUARIO");
                        $("#zonaCompartir").html('<button type = "button" id = "botonCompartir">COMPARTIR</button>');
                    }
                    else {
                        $("#mensajeAJAXcompartir").text("NO EXISTE ESE USUARIO");
                        $("#zonaCompartir").html('');
                    }

                    $("#botonCompartir").click(function () {
                        var fecha = (new Date()).getDate() + "-" + ((new Date()).getMonth() + 1) + "-" + (new Date()).getFullYear();

                        $.post('http://localhost:16550/compartirDiagrama', { usuario: $("input#compartir").val(), quienComparte: nombreUsuario, identificadorUnico: ideUnico, nombreDiagrama: diagramaID, servicio: $("#servicioCompartir option:selected" ).text(), fecha: fecha });
                    });


                });
            }



        }
    );






    function actualizarDiagrama() {
        var message = {
            ultimoModificador: nombreUsuario,
            nombreDibujo: diagramaID,
            diagrama: JSON.stringify(graph),
            ideUnicoDiagrama: ideUnico,
            servicio: servicioCliente
        };

        var nombreDibujo = diagramaID;
        //var nombreDibujo = $('#nombreDiagrama.estado.alert.alert-success').text();
        $("#ultimaModificacion.estado.alert.alert-success").html(nombreUsuario);

        var fecha = (new Date()).getDate() + "-" + ((new Date()).getMonth() + 1) + "-" + (new Date()).getFullYear();




        ///

        var elementos = graph.toJSON().cells;
        //alert('SE DA: ' + elementos);
        //console.log('Elementos: ' + typeof(JSON.parse(dibujo)));
        var entidades;
        var relaciones;



        //entidades = { "cells": entidades };
        //relaciones = {"cells": relaciones};
        entidades = JSON.stringify(graph.getElements());
        relaciones = JSON.stringify(graph.getLinks());


        $.post('http://localhost:16550/actualizarDiagrama', { identificadorUnico: ideUnico, nombreDiagrama: nombreDibujo, ultimoModificador: nombreUsuario, fechaUltimaModificacion: fecha, diagramaEntidad: entidades, diagramaRelacion: relaciones });

        socket.emit('envioMiDiagrama', message);

        //return false;
    }

    $("#btnGuardar.btn.btn-primary").click(actualizarDiagrama);

    $("#botonCambiarNombre.btn.btn-primary").click(function () {

        var nuevoNombre = prompt("Ingresa su nuevo nombre", "diagrama");
        $('#nombreDiagrama.estado.alert.alert-success').html(nuevoNombre);
        diagramaID = nuevoNombre;
    }
    );

});


