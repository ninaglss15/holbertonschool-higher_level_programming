const button = document.querySelector('#update_header');
const header = document.querySelector('header');

if (button && header) {
  button.addEventListener('click', function() {
    header.textContent = 'New Header!!!';
  });
}
