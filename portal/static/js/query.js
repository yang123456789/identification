(function ($) {
    // 导航切换
    $(document).on('click', '.containers .contain ul li', function () {
        $(this).addClass('cards').siblings().removeClass('cards');
        $('.containers .tabContent .content').eq($(this).index()).show().siblings().hide();
    });

    // 信息查询
    $(document).on('click', '.containers .info span', function () {
        var card = $('.containers .content #query').val();
        if(validate(card)) {
            $.ajax({
                type: 'POST',
                url: '/query/info',
                data: {'card': card},
                dataType: 'json',
                success: function (msg) {
                    if(msg['status'] == 200){
                        var con = msg['message'];
                        var area = $('.containers .show .area #area');
                        var birth = $('.containers .show .area #birth');
                        var gender = $('.containers .show .area #gender');
                        area.html(con['area']);
                        birth.html(con['birthday']);
                        gender.html(con['sex']);
                        $('.containers .show .area').show();
                    }
                    else{
                        layer.msg(msg['message'], {icon: 5}, {time: 500});
                    }
                }
            });
        }
    });

    // 泄漏查询
    $(document).on('click', '.containers .leak span', function () {
        var card = $('.containers .content #leak').val();
        if(validate(card)) {
            $.ajax({
                type: 'POST',
                url: '/query/leak',
                data: {'card': card},
                dataType: 'json',
                success: function (msg) {
                    if(msg['status'] == 200){
                        var con = msg['message'];
                        var cards = $('.containers .show .leakQuery .cards #cardno');
                        var res = $('.containers .show .leakQuery .res #res');
                        var tips = $('.containers .show .leakQuery .tips #tips');
                        cards.html(con['cardno']);
                        res.html(con['res']);
                        tips.html(con['tips']);
                        $('.containers .show .leakQuery').show();
                    }
                    else{
                        layer.msg(msg['message'], {icon: 5}, {time: 500});
                    }
                }
            });
        }
    });

    // 挂失查询
    $(document).on('click', '.containers .loss span', function () {
        var card = $('.containers .content #loss').val();
        if(validate(card)) {
            $.ajax({
                type: 'POST',
                url: '/query/loss',
                data: {'card': card},
                dataType: 'json',
                success: function (msg) {
                    if(msg['status'] == 200){
                        var con = msg['message'];
                        var cards = $('.containers .show .lossQuery .cards #card-ID');
                        var res = $('.containers .show .lossQuery .res #res-id');
                        var tips = $('.containers .show .lossQuery .tips #tips-id');
                        cards.html(con['cardno']);
                        res.html(con['res']);
                        tips.html(con['tips']);
                        $('.containers .show .lossQuery').show();
                    }
                    else{
                        layer.msg(msg['message'], {icon: 5}, {time: 500});
                    }
                }
            });
        }
    });

    validate = function (id) {
        if($.isNumeric(id) == false) {
            layer.msg('身份证号码必须是数字', {icon: 5}, {time: 500});
            return false;
        }
        else if(id.length < 15 || id.length > 18) {
            layer.msg('身份证号码必须是15或18位', {icon: 5}, {time: 500});
            return false;
        }else{
            return true;
        }
    };

    // 隐藏或显示查询结果
    $(document).on('click', '.containers .contain ul .default', function () {
        $('.containers .show .showInfo').hide();
    });
})(jQuery);