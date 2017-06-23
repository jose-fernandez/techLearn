
$(document).ready(function () {
    var cur_progress = 0;
    var aumento = 100 / $('.ejercicio').length;
    var tabs = [];



    $('.ejercicio').each(function () {
        tabs.push($(this).attr('id'));
    });

    function esconderVideo(val) {
        if (val == 1) {
            $('#mediaContent').hide('slow');
            $("#ejer").removeAttr('class');
            $('#ejer').attr('class', ' sixteen wide column');
        } else {
            $('#mediaContent').show('slow');
            $("#ejer").removeAttr('class');
            $('#ejer').attr('class', ' eleven wide column');
        }
    }

    $('#prog').progress({
        percent: 0
    });

    var num = 1;
    $('.item').each(function () {
        $(this).text(num);
        num++;
    });

    $('.menu .item').tab({
        onVisible: function () {

            var val = $(this).find('iframe').contents().find('#sinVideo').attr('value');
            esconderVideo(val);
        }
    })
    ;
    var tab = 'div#' + tabs[0];
    $(tab).addClass('active');

    var tabe = '#' + tabs[0] + '.item';
    $(tabe).addClass('active');

    $('.ui.accordion')
        .accordion()
    ;

    $('#bot').click(function () {

        cur_progress += aumento;
        $('#prog').progress({
            percent: cur_progress
        });

        console.log('progreso: '+cur_progress);
        if (cur_progress >= 100) {
            $('.ui.basic.modal')
                .modal('show')
                .modal('setting', 'closable', false)
                .modal({
                    blurring: true
                })
            ;
        } else {
            nextTab();
        }

    });

    function nextTab() {
        var id_tab = $('.item.active').attr('data-tab');
        $('.item.active').removeClass('active');
        for (i = 0; i < tabs.length; i++) {
            if (tabs[i] == id_tab && i+1!=tabs.length) {
                $.tab('change tab', tabs[i + 1]);
                $('#' + tabs[i + 1]).addClass('active');

                var val = $('.ejercicio.active').find('iframe').contents().find('#sinVideo').attr('value');
                esconderVideo(val)
            }
        }
    }



});
