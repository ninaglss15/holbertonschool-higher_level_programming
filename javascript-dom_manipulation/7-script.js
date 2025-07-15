const element = document.querySelector("ul");


  async function getData() {
    const url = "https://swapi-api.hbtn.io/api/films/?format=json";
    try {
      const response = await fetch(url);
      if (!response.ok) {
        throw new Error(`Response status: ${response.status}`);
      }
  
      const json = await response.json();
      json.results.forEach((movie) => {
        element.innerHTML += `<li>${movie.title}</li>`;
    });
    } catch (error) {
      console.error(error.message);
    }
  }

  getData();