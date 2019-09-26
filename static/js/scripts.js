AOS.init();
const searchButton = document.querySelector('#button--search');
const searchBar = document.querySelector('.search');

searchButton.addEventListener('click', () => {
    searchBar.classList.toggle('invisible');
    console.log('test');
});

const hamburgerIcon = document.querySelector('.hamburger');
const hamburgerMenu = document.querySelector('.hamburger__menu');
const hamburgerEntries = document.querySelectorAll('.hamburger__entry');

for (let i = 0; i < hamburgerEntries.length; i++) {
    let item = hamburgerEntries[i];
    item.addEventListener('click', toggleHamburger);
}

hamburgerIcon.addEventListener('click', toggleHamburger);

function toggleHamburger() {
    hamburgerIcon.classList.toggle("clicked");
    hamburgerMenu.classList.toggle("show");
}
