document.addEventListener('DOMContentLoaded', () => {
  const api = 'https://hellosalut.stefanbohacek.com/?lang=fr';
  const helloBox = document.getElementById('hello');

  if (helloBox) {
    fetch(api)
      .then(resp => resp.json())
      .then(result => {
        helloBox.textContent = result.hello;
      });
  }
});
