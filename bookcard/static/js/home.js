
// product card
document.addEventListener('DOMContentLoaded', () => {
    const cards = document.querySelectorAll('.card');

    cards.forEach(card => {
        card.addEventListener('mouseenter', () => {
            const button = card.querySelector('.add-to-cart');
            button.style.bottom = '0';
        });

        card.addEventListener('mouseleave', () => {
            const button = card.querySelector('.add-to-cart');
            button.style.bottom = '-40px';
        });
    });
});


// owl carousel
$(document).ready(function() {
    // Initialize Owl Carousel
    const owl = $('.owl-carousel').owlCarousel({
        loop: true,
        margin: 20,
        nav: false,
        dots: false,
        autoplay: true,
        autoplayTimeout: 8000,
        autoplayHoverPause: true,
        responsive: {
            0: {
                items: 1
            },
            600: {
                items: 2
            },
            1000: {
                items: 3
            },
            1200: {
                items: 4
            }
        }
    });

    // Custom Navigation
    $('.custom-next').click(function() {
        owl.trigger('next.owl.carousel');
    });

    $('.custom-prev').click(function() {
        owl.trigger('prev.owl.carousel');
    });

    // Add to Cart Button Animation
    $('.add-to-cart').click(function() {
        const button = $(this);
        button.css('transform', 'scale(0.95)');
        setTimeout(() => {
            button.css('transform', 'scale(1)');
        }, 100);
    });
});