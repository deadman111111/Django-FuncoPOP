document.addEventListener('DOMContentLoaded', function () {
    const scrollContainer = document.getElementById('popular-scroll');
    const leftBtn = document.getElementById('scroll-left');
    const rightBtn = document.getElementById('scroll-right');
    const floatingBoxes = document.querySelectorAll('.floating-box');

    if (scrollContainer && leftBtn && rightBtn) {
        const scrollAmount = 320;

        leftBtn.addEventListener('click', function () {
            scrollContainer.scrollBy({
                left: -scrollAmount,
                behavior: 'smooth'
            });
        });

        rightBtn.addEventListener('click', function () {
            scrollContainer.scrollBy({
                left: scrollAmount,
                behavior: 'smooth'
            });
        });
    }

    floatingBoxes.forEach((box, index) => {
        let time = index * 0.8;

        function animate() {
            time += 0.03;
            const y = Math.sin(time) * 10;
            box.style.transform = `translateY(${y}px)`;
            requestAnimationFrame(animate);
        }

        animate();
    });
});


const featureCards = document.querySelectorAll('.feature');

featureCards.forEach(card => {

    card.addEventListener('mouseenter', () => {
        card.style.transform = 'scale(1.05)';
        card.style.transition = '0.25s ease';
        card.style.boxShadow = '0 10px 25px rgba(0,0,0,0.15)';
    });

    card.addEventListener('mouseleave', () => {
        card.style.transform = 'scale(1)';
        card.style.boxShadow = '0 6px 18px rgba(0,0,0,0.08)';
    });

});