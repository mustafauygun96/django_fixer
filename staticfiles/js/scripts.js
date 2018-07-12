$( document ).ready(function() {
     $(".main-slider").owlCarousel({
        items: 1,
        loop: true,
        nav: false,
        navText: ['<i class="fa fa-angle-left" aria-hidden="true"></i>', '<i class="fa fa-angle-right" aria-hidden="true"></i>'],
        dots: false,
        dotsData: false,
        animateOut: 'slideOutLeft',
        animateIn: 'slideInRight',
        smartSpeed: 700,
        mouseDrag: true,
        touchDrag: true,
        autoplay:true,
        autoplayTimeout:4000,
        responsive: {
            0: {
                items: 1
            },
            920: {
                items: 1
            }
        }
    });
});