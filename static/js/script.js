const themeToggleButton = document.querySelector('#theme-toggle-button');
const body = document.querySelector('body');
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
