$(window).scroll(function(){
    if ($(window).scrollTop() > 200) {
        $('.navbar-signup').addClass('scroll');
    }
    else {
        $('.navbar-signup').removeClass('scroll')
    }
});
