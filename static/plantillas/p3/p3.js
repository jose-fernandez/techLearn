
$(document).ready(function () {
    var errors = [];//array de elementos draggables erroneos
    var oks = [];// ""                "" correctos
    var droppeds=0;//elemntos draggables colocados en un hueco.
    var num_rec = $('.drop').length;

    //---------------------desordenar elementos draggables-------------------//
    $(function () {
        $("#inicio").randomize("div.draggable");

    });

    (function ($) {

        $.fn.randomize = function (childElem) {
            return this.each(function () {
                var $this = $(this);
                var elems = $this.children(childElem);

                elems.sort(function () {
                    return (Math.round(Math.random()) - 0.5);
                });

                $this.remove(childElem);

                for (var i = 0; i < elems.length; i++)
                    $this.append(elems[i]);

            });
        }
    })(jQuery);
    //-------------------------------------------------------------------------//


    //-----------------------------desordeanr elemntos de los select----------//
    $('.select').each(function () {
        var i =Math.floor((Math.random() * 3) + 1);

        var option = $(this).find('option[value=1]');
        var option2 = $(this).find('option[value='+i+']');

        console.log("opcion"+option.html());
        $( option ).insertAfter( option2);
    });
    //-----------------------------------------------------------------------//


    $('.hint').click(function () {
        var id = $(this).attr("id");
        var dia = '#dialog' + id + '_n1';
        console.log("dialogando");
        $(dia).dialog({
            autoOpen: true,
            modal: false,
            width: 400,
            top: 50,
            left: 100,
            height: 300,
            show: {
                effect: "fade",
                duration: 100
            },
            hide: {
                effect: "fade",
                duration: 100
            }
        });
    });

    $('#corregir_btn').click(function () {

        var fill_correctos = 0;
        var fills = 0;
        var option_correctos = 0;
        var options = 0;
        var id_error = [];

        $('.fill').each(function () {
            fills += 1;
            var resp = $(this).parent().parent().find($('.resp')).attr('value').toLowerCase();
            var te = $(this).val().toLowerCase();

            if (resp != te) {
                $(this).parent().addClass('error');
                id_error.push($(this).attr('id'));
            } else {
                fill_correctos += 1;
                $(this).parent().addClass('disabled');
            }
        });

        $("select option:selected").each(function () {
            options += 1;

            if ($(this).hasClass('correcta')) {
                $(this).parent().parent().addClass('disabled');
                option_correctos += 1;
            } else {
                $(this).parent().parent().addClass('error');
                id_error.push($(this).parent().attr('id'));
            }
        });

        for (i = 0; i < errors.length; i++) {
            var ob = errors[i];
            $(".drop").droppable('enable');
            $('#inicio').append(ob);

            ob.animate({left: 0, top: 0}).css("border", "3px solid red");
            id_error.push(errors[i].attr("id") );
        }

        for (i = 0; i < oks.length; i++) {
            var obc = oks[i];
            obc.addClass("green");
            obc.draggable('disable');
        }

        console.log('fill: ' + fills + ', fillcor: ' + fill_correctos);

        if (fills == fill_correctos && options == option_correctos && oks.length == num_rec) {
            contar_aciertos()
        } else {
            for (i = 0; i < id_error.length; i++) {
                var did = '.pista2_' + id_error[i];
                $(did).css('display', 'inline');
            }
            $('.dialog_n2').dialog({
                autoOpen: true,
                modal: true,
                resizable: true,
                width: 400,
                height: 400,
                draggable: false,
                close: function () {
                    for (i = 0; i < id_error.length; i++) {
                        var did = '.pista2_' + id_error[i];
                        $(did).css('display', 'none');
                    }
                },
                show: {
                    effect: "fade",
                    duration: 100
                },
                hide: {
                    effect: "fade",
                    duration: 100
                }
            });
        }
    });

    function contar_aciertos() {
        call_finished();
        $('#dialogV').dialog({
            autoOpen: true,
            modal: true,
            resizable: false,
            draggable: false,
            show: {
                effect: "scale",
                duration: 500
            },
            open: function (event, ui) {
                $(".ui-dialog-titlebar-close", ui.dialog | ui).hide();
            },
            hide: {
                effect: "fade",
                duration: 100
            }
        });
    }

    //funcion para pasar al siguiente ejercicio cuando esta en la secuencia
    function call_finished() {
        var boton = window.parent.$('#bot');
        boton.trigger('click');
    }

    $(".drag").draggable({
        revert: "invalid"
        ,
        stack: ".contenedor",
        start: function (event, ui) {

            if ($(this).data('droppedin')) {
                $(this).data('droppedin').droppable('enable');
                $(this).data('droppedin', null);
            }

        }
    });

    $('#inicio').droppable({
        accept: ".drag",
        drop:function (event, ui) {
            $(this).append($(ui.draggable).css({left: 0, top: 0}));
            for (i = 0; i < oks.length; i++) {
                if (oks[i].attr("id") == $(ui.draggable).attr("id")) {
                    oks.splice(i, 1);
                }
            }

            for (i = 0; i < errors.length; i++) {
                if (errors[i].attr("id") == $(ui.draggable).attr("id")) {
                    errors.splice(i, 1);

                }
            }
        }
    });




    $(".drop").droppable({
        accept: ".drag",
        drop: function (event, ui) {
            $(this).append($(ui.draggable).css({left: 0, top: 0}));
            droppeds++;
            if ($(this).attr("id") != "inicio") {
                $(this).css("width", $(ui.draggable).width()+28);
            }
            if (droppeds==num_rec) {

            }
            var drop_p = $(this).offset();
            var drag_p = ui.draggable.offset();
            var left_end = drop_p.left - drag_p.left + 1;
            var top_end = drop_p.top - drag_p.top + 1;
            ui.draggable.animate({
                top: '+=' + top_end,
                left: '+=' + left_end
            });

            ui.draggable.data('droppedin', $(this));
            $(this).droppable('disable');

            for (i = 0; i < oks.length; i++) {
                if (oks[i].attr("id") == $(ui.draggable).attr("id")) {
                    oks.splice(i, 1);
                }
            }

            for (i = 0; i < errors.length; i++) {
                if (errors[i].attr("id") == $(ui.draggable).attr("id")) {
                    errors.splice(i, 1);

                }
            }

            if ($(this).attr("id") != "inicio") {

                if (($(ui.draggable).attr("id")) == ($(this).attr("id"))) {
                    oks.push($(ui.draggable));
                } else {
                    errors.push($(ui.draggable));
                }
            }
            console.log("errores: "+errors.toString())
        }
    }).draggable();

});