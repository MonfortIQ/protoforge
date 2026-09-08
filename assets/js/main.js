// main.js

document.addEventListener('DOMContentLoaded', () => {
    


    // --- Navbar Scroll Effect ---
    const navbar = document.getElementById('navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar?.classList.add('scrolled');
        } else {
            navbar?.classList.remove('scrolled');
        }
    });

    // --- Loading Screen ---
    const loadingScreen = document.getElementById('loading-screen');
    const progressBar = document.querySelector('.progress-bar-loading');
    
    if (loadingScreen && progressBar) {
        let progress = 0;
        const interval = setInterval(() => {
            progress += Math.random() * 30;
            if (progress > 100) progress = 100;
            progressBar.style.width = `${progress}%`;
            
            if (progress === 100) {
                clearInterval(interval);
                setTimeout(() => {
                    loadingScreen.style.opacity = '0';
                    setTimeout(() => {
                        loadingScreen.style.display = 'none';
                        initGSAP();
                    }, 500);
                }, 300);
            }
        }, 200);
    } else {
        initGSAP();
    }

    // --- GSAP Animations ---
    function initGSAP() {
        if (typeof gsap !== 'undefined' && typeof ScrollTrigger !== 'undefined') {
            gsap.registerPlugin(ScrollTrigger);

            // Hero Animations
            gsap.fromTo('.hero-content > *', 
                { y: 50, opacity: 0 },
                { y: 0, opacity: 1, duration: 1, stagger: 0.2, ease: 'power3.out' }
            );

            gsap.fromTo('.hero-visual', 
                { x: 50, opacity: 0 },
                { x: 0, opacity: 1, duration: 1.2, delay: 0.4, ease: 'power3.out' }
            );

            // Card Staggers on scroll
            gsap.utils.toArray('.stagger-cards').forEach(section => {
                const cards = section.querySelectorAll('.clay-card');
                if (cards.length > 0) {
                    gsap.fromTo(cards, 
                        { y: 50, opacity: 0 },
                        {
                            scrollTrigger: {
                                trigger: section,
                                start: 'top 85%',
                            },
                            y: 0,
                            opacity: 1,
                            duration: 0.8,
                            stagger: 0.1,
                            ease: 'back.out(1.2)'
                        }
                    );
                }
            });

            // Fade up elements
            gsap.utils.toArray('.fade-up').forEach(elem => {
                gsap.fromTo(elem, 
                    { y: 30, opacity: 0 },
                    {
                        scrollTrigger: {
                            trigger: elem,
                            start: 'top 90%',
                        },
                        y: 0,
                        opacity: 1,
                        duration: 0.8,
                        ease: 'power2.out'
                    }
                );
            });

            // Force recalculation after layout settles
            setTimeout(() => {
                ScrollTrigger.refresh();
            }, 500);
        }
    }
});
