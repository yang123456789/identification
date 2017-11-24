(function ($) {
    // 导航切换
    $(document).on('click', '.containers .contain ul li', function () {
        $(this).addClass('cards').siblings().removeClass('cards');
        $('.containers .tabContent .content').eq($(this).index()).show().siblings().hide();
    });

    // 信息查询
    $(document).on('click', '.containers .content #query span', function () {
        var card = $('.containers .content #query').val();
        if(validate(card)) {
            $.ajax({
                type: 'POST',
                url: '',
                data: {'card': card},
                dataType: 'json',
                success: function (msg) {
                    console.log(msg)
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
    }
})(jQuery);