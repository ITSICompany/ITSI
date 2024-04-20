const carts_cart__menu = document.getElementById("carts_cart__menu");
const carts_cart_content = document.getElementById('carts_cart_content');

var carts_cart__menu__bool = Boolean(true)

carts_cart__menu.addEventListener("click", () => {
    if (carts_cart__menu__bool) {
        carts_cart__menu__bool = false;
        carts_cart_content.style.display = 'block';
    }
    else 
    {
        carts_cart__menu__bool = true;
        carts_cart_content.style.display = 'none';
    }
});