const movieList = document.querySelector('#list_movies');
const apiUrl = 'https://swapi-api.hbtn.io/api/films/?format=json';

fetch(apiUrl)
  .then(function(response) {
    return response.json();
  })
  .then(function(data) {
    const films = data.results;
    for (let i = 0; i < films.length; i++) {
      const li = document.createElement('li');
      li.textContent = films[i].title;
      movieList.appendChild(li);
    }
  });