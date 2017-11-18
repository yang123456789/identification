(function ($) {
    $(document).on('click', '.content .banner .head .nav li', function () {
        $(this).addClass('skit').siblings().removeClass('skit');
        $('.content .banner #subject .part').eq($(this).index()).show().siblings().hide();
    });
    // 注册
    $(document).on('click', '.container .footer #register', function () {
        var publicKey = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDp0Vu1+AX9Fmn6klmOimmI6RPmKbRfcbFwgpdKk+DkN8EeeYKzq15bS+0dsT/PixgxYT0nYbUq9UNbe8dNbXiikN87h3WXKnNSMQ1stbmjL5w7T5kRPejHFecNZ+hn1/H5P+Tp3RgpwSB8kIgmsYblF5aQM6oKZnZSW7qsICrokQIDAQAB';
        var encrypt = new JSEncrypt();
        encrypt.setPublicKey(publicKey);
        var username = $('input[name="username"]').val();
        var email = $('input[name="email"]').val();
        var password = $('input[name="password"]').val();
        $.ajax({
            type: "POST",
            url: "/register",
            data: {'username': username, 'email': email, 'password': encrypt.encrypt(password)},
            dataType: 'json',
            success: function (msg) {
                if(msg['status'] == 200) {
                    layer.msg(msg['message'], {icon: 6}, {time: 500});
                    setTimeout(function() {window.location.reload()}, 560);
                }
                else if(msg['status'] == 400) {
                    layer.msg(msg['message'], {icon: 5}, {time: 500});
                }
                else if(msg['status'] == 404) {
                    layer.msg(msg['message'], {icon: 5}, {time: 500});
                }
                else {
                    layer.msg('注册失败', {icon: 5}, {time: 500});
                }
            }
        });
    });

    // 登录
    $(document).on('click', '.container .footer #login', function () {
        var publicKey = 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDp0Vu1+AX9Fmn6klmOimmI6RPmKbRfcbFwgpdKk+DkN8EeeYKzq15bS+0dsT/PixgxYT0nYbUq9UNbe8dNbXiikN87h3WXKnNSMQ1stbmjL5w7T5kRPejHFecNZ+hn1/H5P+Tp3RgpwSB8kIgmsYblF5aQM6oKZnZSW7qsICrokQIDAQAB';
        var encrypt = new JSEncrypt();
        encrypt.setPublicKey(publicKey);
        var username = $('.container .bottom .group #username-email').val();
        var password = $('.container .bottom .group #password').val();
        $.ajax({
            type: "POST",
            url: "/login",
            data: {'username': username, 'password': encrypt.encrypt(password)},
            success: function(msg) {
                console.log(msg)
            }
        });
    });
})(jQuery);