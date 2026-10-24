const themeToggleButton = document.querySelector('#theme-toggle-button');
const body = document.querySelector('body');
const searchInput = document.querySelector('#search-input');
const bookLinks = document.querySelectorAll('.card');


const savedTheme = localStorage.getItem('theme');
if(savedTheme === 'dark'){
  body.classList.add('dark-mode');
  themeToggleButton.textContent = '☀️';
}
themeToggleButton.addEventListener('click', () => {
  body.classList.toggle('dark-mode');
  const isDarkMode = body.classList.contains('dark-mode');
  themeToggleButton.textContent = isDarkMode ? '☀️' : '🌙';
  localStorage.setItem('theme', isDarkMode ? 'dark' : 'light');
});

searchInput.addEventListener('input', () => {
  const searchTerm = searchInput.value.toLowerCase();

  bookLinks.forEach(link => {
    const bookTitle = link.querySelector('h3').textContent.toLowerCase();
    if (bookTitle.includes(searchTerm)) {
      link.style.display = 'block'; 
    } else {
      link.style.display = 'none'; 
    }
  });
});
 