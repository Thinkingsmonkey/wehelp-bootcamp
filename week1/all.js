const burger = document.querySelector('.menuBurger');
const menu = document.querySelector(".menu");
const burgerBg = document.querySelector('.menuBurgerBg')

function burgerActive() {
    menu.classList.toggle('active');
}

burger.addEventListener("click", burgerActive)
burgerBg.addEventListener("click", burgerActive)