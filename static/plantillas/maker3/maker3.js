$(document).ready(function () {
    var recs = [];
    recs.push($('#id_ej').attr('value'));
    console.log('cargado');
    // $('.ui.basic.modal')
    //             .modal('show')
    //             .modal('setting', 'duration', 1)
    //             .modal('setting', 'closable', false)
    //             .modal({
    //                 blurring: true
    //             });


    $('.menu .item').tab();


    $('#selectpos').on('change',function () {
        post_posicion();
        console.log("cambiadoito");
    });

    function post_posicion() {

        var datos = new FormData();

        var e = document.getElementById("selectpos");
        var pos = e.options[e.selectedIndex].value;
        if(pos==0){
            datos.append('pos',parseInt($('select option:last').val())+1);
        }else{
            datos.append('pos',pos);
        }


        datos.append('ejercicio',$('#ejId').attr('value'));
        datos.append('proyecto',$('#proyId').attr('value'));

        $.ajax({
            url: $('#selectpos').attr('href'),
            type: "POST",
            data: datos,
            processData: false,
            contentType: false,

            // handle a successful response
            success: function (json) {
                if(json.result=='ok')
                    console.log('checkecd ok');
            },
            // handle a non-successful response
            error: function (xhr, errmsg, err) {
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    }


    $('#form_texto').on('submit', function (event) {
        event.preventDefault();
        console.log("form submitted!");  // sanity check
        if (!$('#texto').val()) {
            $('.field.texto').addClass('error');
        } else {
            $('.field.texto').removeClass('error');
            post_texto();
        }
    });


    function post_texto() {
        console.log("create post is working!");// sanity check
        $.ajax({
            url: $('#form_texto').attr('action'), // the endpoint
            type: "POST", // http method
            data: {texto: $('#texto').val()}, // data sent with the post request

            // handle a successful response
            success: function (json) {
                $('#texto').val(''); // remove the value from the input
                console.log(json); // log the returned json to the console
                console.log("success"); // another sanity check
                $('.contenedor').append('<div class="ui large label"> <p>' + json.texto + '</p></div>');
                recs.push(json.key);
                console.log('recs: ' + recs.toString());
            },
            // handle a non-successful response
            error: function (xhr, errmsg, err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " + errmsg +
                    " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    }


    $('#form_fill').on('submit', function (event) {
        event.preventDefault();
        console.log("form submitted!");  // sanity check
        if (!$('#fill').val()) {
            $('.field.fill').addClass('error');
        } else {
            $('.field.fill').removeClass('error');
            post_fill();
        }
    });


    function post_fill() {
        console.log("create post is working!");// sanity check
        var input1 = document.getElementById('id_texto_f1');
        var input2 = document.getElementById('id_texto_f2');
        var media1 = document.getElementById('id_media_f1');
        var media2 = document.getElementById('id_media_f2');

        var datos = new FormData();
        datos.append('texto', $('#fill').val());

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

        $.ajax({
            url: $('#form_fill').attr('action'), // the endpoint
            type: "POST", // http method
            data: datos, // data sent with the post request
            processData: false,
            contentType: false,
            // handle a successful response
            success: function (json) {
                $('#fill').val('');
                $('.form-group').css("display", "none");
                $('.opcion1').css("display", "inline");
                $('.opcion2').css("display", "inline");
                $('.ui.primary.s6').addClass('button').addClass('opcion');
                input1.value = '';
                input2.value = '';
                media1.value = '';
                media2.value = '';
                console.log(json);
                console.log("success");
                $('.contenedor').append('<div class="ui large label"><div class="ui form"> <div class="field"><input type="text" name="texto" id="texto" placeholder="' + json.texto + '"></div></div></div>');
                recs.push(json.key);
                console.log('recs: ' + recs.toString());
            },

            error: function (xhr, errmsg, err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " + errmsg +
                    " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    }


    $('#form_options').on('submit', function (event) {
        event.preventDefault();
        console.log("form submitted!");  // sanity check
        if (!$('#option1').val()) {
            $('.field.option1').addClass('error');
        } else {
            $('.field.option1').removeClass('error');
            if (!$('#option2').val()) {
                $('.field.option2').addClass('error');
            } else {
                $('.field.option2').removeClass('error');
                if (!$('#option3').val()) {
                    $('.field.option3').addClass('error');
                } else {
                    $('.field.option3').removeClass('error');
                    post_options();
                }
            }
        }
    });


    function post_options() {
        console.log("create post is working!");// sanity check
        var input1 = document.getElementById('id_texto_f1_op');
        var input2 = document.getElementById('id_texto_f2_op');
        var media1 = document.getElementById('id_media_f1_op');
        var media2 = document.getElementById('id_media_f2_op');

        var datos = new FormData();
        datos.append('texto', $('#option1').val());

        datos.append('opcion2', $('#option2').val());
        datos.append('opcion3', $('#option3').val());

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

        $.ajax({
            url: $('#form_options').attr('action'), // the endpoint
            type: "POST", // http method
            data: datos, // data sent with the post request
            processData: false,
            contentType: false,
            // handle a successful response
            success: function (json) {
                $('#option1').val('');
                $('#option2').val('');
                $('#option3').val('');
                $('.form-group').css("display", "none");
                $('.opcion1').css("display", "inline");
                $('.opcion2').css("display", "inline");
                $('.ui.primary.s6').addClass('button').addClass('opcion');
                input1.value = '';
                input2.value = '';
                media1.value = '';
                media2.value = '';
                console.log(json);
                console.log("success");
                $('.contenedor').append(
                    '<div class="ui large label"><div class="ui form"> <div class="field"> <select> <option value="">'+json.texto+'</option> <option value="1">'+json.op2+'</option> <option value="0">'+json.op3+'</option> </select> </div></div></div>');
                recs.push(json.key);
                console.log('recs: ' + recs.toString());
            },

            error: function (xhr, errmsg, err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " + errmsg +
                    " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    }

    $('#form_drag').on('submit', function (event) {
        event.preventDefault();
        console.log("form submitted!");  // sanity check
        if (!$('#drag').val()) {
            $('.field.drag').addClass('error');
        } else {
            $('.field.drag').removeClass('error');
            post_drag();
        }
    });


    function post_drag() {
        console.log("create post is working!");// sanity check
        var input1 = document.getElementById('id_texto_f1_drag');
        var input2 = document.getElementById('id_texto_f2_drag');
        var media1 = document.getElementById('id_media_f1_drag');
        var media2 = document.getElementById('id_media_f2_drag');

        var datos = new FormData();
        datos.append('texto', $('#drag').val());

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

        $.ajax({
            url: $('#form_drag').attr('action'), // the endpoint
            type: "POST", // http method
            data: datos, // data sent with the post request
            processData: false,
            contentType: false,
            // handle a successful response
            success: function (json) {
                $('#drag').val('');
                $('.form-group').css("display", "none");
                $('.opcion1').css("display", "inline");
                $('.opcion2').css("display", "inline");
                $('.ui.primary.s6').addClass('button').addClass('opcion');
                input1.value = '';
                input2.value = '';
                media1.value = '';
                media2.value = '';
                console.log(json);
                console.log("success");
                $('.contenedor').append('<div class="ui large raised label violet"> <p>' + json.texto + '</p></div>');
                recs.push(json.key);
                console.log('recs: ' + recs.toString());
            },

            error: function (xhr, errmsg, err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " + errmsg +
                    " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    }


    $('#form_file').on('submit', function (event) {
        event.preventDefault();
        console.log("form submitted!");  // sanity check
        console.log("create post is working!");// sanity check
        upload(document.getElementById('audio'), $('#form_file').attr('action'));
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
                document.getElementById("audio").value = "";
                console.log(json); // log the returned json to the console
                console.log("success"); // another sanity check
                if (json.ext == 'mp3' || json.ext == 'wav') {
                    $('.contenedor').append('<div class="ui label"><audio controls><source src="/' + json.url + '" type="audio/' + json.ext + '"></audio></div>');
                    recs.push(json.key);
                    console.log('recs: ' + recs.toString());
                } else {
                    $('#results').append('<div class="ui warning message"> <i class="close icon"></i> <div class="header">File not valid</div>Make sure the file is .wav or .mp3 </div>')
                    $('.message .close').on('click', function () {
                        $(this).closest('.message').transition('fade');
                    });
                }
            },
            error: function (xhr, errmsg, err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " + errmsg +
                    "<a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    }

    var divs={};
    $(document).on('click','.opcion',function () {
        divClone = $(this).parent().parent().clone();
        divs[$(this).parent().parent().attr('id')] = divClone;

        $(this).find('.form-group').css("display", "inline");
        $(this).removeClass("button").removeClass("opcion", "");
        if ($(this).hasClass("opcion1")) {
            $(this).parent().parent().find('.opcion2').css("display", "none");
        } else {
            $(this).parent().parent().find('.opcion1').css("display", "none");
        }
    });

    $(document).on('click','.reset',function () {
       var div=divs[$(this).parent().parent().parent().parent().attr('id')];
        $(this).parent().parent().parent().parent().replaceWith(div);
    });


    $('.back').click(function () {
        parent.history.back();
        return false;
    });


    $('#add_media').click(function () {
        var div = document.createElement('div');
        div.innerHTML = "<p><input type='file'></p>";
        $('.contenedor').append(div);
    });


    $('#add_text').click(function () {
        var div = document.createElement('div');
        div.innerHTML = "<p><span contenteditable='true'>Escribe aqui</span></p>";
        $('.contenedor').append(div);
    });


    $('#del_last').click(function () {
        $('.contenedor div').last().remove()
    });


    $('.button.teal').click(function () {
        if (recs.length >= 2) {
            post_posicion();
            $('#save').parent().css('display', 'inline');
        } else {
            console.log(recs.length);
        }
    });

    $('#masrec').click(function () {
        $('#recursos_panel').prepend("<div class=\"six wide segment ui\"><div id=\"panel\" class=\"ui grid contenedor\"> <div class=\"row\" style=\"display: none\"><input id=\"key_rec\" type=\"hidden\" value=\"\"><button class=\"ui green button\" id=\"save\" ><i class=\"save icon\"></i></button><button href=\""+$('#urlDel').val()+"\" id=\"borrar_rec\" style=\"display: none\" class=\"ui button red\"><i class=\"fa fa-times\"></i> </button></div> </div></div>")
        $(this).addClass('disabled');
    });

    $(document).on('click', '#save', function () {
        $(this).addClass('loading');
        $(this).parent().find('#borrar_rec').css('display','inline');
        console.log("saving is working!");// sanity check
        console.log('Stringifying' + JSON.stringify({array: recs}));
        $.ajax({
            url: $('#url_guardar').attr('href'), // the endpoint
            type: "POST", // http method
            data: JSON.stringify({array: recs}), // data sent with the post request

            // handle a successful response
            success: function (json) {
                $('.contenedor').removeClass('contenedor');
                $('#save').empty().removeClass('loading').addClass('disabled').append('<i class="fa fa-check"></i>').removeAttr('id');
                recs = [];
                recs.push($('#id_ej').attr('value'));
                $('#masrec').removeClass('disabled');
                $('#key_rec').val(json.key);
                console.log('recurso: ' + json.key);
                console.log('recs: ' + recs.toString());
                $('#save_bt').removeClass('disabled');
                $('#masrec').trigger('click');
            },
            // handle a non-successful response
            error: function (xhr, errmsg, err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " + errmsg +
                    "<a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    });

    $(document).on('click', '#borrar_rec', function () {
        var formdata = new FormData();
        var id_rec=$(this).parent().find('#key_rec').val();
        formdata.append('recurso', id_rec);
        formdata.append('ejercicio', $('#ejId').val());
        $.ajax({
            url: $('#borrar_rec').attr('href'), // the endpoint
            type: "POST", // http method
            data: formdata, // data sent with the post request
            processData: false,
            contentType: false,

            // handle a successful response
            success: function (json) {
                var selector = 'input[value="'+id_rec+'"]';
                $(selector).parent().parent().parent().remove();
            },
            // handle a non-successful response
            error: function (xhr, errmsg, err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " + errmsg +
                    "<a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    });

    if($('.borrar2').length>0){
        $('#save_bt').removeClass('disabled');
    }

    $('.ui.checkbox')
        .checkbox()
    ;

    $('#checkVideo').change(function () {
        if ($(this).is(':checked')) {
            checked = 1;
            post_checked();
        } else {
            checked = 0;
            post_checked();
        }
    });

    $('#salto').click(function () {
        post_section_break();
    });

    function post_section_break() {
        console.log("create post is working!");// sanity check
        $.ajax({
            url: $('#salto').attr('href'), // the endpoint
            type: "POST", // http method
            data: {texto: $('#texto').val()}, // data sent with the post request

            // handle a successful response
            success: function (json) {
                console.log("success"); // another sanity check
                $('.contenedor').append('<div class="ui row"></div>');
                recs.push(json.key);
            },
            // handle a non-successful response
            error: function (xhr, errmsg, err) {
                $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: " + errmsg +
                    " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    }

    function post_checked() {
        var datos = new FormData();
        datos.append('checked',checked);
        datos.append('ejercicio',$('#ejId').attr('value'));
        $.ajax({
            url: $('#checkVideo').attr('src'),
            type: "POST",
            data: datos,
            processData: false,
            contentType: false,

            // handle a successful response
            success: function (json) {
                if(json.result=='ok')
                    console.log('checkecd ok');
            },
            // handle a non-successful response
            error: function (xhr, errmsg, err) {
                console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
            }
        });
    }

});