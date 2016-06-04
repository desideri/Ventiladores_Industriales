$(document).ready(function(){
    $("a.show").click(function(){
        div = $(this).attr('data');
        id_current = $('.current').attr('id');
        $('#'+id_current).removeClass('current');
        $('#'+id_current).addClass('inactive');
        $(div).removeClass('inactive');
        $(div).addClass('current');
        $('#'+id_current).hide('slow');
        $(div).show('slow');
    });
});
