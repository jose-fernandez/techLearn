
$(document).ready(function () {
    function ansel(bread) {
                bread.empty();
                var li1 = document.createElement('li');
                li1.innerHTML = ["Search"];
                bread.append(li1);
    }

    ansel($("#bread"));

    $('select.dropdown').dropdown();

    $('#units').removeClass('active');
    $('#search').addClass('active');

    var inicio = new FormData();
    inicio.append('nombre', '');
    inicio.append('tema', 'Todo');
    inicio.append('idioma', 'Todo');
    inicio.append('nivel', 'Todo');
    buscar(inicio);

    $('#btn_buscar').click(function () {
        $(this).addClass('loading');
        $('#resultados').addClass('loading');

        var datos = new FormData();
        datos.append('nombre', $('#name').val());

        if($('#idioma').find(":selected").attr('value')==0){
            datos.append('idioma', 'Todo');
        }else{
            datos.append('idioma', $('#idioma').find(":selected").text());
        }

        if($('#nivel').find(":selected").attr('value')==0){
            datos.append('nivel', 'Todo');
        }else{
            datos.append('nivel', $('#nivel').find(":selected").text());
        }

        if($('#tema').find(":selected").attr('value')==0){
            datos.append('tema', 'Todo');
        }else{
            datos.append('tema', $('#tema').find(":selected").text());
        }

        buscar(datos);
    });

    function buscar(datos) {
        $.ajax({
            url: $('#btn_buscar').attr('href'), // the endpoint
            type: "POST", // http method
            data: datos, // data sent with the post request
            processData: false,
            contentType: false,
            // handle a successful response
            success: function (json) {
                console.log(json.lista);
                $('#btn_buscar').removeClass('loading');
                $('#resultados').removeClass('loading');
                $('#resultados').html('');
                $('#resultados').append('<div class="ui sixteen wide column"><label></label></div>')
                var arr=json.lista;

                if(arr.length>0) {
                    var idcard = 0;
                    for (var i = 0; i < arr.length; i++) {
                        var obj = arr[i];
                        $('#resultados').append('' +
                            '<a class="ui raised link card" id="card_' + idcard + '" href="doProject/' + obj.id_proyecto + '">' +
                            '<div class="image">' +
                            '<video preload="auto" width="100%">' +
                            '<source src="/' + obj.media + '" type="video/webm">' +
                            '</video>' +
                            '</div>' +
                            '<div class="content">' +
                            '<p class="header">' + obj.nombre + '</p>' +
                            '<div class="description">' +
                            '' + obj.descripcion +
                            '</div>' +
                            '</div>' +
                            '<div class="extra content">' +
                            '<span class="left floated"><i class="fa icon"></i>' + obj.idioma + '</span>' +
                            '<span class="">' + obj.tema + ' </span>' +
                            '<span class="right floated">' +
                            '' + obj.nivel + '' +
                            '</span>' +
                            '</div>' +
                            '</a>');
                        if (obj.nivel == 'B2') {
                            var id = '#card_' + idcard;
                            $(id).addClass('red');
                        }
                        if (obj.nivel == 'B1') {
                            var id = '#card_' + idcard;
                            $(id).addClass('orange');
                        }
                        if (obj.nivel == 'A2') {
                            var id = '#card_' + idcard;
                            $(id).addClass('yellow');
                        }
                        if (obj.nivel == 'A1') {
                            var id = '#card_' + idcard;
                            $(id).addClass('green');
                        }
                        idcard++;

                    }
                }else {
                    $('#resultados').html('');
                    $('#resultados').append('<div class="ui yellow message">There are no results for that search</div>')
                }
            },

            error: function () {
                console.log(xhr.status + ": " + xhr.responseText);
            }
        });
    }

});

