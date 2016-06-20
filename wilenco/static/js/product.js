/*
@Autor: Israel Fernandez

Script que carga los productos mediante una llamada ajax
*/
$(document).ready(function(){
    // array de json que contiene los productos
    var productos = [];
    $.getJSON('http://162.243.121.93/api/producto/?format=json',function(data){
        productos = data;
        for(var i = 0; i < productos.length; i++){
            var html = '<div class="col-md-3 product-model-sec">'
                    +'<div class="more-product"><span> </span></div>'
                    +'<div class="product-img b-link-stripe b-animate-go  thickbox">'
                    +'<img src="'+productos[i].imagen+'" class="img-responsive" width="102" height="102">'
                    +'<div class="b-wrapper">'
                    +'<h4 class="b-animate b-from-left  b-delay03">'
                    +'<button><span class="glyphicon glyphicon-zoom-in" ></span>Quick View</button>'
                    +'</h4></div></div>'
                    +'<div class="product-info simpleCart_shelfItem">'
                     +'<div class="product-info-cust prt_name">'
                     +'<h4>'+productos[i].nombre+'</h4>'
                     +'<input type="button" class="item_add items" value="DETALLES">'
                     +'<input type="button" class="item_add items" value="AÑADIR">'
                     +'<div class="clearfix"></div></div></div></div>';
             $('#catalogo_productos').append(html);
        }

    });

});
