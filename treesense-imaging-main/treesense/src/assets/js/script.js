// JavaScript code to toggle mobile menu visibility
const mobileMenuIcon = document.querySelector('.hamburger-icon');
const mobileMenu = document.querySelector('.mobile-menu');

if (mobileMenuIcon && mobileMenu) {
    mobileMenuIcon.addEventListener('click', () => {
        mobileMenu.classList.toggle('active');
    });
}