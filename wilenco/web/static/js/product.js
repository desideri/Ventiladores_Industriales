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
function LoadProducto(index){
    $('.item_price').empty();
    $('p.para').empty();
    $('#photoProducto').attr('src',productos[index].imagen);
    $('.item_price').append(productos[index].nombre);
    $('p.para').append(productos[index].descripcion);
    $(".prdt-info-grid ul").append("<li>- Categoria : "+productos[index].categoria+"</li>");
    $(".prdt-info-grid ul").append("<li>- Marca : "+productos[index].marca+"</li>");
    $(".prdt-info-grid ul").append("<li>- Capacidad : "+productos[index].capacidad+"</li>");
}
$(document).ready(function(){
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
                    +'<h4>'+productos[i].nombre+'</h4>'
                    +'<input type="text" class="item_quantity" value="1" />'
                    +'<input type="button" class="item_add items" value="ADD">'
                    +'<div class="clearfix"></div>'
                    +'</div></div></div>';
             $('.product-model-sec').append(html);
        }

    });


});
