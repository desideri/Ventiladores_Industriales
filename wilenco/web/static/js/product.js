/*
Product.js
@Autor: Israel Fernandez
@Version: 1.0
@Desde: 19/06/2016

Script que carga los productos en la base mediante una llamada AJAX
Almacena la informacion de los productos dentro de un ARRAY de JSONS
llamada productos.
*/
var productos = [];
var all_products = "" ;
function LoadProducto(index){
    $('.item_price').empty();
    $('p.para').empty();
    $('.prdt-info-grid').empty();
    $('#photoProducto').attr('src',productos[index].imagen);
    $('.item_price').append("<b>"+productos[index].nombre+"</b>");
    $('p.para').append(productos[index].descripcion);
    $(".prdt-info-grid").append($('<ul>').attr("class", "hul"));
    $(".hul").append("<li><b> -Categoria : </b>"+productos[index].categoria+"</li>");
    $(".hul").append("<li><b> -Capacidad : </b>"+productos[index].capacidad+"</li>");
    $(".hul").append("<li><b> -Marca : </b>"+productos[index].marca+"</li>");
}


function searchByMark(marca){
    $('.product-model-sec').empty();
    for (var i = 0; i < productos.length; i++) {
        if(productos[i].marca.includes(marca)){
            var html = '<a class="infoProducto" href="#" onclick="LoadProducto('+i+')" data-toggle="modal" data-target=".bs-example-modal-lg" data-index="'+i+'">'
            +'<div class="product-grid">'
            +'<div class="more-product"><span></span></div>'
            +'<div class="product-img b-link-stripe b-animate-go  thickbox">'
            +'<img src="'+productos[i].imagen+'" class="img-responsive" style="width:203px;height: 157px;" />'
            +'<div class="b-wrapper">'
            +'<h4 class="b-animate b-from-left  b-delay03">'
            +'<button><span class="glyphicon glyphicon-zoom-in" aria-hidden="true"></span>Ver M&aacute;s</button>'
            +'</h4></div></div></a>'
            +'<div class="product-info simpleCart_shelfItem">'
            +'<div class="product-info-cust prt_name">'
            +'<h4 class="item_name">'+productos[i].nombre+'</h4>'
            +'<h5 class="item_marca">'+productos[i].marca+'</h5>'
            +'<input type="text" class="item_quantity" value="1" />'
            +'<input type="button" class="item_add items" value="+">'
            +'<div class="clearfix"></div>'
            +'</div></div></div>';

            $('.product-model-sec').append(html);
        }
    }
}

function searchByCategory(categoria){
    $('.product-model-sec').empty();
    for (var i = 0; i < productos.length; i++) {
        if(productos[i].categoria.includes(categoria)){
            var html = '<a class="infoProducto" href="#" onclick="LoadProducto('+i+')" data-toggle="modal" data-target=".bs-example-modal-lg" data-index="'+i+'">'
            +'<div class="product-grid">'
            +'<div class="more-product"><span></span></div>'
            +'<div class="product-img b-link-stripe b-animate-go  thickbox">'
            +'<img src="'+productos[i].imagen+'" class="img-responsive" style="width:203px;height: 157px;" />'
            +'<div class="b-wrapper">'
            +'<h4 class="b-animate b-from-left  b-delay03">'
            +'<button><span class="glyphicon glyphicon-zoom-in" aria-hidden="true"></span>Ver M&aacute;s</button>'
            +'</h4></div></div></a>'
            +'<div class="product-info simpleCart_shelfItem">'
            +'<div class="product-info-cust prt_name">'
            +'<h4 class="item_name">'+productos[i].nombre+'</h4>'
            +'<h5 class="item_marca">'+productos[i].marca+'</h5>'
            +'<input type="text" class="item_quantity" value="1" />'
            +'<input type="button" class="item_add items" value="+">'
            +'<div class="clearfix"></div>'
            +'</div></div></div>';

            $('.product-model-sec').append(html);
        }
    }
}

