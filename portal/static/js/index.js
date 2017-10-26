(function ($) {
    $(document).on('click', '.content .banner .head .nav li', function () {
        $(this).addClass('skit').siblings().removeClass('skit');
        $('.content .banner #subject .part').eq($(this).index()).show().siblings().hide();
    });
})(jQuery);