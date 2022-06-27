(function () {

	'use strict'


	AOS.init({
		duration: 800,
		easing: 'slide',
		once: true
	});

	var preloader = function() {

		var loader = document.querySelector('.loader');
		var overlay = document.getElementById('overlayer');

		function fadeOut(el) {
			el.style.opacity = 1;
			(function fade() {
				if ((el.style.opacity -= .1) < 0) {
					el.style.display = "none";
				} else {
					requestAnimationFrame(fade);
				}
			})();
		};

		setTimeout(function() {
			fadeOut(loader);
			fadeOut(overlay);
		}, 200);
	};
	preloader();

	var tinyslider = function() {
		var el = document.querySelectorAll('.testimonial-slider');
		if ( el.length > 0 ) {
			var slider = tns({
				container: ".testimonial-slider",
				items: 1,
				axis: "horizontal",

				controlsContainer: '#testimonial-nav',
				swipeAngle: false,
				speed: 700,
				nav: true,
				controls: true,
				autoplay: true,
				autoplayHoverPause: true,
				autoplayTimeout: 3500,
				autoplayButtonOutput: false
			});
		}
	}
	tinyslider();

	var lightbox = function() {
		var lightboxVideo = GLightbox({
			selector: '.glightbox'
		});
	};
	lightbox();



})()