function displayProducts(){
    $('.product-model-sec').empty();
    $('.product-model-sec').append(all_products);
    $("input[name='categoriascheck']").prop('checked',false);
    $("input[name='marcascheck']").prop('checked',false);

}

var dpr;
$(document).ready(function(){
    var nombreProductos = [];
    var p= new Object();
    // array de json que contiene los productos
    $.getJSON('http://162.243.121.93/api/producto/?format=json',function(data){
        productos = data;
        for(var i = 0; i < productos.length; i++){
            var html = '<a class="infoProducto" href="#" onclick="LoadProducto('+i+')" data-toggle="modal" data-target=".bs-example-modal-lg" data-index="'+i+'">'
            +'<div class="product-grid">'
            +'<div class="more-product"><span></span></div>'
            +'<div class="product-img b-link-stripe b-animate-go  thickbox">'
            +'<img src="'+productos[i].imagen+'" class="img-responsive" style="width:203px;height: 157px;" />'
            +'<div class="b-wrapper">'
            +'<h4 class="b-animate b-from-left  b-delay03">'
            +'<button><span class="glyphicon glyphicon-zoom-in" aria-hidden="true"></span>Ver M&aacute;s</button>'
            +'</h4></div></div></a>'
            +'<div class="product-info simpleCart_shelfItem">'
            +'<div class="product-info-cust prt_name">'
            +'<h4 class="item_name">'+productos[i].nombre+'</h4>'
            +'<h5 class="item_marca">'+productos[i].marca+'</h5>'
            +'<input type="text" class="item_quantity" value="1" />'
            +'<input type="button" class="item_add items" value="+">'
            +'<div class="clearfix"></div>'
            +'</div></div></div>';
            all_products = all_products + html;
            $('.product-model-sec').append(html);
            nombreProductos.push(productos[i].categoria + "  " + productos[i].marca + "   " + productos[i].capacidad);
            valor= productos[i].categoria + "  " + productos[i].marca + "   " + productos[i].capacidad;
            p[valor] = i;
        }

        var id=-1;
        //llamada a typeahead para el buscador
        $.typeahead({
            input: '.js-typeahead-lista_productos',
            order: "desc",
            searchOnFocus: true, // minLength: 3
            highlight:true,
            hint:true,
            source: nombreProductos,
            callback: {
                onInit: function (node) {
                    console.log('Typeahead Initiated on ' + node.selector);
                },
                onClickAfter: function (node, a, item, event) {
                    var text = $('.js-typeahead-lista_productos').val();
                    id = p[text]; // id del producto seleccionado
                    console.log(id);
                    //mostrar el modal en base al id seleccionado
                    LoadProducto(id);
                    $('.bs-example-modal-lg').modal('show');
                }
            }
        });
    });

    $('.product-model-sec').bind('DOMSubtreeModified', function(){
        /*
        El evento DOMSubtreeModified detecta si se ha modificado algun elemento
        dentro del objeto, guarda la longitud original
        */
        len = $('.product-model-sec > a').length;
        if(len < productos.length){
            $('#label_allproducts').show();
        }
        else{
            $('#label_allproducts').hide();
        }
    });

    $.getJSON('http://162.243.121.93/api/categoria/?format=json',function(data){
        dpr = data;
        categorias = $('#categorias_list');
        for (var i = 0; i < data.length ; i++) {
            var categoria = data[i].categoria;
            var item = "<label class='checkbox cat'><input type='radio' name='categoriascheck' onclick=searchByCategory('"+String(categoria.split(" ")[0])+"') ><i></i>"+categoria+"</label>";
            categorias.append(item);
        }
    });
    $.getJSON('http://162.243.121.93/get_marcas/',function(data){
        marcas = $('#marcas_list');
        for (var i = 0; i < data.marcas.length ; i++) {
            var item = "<label class='checkbox mar'><input type='radio' name='marcascheck' onclick=searchByMark('"+data.marcas[i]+"') ><i></i>"+data.marcas[i]+"</label>";
            marcas.append(item);
        }
    });

});
