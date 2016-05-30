$(document).ready(function(){
    $("a.show").click(function(){
        div = $(this).attr('href');
        $('.current').hide("blind");
        $(div).show("blind");
    });
});
