const button = document.querySelector('#add_item');
const list = document.querySelector('.my_list');

if (button && list) {
  button.addEventListener('click', function() {
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';
    list.appendChild(newItem);
  });
}
