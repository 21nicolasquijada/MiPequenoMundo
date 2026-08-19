// Lightbox de la galería: abre cada foto en un popup con título y descripción.
document.addEventListener('DOMContentLoaded', function () {
    var lightbox = document.getElementById('galeriaLightbox');
    if (!lightbox) return;

    var dialog = lightbox.querySelector('.lightbox-dialog');
    var imgEl = document.getElementById('lightboxImg');
    var tituloEl = document.getElementById('lightboxTitulo');
    var descripcionEl = document.getElementById('lightboxDescripcion');
    var closeBtn = document.getElementById('lightboxClose');
    var triggers = document.querySelectorAll('[data-lightbox-trigger]');
    var lastFocused = null;
    var hasGsap = typeof gsap !== 'undefined';

    function openLightbox(trigger) {
        lastFocused = trigger;
        imgEl.src = trigger.getAttribute('data-img');
        imgEl.alt = trigger.getAttribute('data-titulo') || '';

        var titulo = trigger.getAttribute('data-titulo') || '';
        var descripcion = trigger.getAttribute('data-descripcion') || '';
        tituloEl.textContent = titulo;
        tituloEl.style.display = titulo ? '' : 'none';
        descripcionEl.textContent = descripcion;
        descripcionEl.style.display = descripcion ? '' : 'none';

        lightbox.classList.add('is-open');
        closeBtn.focus();

        if (hasGsap) {
            gsap.fromTo(lightbox, { autoAlpha: 0 }, { autoAlpha: 1, duration: 0.25, ease: 'power1.out' });
            gsap.fromTo(dialog, { autoAlpha: 0, y: 24, scale: 0.96 }, { autoAlpha: 1, y: 0, scale: 1, duration: 0.35, ease: 'back.out(1.6)' });
        }
    }

    function closeLightbox() {
        function finish() {
            lightbox.classList.remove('is-open');
            imgEl.src = '';
            if (lastFocused) lastFocused.focus();
        }

        if (hasGsap) {
            gsap.to(dialog, { autoAlpha: 0, y: 16, scale: 0.96, duration: 0.2, ease: 'power1.in' });
            gsap.to(lightbox, { autoAlpha: 0, duration: 0.2, ease: 'power1.in', onComplete: finish });
        } else {
            finish();
        }
    }

    triggers.forEach(function (trigger) {
        trigger.addEventListener('click', function () {
            openLightbox(trigger);
        });
    });

    closeBtn.addEventListener('click', closeLightbox);

    lightbox.addEventListener('click', function (event) {
        if (event.target === lightbox) closeLightbox();
    });

    document.addEventListener('keydown', function (event) {
        if (event.key === 'Escape' && lightbox.classList.contains('is-open')) closeLightbox();
    });
});
