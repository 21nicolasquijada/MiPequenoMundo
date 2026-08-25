// Menú móvil + animaciones GSAP (mascotas flotantes, entrada del hero, revelado al hacer scroll).
document.addEventListener('DOMContentLoaded', function () {
    var toggle = document.getElementById('navToggle');
    var nav = document.getElementById('siteNav');

    if (toggle && nav) {
        toggle.addEventListener('click', function () {
            var isOpen = nav.classList.toggle('open');
            toggle.setAttribute('aria-expanded', isOpen);
        });
    }

    // Header flotante: mide su alto real (para que el resto de la página no
    // quede tapada) y alterna a sólido apenas se hace scroll.
    var header = document.querySelector('.site-header');
    if (header) {
        var syncHeaderHeight = function () {
            document.documentElement.style.setProperty('--header-h', header.offsetHeight + 'px');
        };
        syncHeaderHeight();
        window.addEventListener('resize', syncHeaderHeight);

        var syncHeaderScrolled = function () {
            header.classList.toggle('is-scrolled', window.scrollY > 10);
        };
        syncHeaderScrolled();
        window.addEventListener('scroll', syncHeaderScrolled, { passive: true });
    }

    if (typeof gsap === 'undefined') return;

    var prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (typeof ScrollTrigger !== 'undefined') gsap.registerPlugin(ScrollTrigger);

    // Mascotas flotando libremente por detrás del contenido.
    if (!prefersReducedMotion) {
        document.querySelectorAll('.mascot').forEach(function (mascot, index) {
            var driftX = 40 + Math.random() * 60;
            var driftY = 30 + Math.random() * 50;
            var duration = 6 + Math.random() * 5;

            gsap.to(mascot, {
                x: (index % 2 === 0 ? 1 : -1) * driftX,
                y: (index % 3 === 0 ? -1 : 1) * driftY,
                rotation: (index % 2 === 0 ? 1 : -1) * 8,
                duration: duration,
                ease: 'sine.inOut',
                repeat: -1,
                yoyo: true,
                delay: index * 0.4,
            });
        });
    }

    // Entrada suave del hero de cada página.
    var heroPanel = document.querySelector('.hero-text-panel');
    var heroMedia = document.querySelector('.hero-media');
    if (heroPanel || heroMedia) {
        var heroTl = gsap.timeline({ defaults: { ease: 'power2.out', duration: 0.7 } });
        if (heroPanel) heroTl.from(heroPanel, { autoAlpha: 0, y: 24 });
        if (heroMedia) heroTl.from(heroMedia, { autoAlpha: 0, y: 24, scale: 0.97 }, '-=0.45');
    }

    // Revelado al hacer scroll para tarjetas y secciones de contenido.
    if (typeof ScrollTrigger !== 'undefined') {
        var revealSelectors = [
            '.feature-item', '.level-item', '.card', '.gallery-item',
            '.day-card', '.week-block', '.content-card', '.section-card',
        ];

        revealSelectors.forEach(function (selector) {
            var items = document.querySelectorAll(selector);
            if (!items.length) return;

            gsap.from(items, {
                autoAlpha: 0,
                y: 28,
                duration: 0.6,
                ease: 'power2.out',
                stagger: 0.08,
                scrollTrigger: {
                    trigger: items[0].closest('section') || items[0],
                    start: 'top 85%',
                    once: true,
                },
            });
        });
    }
});
