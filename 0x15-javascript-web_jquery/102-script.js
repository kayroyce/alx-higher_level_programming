document.addEventListener('DOMContentLoaded', function(){
    $('INPUT#btn_translate').click(function(){
        $.get('https://fourtonfish.com/hellosalut/?lang=' +
            $('INPUT#language_code').val(), (data) =>
                $('DIV#hello').html(data.hello))
    });
});