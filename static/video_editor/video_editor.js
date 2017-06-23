
$(document).ready(function () {
    var opcion = 1;

    $('#carga_youtube').hide();

    $('.ui.checkbox').checkbox();

    $('#local').click(function () {
        opcion = 1;
        $('#input_yt').val('');
        $('#carga_youtube').hide('slow');
        $('#carga_local').show('slow');

    });

    $('#yt').click(function () {
        opcion=2;

        $('#input_local').val('');
        $('#carga_local').hide('slow');
        $('#carga_youtube').show('slow');
    });

    $('#btOk').on('click',function () {

        if(opcion==1 && $('#input_local').val()!=''){
            $('#carga_local').addClass('loading');
            upload(document.getElementById('input_local'), $('#input_local').attr('href'));
        }

        if(opcion==2 && $('#input_yt').val()!=''){
            $('#carga_youtube').addClass('loading');
            descargarYT($('#input_yt').attr('href'),$('#input_yt').val());
        }

    });

    function upload(field, upload_url) {
        if (field.files.length == 0) {
            return;
        }
        file = field.files[0];
        var formdata = new FormData();
        formdata.append('file_upload', file);
        $.ajax({
            url: upload_url,
            type: 'POST',
            data: formdata,
            processData: false,
            contentType: false,
            success: function (json) {
                console.log(json);
                if (json.result == 'ok') {

                    $('#video_carga').attr('src', "/"+json.url);
                    $('.carga').hide();
                    $('#video_segment').hide().removeClass('hidden').show();
                }else {
                    if(json.msg == 'ext'){
                        $('.ui .message').removeClass('hidden');
                    }
                }
            },
            error: function (xhr, errmsg, err) {
                console.log(xhr.status + ": " + xhr.responseText);
            }
        });
    }

    function descargarYT(url,urlyt) {
        $.ajax({
            url: url,
            type: "POST",
            data: {urlyt: urlyt},

            success: function (json) {
                console.log(json);
                $('#carga_youtube').removeClass('loading');

                if (json.result == 'ok') {

                    $('#video_carga').attr('src', "/"+json.url);
                    $('.carga').hide();
                    $('#video_segment').hide().removeClass('hidden').show();
                }
            },
            error: function (xhr, errmsg, err) {
                $('#carga_youtube').removeClass('loading');
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    }

});