const items = document.querySelector('carrossel-itens');
const totalItens = document.querySelectorAll('.item').length;
let currentIndex = 0;

document.querySelector('.next').addEventListener('click', () => {
    if (currentIndex < totalItens - 1) {
        currentIndex++;
        items.style.transform = `translateX(-${currentIndex * 100}%)`;
    }
});

document.querySelector('.prev').addEventListener('click', () => {
    if (currentIndex > 0) {
        currentIndex--;
        items.style.transform = `translateX(-${currentIndex * 100}%)`;
    }
})