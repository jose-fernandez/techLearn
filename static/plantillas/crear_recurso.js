
$(document).ready(function () {
    var divs = {};
    $(document).on('click', '.opcion', function () {
        divClone = $(this).parent().parent().clone();
        divs[$(this).parent().parent().attr('id')] = divClone;


        $(this).find('.titu').html('');
        $(this).find('img').attr('src', '');
        $(this).find('.form-group').css("display", "inline");
        $(this).removeClass("button").removeClass("s6").removeClass("opcion", "");
        if ($(this).hasClass("opcion1")) {
            $(this).parent().parent().find('.opcion2').css("display", "none");
        } else {
            $(this).parent().parent().find('.opcion1').css("display", "none");
        }
    });

    $(document).on('click', '.reset', function () {
        var div = divs[$(this).parent().parent().parent().parent().attr('id')];
        $(this).parent().parent().parent().parent().replaceWith(div);
    });

    //--------------------------CrearrecursoP2------------------//
    var divclone;

    $('#respBtn').click(function () {
        divclone = $('#dialogResp').clone();
        $('.ui.modal').modal('show').modal('setting', 'closable', false).modal('refresh');
    });

    $(document).on('click', '#canceld', function () {
        $('.ui.modal').modal('hide');
        $('#dialogResp').replaceWith(divclone);
    });

    $(document).on('click', '#guardarResp', function () {
        post_resp();
        $(this).addClass('loading');

    });


    function post_resp() {

        console.log("create post is working!");// sanity check
        var idr = document.getElementById('idr');
        var texto = document.getElementById('texto_resp');
        var media = document.getElementById('media_resp');
        var input1 = document.getElementById('texto_n1_resp');
        var input2 = document.getElementById('texto_n2_resp');
        var media1 = document.getElementById('media_n1_resp');
        var media2 = document.getElementById('media_n2_resp');

        var datos= new FormData();

        if (texto.value != '') {
            datos.append('texto', texto.value);
        }

        if (media.files.length != 0) {
            var file0 = media.files[0];
            datos.append('media', file0);
        }

        if (input1.value != '') {
            datos.append('hint1', input1.value);
        }

        if (input2.value != '') {
            datos.append('hint2', input2.value);
        }

        if (media1.files.length != 0) {
            var file = media1.files[0];
            datos.append('media1', file);
        }

        if (media2.files.length != 0) {
            var file2 = media2.files[0];
            datos.append('media2', file2);
        }
        datos.append('idr', $('#idr').attr('value'));

        $.ajax({
            url: $('#guardarResp').attr('href'), // the endpoint
            type: "POST", // http method
            data: datos, // data sent with the post request
            processData: false,
            contentType: false,
            // handle a successful response
            success: function (json) {
                $('#canceld').trigger('click');
                console.log(json);
                console.log("success");
                $('#guardarResp').removeClass('loading');
                $('#respuestas_panel').append('<div class="ui segment">'+json.texto+'</div>')
            },

            error: function (xhr, errmsg, err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " + errmsg +
                    " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    }

});