
$(document).ready(function () {
    var mostrar=0;
    var tabs = [];

    $('#trans').click(function () {
        if(mostrar==0) {
            $('#transcription').hide().appendTo($('#media_content')).show('slow');
            mostrar=1;
        }else {
            $('#transcription').hide('slow');
           mostrar=0;
        }
    });

    $("#accordion").on("shown.bs.collapse", function () {
        var myEl = $(this).find('.collapse.in');

        $('html, body').animate({
            scrollTop: $(myEl).offset().top
        }, 500);
    });

    $("#units").click(function () {
        $(this).addClass("active");
        $(this).siblings().removeClass("active");
    });
    $("#units").addClass("active");



    $('.ejercicio').each(function () {
        tabs.push($(this).attr('id'));
    });


    $('.menu .item').tab();

    var tabe = '#' + tabs[0];

    var tabseg = '#' + tabs[0]+'seg';
    $(tabe).addClass('active');
    $(tabseg).addClass('active');

    var num = 1;
    $('.item').each(function () {
        $(this).prepend(num +'&nbsp; ');
        num++;
    });

    $('.reload').click(function () {
        var iframe = $(this).parent().parent().find('iframe');
        console.log('frame: '+iframe.html());
        iframe.attr('src',iframe.attr('src'));
    })

});
